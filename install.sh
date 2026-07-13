#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TOOLS=(claude codex kiro cursor)
LANGS=(java scala go typescript python rust)
CATEGORIES=(best-practices lint security static-scan)

tool=""
lang=""
scope=""
target="$PWD"
dry_run=0
force=0

usage() {
  cat <<'USAGE'
Usage:
  ./install.sh
  ./install.sh --tool <claude|codex|kiro|cursor|all> --lang <java|scala|go|typescript|python|rust|all> [--scope personal|project]

Options:
  --tool TOOL       AI tool to install for
  --lang LANG       Programming language to install
  --scope SCOPE     personal or project (default: personal)
  --target PATH     Project target directory for --scope project (default: current directory)
  --dry-run         Print actions without copying files
  --force           Replace existing installed skill directories
  --list            List supported tools, languages, and skill categories
  -h, --help        Show this help
USAGE
}

join_by_comma() {
  local out=""
  local item
  for item in "$@"; do
    if [[ -z "$out" ]]; then
      out="$item"
    else
      out="$out, $item"
    fi
  done
  echo "$out"
}

contains() {
  local needle="$1"
  shift
  local item
  for item in "$@"; do
    [[ "$item" == "$needle" ]] && return 0
  done
  return 1
}

list_supported() {
  echo "Tools: $(join_by_comma "${TOOLS[@]}"), all"
  echo "Languages: $(join_by_comma "${LANGS[@]}"), all"
  echo "Categories: $(join_by_comma "${CATEGORIES[@]}")"
}

personal_dest() {
  case "$1" in
    claude) echo "$HOME/.claude/skills" ;;
    codex) echo "${CODEX_HOME:-$HOME/.codex}/skills" ;;
    kiro) echo "$HOME/.kiro/skills" ;;
    cursor) echo "$HOME/.cursor/skills" ;;
    *) echo "unknown tool: $1" >&2; exit 1 ;;
  esac
}

project_dest() {
  case "$1" in
    claude) echo "$target/.claude/skills" ;;
    codex) echo "$target/.codex/skills" ;;
    kiro) echo "$target/.kiro/skills" ;;
    cursor) echo "$target/.cursor/skills" ;;
    *) echo "unknown tool: $1" >&2; exit 1 ;;
  esac
}

install_one() {
  local selected_tool="$1"
  local selected_lang="$2"
  local src_dir="$ROOT_DIR/$selected_lang/$selected_tool"
  local dest_root
  local skill_src
  local skill_name
  local skill_dest

  [[ -d "$src_dir" ]] || {
    echo "Missing source directory: $src_dir" >&2
    exit 1
  }

  if [[ "$scope" == "personal" ]]; then
    dest_root="$(personal_dest "$selected_tool")"
  else
    dest_root="$(project_dest "$selected_tool")"
  fi

  for skill_src in "$src_dir"/*; do
    [[ -d "$skill_src" ]] || continue
    skill_name="$(basename "$skill_src")"
    skill_dest="$dest_root/$skill_name"

    if [[ "$dry_run" == 1 ]]; then
      echo "Would install $selected_lang/$selected_tool/$skill_name -> $skill_dest"
      continue
    fi

    mkdir -p "$dest_root"

    if [[ -e "$skill_dest" ]]; then
      if [[ "$force" == 1 ]]; then
        rm -rf "$skill_dest"
      else
        echo "Skipping existing $skill_dest (use --force to replace)"
        continue
      fi
    fi

    cp -R "$skill_src" "$skill_dest"
    echo "Installed $selected_lang/$selected_tool/$skill_name -> $skill_dest"
  done
}

prompt_if_needed() {
  if [[ -z "$tool" ]]; then
    echo "Choose AI tool:"
    select choice in "${TOOLS[@]}" all; do
      tool="$choice"
      break
    done
  fi

  if [[ -z "$lang" ]]; then
    echo "Choose programming language:"
    select choice in "${LANGS[@]}" all; do
      lang="$choice"
      break
    done
  fi

  if [[ -z "$scope" ]]; then
    echo "Choose install scope:"
    select choice in personal project; do
      scope="$choice"
      break
    done
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool) tool="${2:-}"; shift 2 ;;
    --lang|--language) lang="${2:-}"; shift 2 ;;
    --scope) scope="${2:-}"; shift 2 ;;
    --target) target="${2:-}"; shift 2 ;;
    --dry-run) dry_run=1; shift ;;
    --force) force=1; shift ;;
    --list) list_supported; exit 0 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

prompt_if_needed

[[ "$scope" == "personal" || "$scope" == "project" ]] || {
  echo "Invalid scope: $scope" >&2
  exit 1
}

if [[ "$tool" != "all" ]] && ! contains "$tool" "${TOOLS[@]}"; then
  echo "Invalid tool: $tool" >&2
  list_supported
  exit 1
fi

if [[ "$lang" != "all" ]] && ! contains "$lang" "${LANGS[@]}"; then
  echo "Invalid language: $lang" >&2
  list_supported
  exit 1
fi

selected_tools=()
selected_langs=()

if [[ "$tool" == "all" ]]; then
  selected_tools=("${TOOLS[@]}")
else
  selected_tools=("$tool")
fi

if [[ "$lang" == "all" ]]; then
  selected_langs=("${LANGS[@]}")
else
  selected_langs=("$lang")
fi

for selected_lang in "${selected_langs[@]}"; do
  for selected_tool in "${selected_tools[@]}"; do
    install_one "$selected_tool" "$selected_lang"
  done
done
