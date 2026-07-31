#!/usr/bin/env python3
"""Validate local Markdown links and optionally check external URLs."""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parent
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PARTS = {".git", "node_modules", ".cache", "__pycache__"}


def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_PARTS for part in path.parts)
    ]


def collect_links() -> tuple[list[tuple[Path, str]], list[str]]:
    local_links: list[tuple[Path, str]] = []
    external_links: set[str] = set()
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw_link in LINK_PATTERN.findall(text):
            link = raw_link.strip().strip("<>")
            if not link or link.startswith(("#", "mailto:")) or "{" in link:
                continue
            parsed = urlparse(link)
            if parsed.scheme in {"http", "https"}:
                external_links.add(link)
            elif not parsed.scheme:
                local_links.append((path, unquote(link.split("#", 1)[0])))
    return local_links, sorted(external_links)


def check_external(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "codex-student-starter-link-check/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=8) as response:
            return 200 <= response.status < 400, str(response.status)
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405}:
            fallback = urllib.request.Request(
                url,
                method="GET",
                headers={"User-Agent": "codex-student-starter-link-check/1.0"},
            )
            try:
                with urllib.request.urlopen(fallback, timeout=8) as response:
                    return 200 <= response.status < 400, str(response.status)
            except Exception as fallback_exc:  # network diagnostics only
                return False, str(fallback_exc)
        return False, str(exc.code)
    except Exception as exc:  # network diagnostics only
        return False, str(exc)


def main() -> int:
    online = "--online" in sys.argv[1:]
    local_links, external_links = collect_links()
    missing: list[str] = []

    for source, relative in local_links:
        if not relative:
            continue
        target = (source.parent / relative).resolve()
        if not target.exists():
            missing.append(f"{source.relative_to(ROOT)} -> {relative}")

    if missing:
        print("本地連結失敗：")
        for item in missing:
            print(f"- {item}")
    else:
        print(f"本地連結通過：{len(local_links)} 個")

    print(f"外部網址：{len(external_links)} 個")
    if online:
        print("開始線上檢查；此模式需要網路權限。")
        external_failures: list[str] = []
        for url in external_links:
            ok, detail = check_external(url)
            print(f"- {'PASS' if ok else 'FAIL'} {url} [{detail}]")
            if not ok:
                external_failures.append(url)
        if external_failures:
            return 1
    else:
        for url in external_links:
            print(f"- {url}")
        print("未執行線上存取；取得網路授權後，Windows 使用 check.ps1 -Online，macOS 使用 sh ./check.sh --online。")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
