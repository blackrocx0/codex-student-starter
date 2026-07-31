#!/bin/sh
set -eu

case "$0" in
    /*) SCRIPT_PATH=$0 ;;
    *) SCRIPT_PATH=$PWD/$0 ;;
esac
SCRIPT_DIR=${SCRIPT_PATH%/*}
SCRIPT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR" && pwd)
cd "$SCRIPT_DIR"

if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
else
    echo "找不到 Python 3.9+。請勿自動安裝；改由 Codex 執行 README.md 所述的唯讀人工檢查。" >&2
    exit 1
fi

printf '%s\n' "Platform: macOS / POSIX"
"$PYTHON" doctor.py
"$PYTHON" security_scan.py
if [ "${1:-}" = "--online" ]; then
    "$PYTHON" link_check.py --online
else
    "$PYTHON" link_check.py
fi
printf '%s\n' "macOS / POSIX checks passed."
