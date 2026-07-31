#!/usr/bin/env python3
"""Validate a freshly cloned three-project student framework."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_PROJECTS = {
    "01-llm-wiki": [
        "AGENTS.md",
        "README.md",
        ".agents/skills/wiki-ingest/SKILL.md",
        ".agents/skills/wiki-query/SKILL.md",
        "wiki/index.md",
        "wiki/log.md",
    ],
    "02-schedule-assistant": [
        "AGENTS.md",
        "README.md",
        ".agents/skills/schedule-planning/SKILL.md",
        "preferences.example.yaml",
        "pending_items.md",
        "scripts/bootstrap.py",
    ],
    "03-presentation-framework": [
        "AGENTS.md",
        "README.md",
        ".agents/skills/presentation-yaml/SKILL.md",
        "examples/demo-process-flow.assembled.yaml",
        "scripts/validate_slide_yaml.py",
    ],
}
ROOT_FILES = (
    "AGENTS.md",
    "README.md",
    "INSTALL.md",
    "INSTALL_PROMPT.txt",
    "PERMISSIONS.md",
    "PROJECTS.md",
    "SECURITY.md",
    "link_check.py",
    "security_scan.py",
)


def command_version(command: str) -> str | None:
    executable = shutil.which(command)
    if not executable:
        return None
    try:
        result = subprocess.run(
            [executable, "--version"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return "已找到，但無法讀取版本"
    lines = (result.stdout or result.stderr).strip().splitlines()
    return lines[0] if lines else "已找到"


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    print("Codex 學員框架安裝檢查")
    print(f"- 目前根目錄：{ROOT}")
    print(f"- Python：{sys.version.split()[0]}")

    for filename in ROOT_FILES:
        if not (ROOT / filename).is_file():
            failures.append(f"缺少根目錄檔案：{filename}")

    for project, required_files in EXPECTED_PROJECTS.items():
        project_root = ROOT / project
        if not project_root.is_dir():
            failures.append(f"缺少專案資料夾：{project}")
            continue
        for relative in required_files:
            if not (project_root / relative).is_file():
                failures.append(f"缺少檔案：{project}/{relative}")
        skill_count = len(list((project_root / ".agents" / "skills").glob("*/SKILL.md")))
        print(f"- {project}：{skill_count} 個本地 Skill")

    visible_directories = sorted(
        path.name for path in ROOT.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    expected_directories = sorted(EXPECTED_PROJECTS)
    if visible_directories != expected_directories:
        failures.append(
            "可見資料夾不符合預期：" + ", ".join(visible_directories or ["<none>"])
        )

    for obsolete in ("00-start-here", "modules", ".agents", "student-profile.yaml"):
        if (ROOT / obsolete).exists():
            failures.append(f"根目錄仍有舊版或混合架構殘留：{obsolete}")

    try:
        with tempfile.NamedTemporaryFile(prefix=".install-write-test-", dir=ROOT, delete=True):
            pass
        print("- Workspace：可寫入")
    except OSError as exc:
        failures.append(f"目前資料夾無法寫入：{exc}")

    for command in ("git", "codex"):
        version = command_version(command)
        if version:
            print(f"- {command}：{version}")
        else:
            warnings.append(f"PATH 找不到 {command}")

    if not (ROOT / ".git").exists():
        warnings.append("目前沒有 .git；本機設計檢查可用，但尚未證明是由 GitHub clone 安裝。")
    elif shutil.which("git"):
        try:
            remote = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=5,
            )
            origin = remote.stdout.strip()
            if remote.returncode == 0 and origin:
                print(f"- Git origin：{origin}")
            else:
                warnings.append("Git repository 沒有可辨識的 origin URL。")
        except (OSError, subprocess.SubprocessError) as exc:
            warnings.append(f"無法讀取 Git origin：{exc}")

    if warnings:
        print("提醒：")
        for warning in warnings:
            print(f"- {warning}")

    if failures:
        print("失敗：")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("結果：三個專案結構完整且彼此隔離。")
    print("下一步：執行 security_scan.py 與 link_check.py，再請使用者選擇一個專案資料夾。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
