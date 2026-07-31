#!/bin/sh
set -eu

case "$0" in
    /*) SCRIPT_PATH=$0 ;;
    *) SCRIPT_PATH=$PWD/$0 ;;
esac
SCRIPT_DIR=${SCRIPT_PATH%/*}
SCRIPT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR" && pwd)
PROJECT_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
EXAMPLE="$PROJECT_ROOT/preferences.example.yaml"
PREFERENCES="$PROJECT_ROOT/preferences.yaml"
PLANS="$PROJECT_ROOT/plans"
MARKER="$PROJECT_ROOT/.schedule-init.json"

if [ -f "$PREFERENCES" ]; then
    printf '%s\n' "KEEP: preferences.yaml"
else
    cp "$EXAMPLE" "$PREFERENCES"
    printf '%s\n' "CREATE: preferences.yaml"
fi

mkdir -p "$PLANS"

if [ -f "$MARKER" ]; then
    printf '%s\n' "KEEP: .schedule-init.json"
else
    INITIALIZED_AT=$(date -u "+%Y-%m-%dT%H:%M:%SZ")
    {
        printf '%s\n' '{'
        printf '%s\n' '  "schema_version": 1,'
        printf '%s\n' '  "initialized": true,'
        printf '  "initialized_at": "%s"\n' "$INITIALIZED_AT"
        printf '%s\n' '}'
    } > "$MARKER"
    printf '%s\n' "CREATE: .schedule-init.json"
fi

printf '%s\n' "Work program initialized. Ask for timezone before date planning."
