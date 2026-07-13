# Thule

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

Every language/tool pair contains four core Agent Skill packages:

- `<language>-best-practices`
- `<language>-lint`
- `<language>-security`
- `<language>-static-scan`

Java and Scala tool folders also include JVM diagnostic skills:

- `<language>-thread-dump-analysis`
- `<language>-jvm-memory-analysis`

The skill content is intentionally grounded in official language, tool, security, and diagnostics documentation. The skills do not install linters, scanners, or JVM diagnostic tools for a project; they tell the AI agent how to use the official or already-configured tools for that project.

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

- `--list`: show supported tools, languages, and skill categories
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
