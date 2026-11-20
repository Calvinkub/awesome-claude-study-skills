#!/usr/bin/env bash
# Install study skills into Claude Code.
# Usage:
#   ./install-skills.sh                 # install all skills globally (~/.claude/skills)
#   ./install-skills.sh --project       # install all skills into ./.claude/skills
#   ./install-skills.sh exam-quiz ...   # install only the named skills
#   ./install-skills.sh --zip           # build one ZIP per skill in ./dist for claude.ai upload
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skills"
DEST="$HOME/.claude/skills"
MODE="install"
SELECTED=()

for arg in "$@"; do
  case "$arg" in
    --project) DEST="$PWD/.claude/skills" ;;
    --zip) MODE="zip" ;;
    -h|--help) sed -n '2,7p' "$0"; exit 0 ;;
    *) SELECTED+=("$arg") ;;
  esac
done

if [ ${#SELECTED[@]} -eq 0 ]; then
  for d in "$SRC"/*/; do SELECTED+=("$(basename "$d")"); done
fi

for name in "${SELECTED[@]}"; do
  if [ ! -f "$SRC/$name/SKILL.md" ]; then
    echo "Unknown skill: $name" >&2
    exit 1
  fi
done

if [ "$MODE" = "zip" ]; then
  mkdir -p "$REPO_DIR/dist"
  for name in "${SELECTED[@]}"; do
    (cd "$SRC" && rm -f "$REPO_DIR/dist/$name.zip" && zip -qr "$REPO_DIR/dist/$name.zip" "$name")
    echo "Built dist/$name.zip"
  done
  echo "Upload in claude.ai: Settings > Capabilities (code execution on) > Skills > Upload."
  exit 0
fi

mkdir -p "$DEST"
for name in "${SELECTED[@]}"; do
  rm -rf "${DEST:?}/$name"
  cp -R "$SRC/$name" "$DEST/$name"
  echo "Installed $name -> $DEST/$name"
done
echo "Done. In Claude Code, run /<skill-name>, e.g. /study-session"
