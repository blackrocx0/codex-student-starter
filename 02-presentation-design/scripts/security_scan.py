#!/usr/bin/env python3
"""Scan repository text files for common secrets and private local identifiers."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()
MAX_FILE_SIZE = 2 * 1024 * 1024

SKIP_PARTS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".cache",
    ".codex-log",
}

SUSPICIOUS_FILENAMES = {
    ".env",
    "credentials.json",
    "service-account.json",
    "id_rsa",
    "id_ed25519",
}

PATTERNS = (
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    (
        "Private key",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
    (
        "Assigned secret",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)"
            r"\s*[:=]\s*[\"']?(?!<|\\{|example|demo|your-)[A-Za-z0-9/+_=.-]{12,}"
        ),
    ),
    (
        "Windows user path",
        re.compile(r"(?i)\b[A-Z]:\\Users\\(?!<|your-|student)[^\\\s]+\\"),
    ),
    (
        "macOS user path",
        re.compile(r"(?i)(?<![A-Za-z0-9_])/Users/(?!<|your-|student)[^/\s]+/"),
    ),
    (
        "Non-example email",
        re.compile(
            r"\b[A-Z0-9._%+-]+@(?!example\.com\b)[A-Z0-9.-]+\.[A-Z]{2,}\b",
            re.IGNORECASE,
        ),
    ),
)


def should_skip(path: Path) -> bool:
    if path.resolve() == SELF or path.name == "security_scan.py":
        return True
    if any(part in SKIP_PARTS for part in path.parts):
        return True
    return False


def main() -> int:
    findings: list[tuple[str, str, int]] = []

    for path in ROOT.rglob("*"):
        if not path.is_file() or should_skip(path):
            continue
        relative = path.relative_to(ROOT).as_posix()

        if path.name in SUSPICIOUS_FILENAMES or (
            path.name.startswith(".env.") and path.name != ".env.example"
        ):
            findings.append((relative, "可疑憑證檔名", 0))

        try:
            if path.stat().st_size > MAX_FILE_SIZE:
                continue
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append((relative, label, line_number))

    if findings:
        print("發現可能的敏感資訊；內容已遮蔽，只顯示位置：")
        for relative, label, line_number in findings:
            suffix = f":{line_number}" if line_number else ""
            print(f"- {relative}{suffix} [{label}]")
        print("請人工確認；若是真實憑證，先撤銷／輪換，再處理 Git 歷史。")
        return 1

    print("資安掃描通過：未發現常見 key、token、私人金鑰、非示範信箱或私人 Windows／macOS 路徑。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
