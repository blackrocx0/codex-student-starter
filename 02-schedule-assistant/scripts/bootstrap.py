#!/usr/bin/env python3
"""Initialize schedule preferences inside this project only."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    example = ROOT / "preferences.example.yaml"
    preferences = ROOT / "preferences.yaml"
    plans = ROOT / "plans"
    marker = ROOT / ".schedule-init.json"

    if preferences.exists():
        print("KEEP: preferences.yaml")
    else:
        shutil.copyfile(example, preferences)
        print("CREATE: preferences.yaml")

    plans.mkdir(parents=True, exist_ok=True)

    if marker.exists():
        print("KEEP: .schedule-init.json")
    else:
        marker.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "initialized": True,
                    "initialized_at": datetime.now(timezone.utc).isoformat(),
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print("CREATE: .schedule-init.json")

    print("Schedule project initialized. Ask for timezone before date planning.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
