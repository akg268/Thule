#!/usr/bin/env python3
"""Generate tool-native Agent Skill packages for language quality workflows."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import textwrap


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ("claude", "codex", "kiro", "cursor")


LANGUAGES = {
    "java": {
        "display": "Java",
        "globs": "`**/*.java`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle*`",
        "sources": [
            ("Oracle Code Conventions for the Java Programming Language", "https://www.oracle.com/java/technologies/javase/codeconventions-contents.html"),
            ("Oracle Secure Coding Guidelines for Java SE", "https://www.oracle.com/java/technologies/javase/seccodeguide.html"),
            ("Oracle javac command", "https://docs.oracle.com/en/java/javase/26/docs/specs/man/javac.html"),
            ("Oracle jdeps command", "https://docs.oracle.com/en/java/javase/26/docs/specs/man/jdeps.html"),
            ("Oracle jdeprscan command", "https://docs.oracle.com/en/java/javase/26/docs/specs/man/jdeprscan.html"),
            ("OWASP Dependency-Check", "https://owasp.org/www-project-dependency-check/"),
        ],
        "best": [
            "Prefer explicit, small APIs with private fields and cohesive classes.",
            "Follow established Java naming: classes in UpperCamelCase, methods and variables in lowerCamelCase, constants in uppercase words.",
            "Use packages, imports, declarations, comments, and whitespace consistently with the project style; do not churn unrelated formatting.",
            "Document public APIs and security-relevant preconditions with Javadoc.",
            "Use modern language features only when the configured source or release level supports them.",
        ],
        "lint": [
            "Prefer the project formatter and build tasks when present.",
            "Run `javac -Xlint` or the build equivalent to surface compiler lint categories.",
            "Treat `-Werror` as a project decision; do not introduce it unless the repo already enforces warnings as errors.",
            "Use `javadoc -Xdoclint` when the change affects public API documentation.",
            "For Maven or Gradle projects, prefer existing `mvn test`, `mvn verify`, `gradle check`, or wrapper scripts.",
        ],
        "security": [
            "Model trust boundaries and validate data crossing them before use.",
            "Restrict privileges and isolate untrusted code, users, data, services, and dependencies.",
            "Release resources in all paths with try-with-resources or clear acquire/release pairing.",
            "Avoid unsafe deserialization, reflection exposure, injection sinks, and unbounded resource consumption.",
            "Track third-party dependency updates and apply security fixes promptly.",
        ],
        "scan": [
            "Run `jdeps` to inspect dependencies, module boundaries, and JDK internal API use.",
            "Run `jdeprscan` against built class directories or JARs to find Java SE deprecated API use.",
            "Run `javac -Xlint:all` through the project build when practical.",
            "Run OWASP Dependency-Check for Maven, Gradle, CLI, or CI dependency vulnerability scanning when configured.",
            "Report tool versions, command exits, and any warnings left unresolved.",
        ],
    },
    "scala": {
        "display": "Scala",
        "globs": "`**/*.scala`, `build.sbt`, `project/*.scala`, `.scalafmt.conf`, `.scalafix.conf`",
        "sources": [
            ("Scala Style Guide", "https://docs.scala-lang.org/style/"),
            ("Scala Futures and Promises", "https://docs.scala-lang.org/overviews/core/futures.html"),
            ("Scalafmt documentation", "https://scalameta.org/scalafmt/"),
            ("Scalafix documentation", "https://scalacenter.github.io/scalafix/"),
            ("OWASP Dependency-Check", "https://owasp.org/www-project-dependency-check/"),
        ],
        "best": [
            "Follow the local Scala version and style before introducing syntax or idioms from another version.",
            "Use clear names, small expressions, and explicit public API types where inference would hide intent.",
            "Keep effects, blocking, and concurrency boundaries visible.",
            "Avoid unnecessary symbolic methods, structural types, and clever implicit or given resolution.",
            "Prefer standard library and project-established abstractions over new helper layers.",
        ],
        "lint": [
            "Run `scalafmt --check` or the build-tool equivalent when `.scalafmt.conf` exists.",
            "Run `scalafix --check` or the sbt/CLI equivalent when `.scalafix.conf` exists.",
            "Use the repository's sbt, Maven, Gradle, or Mill lint/check tasks before inventing new commands.",
            "Treat compiler warnings as actionable; preserve existing warning policy.",
            "Do not reformat files outside the requested change unless the project task already does so.",
        ],
        "security": [
            "Validate untrusted input at trust boundaries before parsing, interpolation, file access, or command execution.",
            "Avoid blocking on the global execution context; mark unavoidable blocking with `blocking` and prefer dedicated execution contexts.",
            "Keep secrets out of source, tests, logs, and generated examples.",
            "Handle failed futures and effects explicitly; do not discard errors with unsafe callbacks.",
            "Scan JVM dependencies for known vulnerable components when dependency metadata changes.",
        ],
        "scan": [
            "Run `scalafix --check` for configured semantic or syntactic rules.",
            "Run `scalafmt --check` for formatting drift.",
            "Run the repo's compiler check with warnings enabled, usually through `sbt Test/compile`, `sbt test`, `mill __.test`, or existing CI scripts.",
            "Run OWASP Dependency-Check through Maven, Gradle, CLI, or configured CI for dependency vulnerabilities.",
            "Summarize findings by source file, rule, severity, and whether a fix was applied.",
        ],
    },
    "go": {
        "display": "Go",
        "globs": "`**/*.go`, `go.mod`, `go.sum`",
        "sources": [
            ("Effective Go", "https://go.dev/doc/effective_go"),
            ("Go security documentation", "https://go.dev/doc/security/"),
            ("go command documentation", "https://pkg.go.dev/cmd/go"),
            ("govulncheck tutorial", "https://go.dev/doc/tutorial/govulncheck"),
        ],
        "best": [
            "Let `gofmt` decide formatting; do not hand-align code in ways gofmt will undo.",
            "Use short, clear package names and avoid underscores or mixedCaps in package names.",
            "Return errors directly and keep the successful path easy to read.",
            "Prefer simple interfaces defined near consumers, especially one-method interfaces with conventional names.",
            "Use context-aware APIs for cancellation, timeouts, and request-scoped values.",
        ],
        "lint": [
            "Run `gofmt` or `go fmt ./...` for formatting.",
            "Run `go vet ./...` for likely mistakes and high-confidence diagnostics.",
            "Run `go test ./...` because it also runs a curated subset of vet checks by default.",
            "Preserve module compatibility and avoid unnecessary `go mod tidy` churn.",
            "Use existing `make`, `just`, or CI lint targets when present.",
        ],
        "security": [
            "Use `govulncheck ./...` to identify known vulnerabilities that are reachable from code paths.",
            "Validate external input before parsing, file operations, templates, SQL, shell commands, or network calls.",
            "Use `crypto/rand` or appropriate crypto packages for security-sensitive randomness.",
            "Propagate and handle errors; never ignore errors from security-relevant operations.",
            "Keep dependencies updated with minimal, reviewable `go.mod` and `go.sum` changes.",
        ],
        "scan": [
            "Run `go vet ./...` for static diagnostics.",
            "Run `go test ./...` to compile and test all packages with default vet coverage.",
            "Run `govulncheck ./...` for reachable vulnerability analysis.",
            "Use `go version -m` when inspecting built binaries for embedded module metadata.",
            "Report whether vulnerabilities are called by the code or only present in imported modules.",
        ],
    },
    "typescript": {
        "display": "TypeScript",
        "globs": "`**/*.ts`, `**/*.tsx`, `tsconfig*.json`, `eslint.config.*`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`",
        "sources": [
            ("TypeScript Handbook", "https://www.typescriptlang.org/docs/handbook/intro.html"),
            ("TSConfig strict option", "https://www.typescriptlang.org/tsconfig/strict.html"),
            ("typescript-eslint Getting Started", "https://typescript-eslint.io/getting-started/"),
            ("npm audit documentation", "https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities/"),
        ],
        "best": [
            "Prefer precise types, narrowing, discriminated unions, and explicit public API boundaries.",
            "Keep `strict` enabled when already configured; do not weaken strictness to silence errors.",
            "Avoid `any`, non-null assertions, broad type assertions, and suppressed errors unless the risk is documented.",
            "Respect the repo's module system, runtime target, JSX mode, and package manager.",
            "Separate validation of untrusted runtime data from compile-time TypeScript types.",
        ],
        "lint": [
            "Run `tsc --noEmit` or the repo's typecheck script.",
            "Run ESLint through the repo script, usually `npm run lint`, `pnpm lint`, or `yarn lint`.",
            "Use `typescript-eslint` recommended or type-aware linting only when the repo is configured for it.",
            "Do not introduce Prettier, ESLint, or config migrations unless the task requests it.",
            "Keep generated files, build outputs, and vendored code out of lint fixes.",
        ],
        "security": [
            "Validate untrusted data at runtime before trusting TypeScript types.",
            "Avoid unsafe DOM insertion, command execution, dynamic evaluation, and string-built SQL or shell commands.",
            "Keep secrets out of source, tests, logs, browser bundles, and checked-in env files.",
            "Use dependency audit tooling from the active package manager before changing lockfiles.",
            "Prefer least-privilege tokens, scoped permissions, and explicit error handling around security boundaries.",
        ],
        "scan": [
            "Run `tsc --noEmit` for static type analysis.",
            "Run ESLint with the existing `eslint.config.*` or package script.",
            "Run `npm audit`, `pnpm audit`, or `yarn npm audit` according to the lockfile and package manager.",
            "Review lockfile-only changes carefully and avoid broad dependency upgrades without need.",
            "Report type errors, lint rules, vulnerable packages, severities, and fix versions separately.",
        ],
    },
    "python": {
        "display": "Python",
        "globs": "`**/*.py`, `pyproject.toml`, `requirements*.txt`, `poetry.lock`, `uv.lock`, `Pipfile.lock`",
        "sources": [
            ("PEP 8", "https://peps.python.org/pep-0008/"),
            ("Python security considerations", "https://docs.python.org/3/library/security_warnings.html"),
            ("Ruff documentation", "https://docs.astral.sh/ruff/"),
            ("Bandit documentation", "https://bandit.readthedocs.io/en/latest/"),
            ("pip-audit", "https://pypi.org/project/pip-audit/"),
        ],
        "best": [
            "Follow PEP 8 unless the project has a stronger local style.",
            "Prefer readable, explicit code with clear names, small functions, and grouped imports.",
            "Use type hints where the project expects them; do not add typing churn to unrelated code.",
            "Use context managers for resources and avoid broad exception swallowing.",
            "Keep dependency metadata and lockfiles minimal and intentional.",
        ],
        "lint": [
            "Run `ruff check .` when Ruff is configured or already used.",
            "Run `ruff format --check .` or the project formatter check when present.",
            "Run the repo's test command, commonly `pytest`, `python -m pytest`, or configured task runners.",
            "Use `python -m compileall` for syntax checks when no richer project command exists.",
            "Do not add new lint tools where a project already standardizes on another tool.",
        ],
        "security": [
            "Review Python standard library modules with documented security considerations before using them on untrusted data.",
            "Avoid unsafe `pickle`, `eval`, shell invocation, temp-file races, XML parsing, and weak randomness.",
            "Use `secrets` instead of `random` for security-sensitive values.",
            "Keep secrets out of code, tests, logs, notebooks, and generated fixtures.",
            "Audit dependencies with `pip-audit` when dependency metadata changes.",
        ],
        "scan": [
            "Run `ruff check .` for lint and static diagnostics.",
            "Run `bandit -r .` for common Python security issue scanning when Bandit is available.",
            "Run `pip-audit` against the project or requirements files for known vulnerable dependencies.",
            "Run `python -m compileall` when syntax coverage is needed without importing application code.",
            "Report findings with file, rule ID, severity, confidence, and whether auto-fix was used.",
        ],
    },
    "rust": {
        "display": "Rust",
        "globs": "`**/*.rs`, `Cargo.toml`, `Cargo.lock`, `rustfmt.toml`, `clippy.toml`",
        "sources": [
            ("Rust API Guidelines", "https://rust-lang.github.io/api-guidelines/"),
            ("Clippy documentation", "https://doc.rust-lang.org/clippy/"),
            ("rustfmt documentation", "https://rust-lang.github.io/rustfmt/"),
            ("RustSec Advisory Database", "https://rustsec.org/"),
        ],
        "best": [
            "Follow Rust API Guidelines for naming, interoperability, documentation, predictability, and type safety.",
            "Prefer safe Rust and isolate unavoidable `unsafe` behind small, documented invariants.",
            "Use ownership, borrowing, `Result`, and `Option` deliberately instead of panics in library code.",
            "Keep public APIs future-proof and avoid exposing unnecessary concrete implementation details.",
            "Use feature flags and dependency choices conservatively.",
        ],
        "lint": [
            "Run `cargo fmt --check` when rustfmt is available.",
            "Run `cargo clippy --all-targets --all-features` or the repo's clippy command.",
            "Do not enable all `clippy::restriction`; choose restriction lints case by case.",
            "Run `cargo test` or the repo's test matrix before finalizing behavioral changes.",
            "Preserve existing `clippy.toml`, `rustfmt.toml`, and workspace policy.",
        ],
        "security": [
            "Treat `unsafe` as security-sensitive: document invariants and minimize scope.",
            "Avoid panics, unchecked indexing, path traversal, command injection, and secret leakage on untrusted inputs.",
            "Use constant-time and audited crypto crates where security properties matter.",
            "Audit dependencies with RustSec tooling when `Cargo.lock` changes.",
            "Review transitive dependency, license, and source policies when `cargo-deny` is configured.",
        ],
        "scan": [
            "Run `cargo check --all-targets --all-features` for static type and borrow checking.",
            "Run `cargo clippy --all-targets --all-features` for Rust lints.",
            "Run `cargo fmt --check` for formatting.",
            "Run `cargo audit` or `cargo deny check advisories` when configured for dependency vulnerability scanning.",
            "Report any `unsafe`, clippy warnings, advisory IDs, affected crates, and fix versions.",
        ],
    },
}


CATEGORIES = {
    "best-practices": {
        "title": "Best Practices",
        "summary": "best practices and idiomatic code guidance",
        "focus": "Write and review maintainable, idiomatic code while preserving the repository's existing architecture and conventions.",
        "key": "best",
    },
    "lint": {
        "title": "Lint",
        "summary": "linting and formatting guidance",
        "focus": "Find and fix lint or formatting issues using existing project tooling before adding anything new.",
        "key": "lint",
    },
    "security": {
        "title": "Security",
        "summary": "secure coding guidance",
        "focus": "Review code for security risks, validate trust boundaries, and keep secrets and dependency risk visible.",
        "key": "security",
    },
    "static-scan": {
        "title": "Static Scan",
        "summary": "static analysis and scanner workflow guidance",
        "focus": "Run static analyzers, type checkers, vulnerability scanners, and compiler diagnostics appropriate to the repository.",
        "key": "scan",
    },
}


README = """# Thule

AI-agent skills for programmers, organized by programming language and AI coding tool.

Languages:

- Java
- Scala
- Go
- TypeScript
- Python
- Rust

Tools:

- Claude
- Codex
- Kiro
- Cursor

Each language/tool pair contains four Agent Skill packages:

- `<language>-best-practices`
- `<language>-lint`
- `<language>-security`
- `<language>-static-scan`

The skill content is intentionally grounded in official language, tool, and security-tool documentation. The skills do not install linters or scanners for a project; they tell the AI agent how to use the official or already-configured tools for that project.

## Install

Interactive:

```bash
./install.sh
```

Direct:

```bash
./install.sh --tool codex --lang go --scope personal
./install.sh --tool cursor --lang typescript --scope project --target /path/to/repo
./install.sh --tool all --lang all --scope project --target /path/to/repo
```

Useful flags:

- `--list`: show supported tools and languages
- `--dry-run`: show what would be copied
- `--force`: replace an existing installed skill directory

## Install Paths

Personal installs:

- Claude: `~/.claude/skills`
- Codex: `${CODEX_HOME:-~/.codex}/skills`
- Kiro: `~/.kiro/skills`
- Cursor: `~/.cursor/skills`

Project installs:

- Claude: `<target>/.claude/skills`
- Codex: `<target>/.codex/skills`
- Kiro: `<target>/.kiro/skills`
- Cursor: `<target>/.cursor/skills`

## Refresh Generated Skills

The repository keeps the skill matrix generated from `scripts/generate_skills.py`.

```bash
python3 scripts/generate_skills.py
```
"""


INSTALL_SH = """#!/usr/bin/env bash
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
"""


def wrapped_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def source_list(items: list[tuple[str, str]]) -> str:
    return "\n".join(f"- [{name}]({url})" for name, url in items)


def skill_md(language: str, category: str, tool: str) -> str:
    data = LANGUAGES[language]
    cat = CATEGORIES[category]
    skill_name = f"{language}-{category}"
    description = (
        f"{data['display']} {cat['summary']} based on official language, tool, "
        f"and scanner documentation. Use when writing, reviewing, linting, securing, "
        f"or statically scanning {data['display']} code for {tool}."
    )

    body = f"""---
name: {skill_name}
description: {description}
---

# {data['display']} {cat['title']}

## Scope

Use for {data['display']} files and project metadata matching {data['globs']}.

{cat['focus']}

## Official Sources

{source_list(data['sources'])}

## Workflow

1. Detect the build tool, package manager, language version, and existing quality commands before changing code.
2. Prefer repository-provided scripts, wrappers, and configuration over introducing new tools.
3. Apply the smallest code change that satisfies the user request and the local conventions.
4. Run the relevant checks below when the toolchain is available.
5. Report commands run, important findings, unresolved risks, and skipped checks.

## Guidance

{wrapped_list(data[cat['key']])}
"""
    return body


def generate() -> None:
    for language in LANGUAGES:
        for tool in TOOLS:
            tool_dir = ROOT / language / tool
            tool_dir.mkdir(parents=True, exist_ok=True)
            for category in CATEGORIES:
                skill_name = f"{language}-{category}"
                skill_dir = tool_dir / skill_name
                skill_dir.mkdir(parents=True, exist_ok=True)
                (skill_dir / "SKILL.md").write_text(skill_md(language, category, tool), encoding="utf-8")

    (ROOT / "README.md").write_text(README, encoding="utf-8")
    install_path = ROOT / "install.sh"
    install_path.write_text(INSTALL_SH, encoding="utf-8")
    install_path.chmod(0o755)


def clean_generated() -> None:
    for language in LANGUAGES:
        lang_dir = ROOT / language
        if lang_dir.exists():
            shutil.rmtree(lang_dir)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true", help="remove generated language directories first")
    args = parser.parse_args()

    if args.clean:
        clean_generated()
    generate()


if __name__ == "__main__":
    main()
