#!/usr/bin/env python3
"""Validate the fixed top-level shape of a seven-section assembled slide YAML."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED = [
    "page_type_and_mood",
    "visual_base_2a",
    "corner_decoration_2b",
    "layout_description",
    "content",
    "safe_zone_constraints",
    "closing_design_intent",
]

REQUIRED_FRAGMENTS = (
    "background:",
    "typography:",
    "color_system:",
    "illustration_style:",
    "structure:",
    "hard_constraint:",
    "edge_rule:",
)


def main() -> int:
    if len(sys.argv) != 2:
        print("用法：Windows 使用 py -3 scripts/validate_slide_yaml.py <yaml-path>；macOS 使用 python3 scripts/validate_slide_yaml.py <yaml-path>")
        return 2

    path = Path(sys.argv[1])
    if not path.is_absolute():
        path = Path.cwd() / path

    if not path.is_file():
        print(f"找不到檔案：{path}")
        return 2

    text = path.read_text(encoding="utf-8")
    top_level = []
    for line in text.splitlines():
        if not line or line.startswith((" ", "\t", "#", "---")):
            continue
        match = re.match(r"^([a-z0-9_]+):(?:\s.*)?$", line)
        if match:
            top_level.append(match.group(1))

    errors: list[str] = []
    if top_level != EXPECTED:
        errors.append(
            "Top-level 區段或順序不正確："
            + ", ".join(top_level or ["<none>"])
        )

    for fragment in REQUIRED_FRAGMENTS:
        if fragment not in text:
            errors.append(f"缺少必要子欄位：{fragment}")

    unresolved = [
        marker
        for marker in ("{TITLE}", "{SUBTITLE}", "<field_", "<zone_", "TODO")
        if marker in text
    ]
    if unresolved:
        errors.append("仍有未填佔位符：" + ", ".join(unresolved))

    if errors:
        print(f"驗證失敗：{path}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"驗證通過：{path}")
    print("- 七個 top-level 區段齊全且順序正確")
    print("- 必要結構欄位存在")
    print("- 未發現已知佔位符")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
