---
name: python-lint
description: Python linting and formatting guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Python code for claude.
---

# Python Lint

## Scope

Use for Python files and project metadata matching `**/*.py`, `pyproject.toml`, `requirements*.txt`, `poetry.lock`, `uv.lock`, `Pipfile.lock`.

Find and fix lint or formatting issues using existing project tooling before adding anything new.

## Official Sources

- [PEP 8](https://peps.python.org/pep-0008/)
- [Python security considerations](https://docs.python.org/3/library/security_warnings.html)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Bandit documentation](https://bandit.readthedocs.io/en/latest/)
- [pip-audit](https://pypi.org/project/pip-audit/)

## Workflow

1. Detect the build tool, package manager, language version, and existing quality commands before changing code.
2. Prefer repository-provided scripts, wrappers, and configuration over introducing new tools.
3. Apply the smallest code change that satisfies the user request and the local conventions.
4. Run the relevant checks below when the toolchain is available.
5. Report commands run, important findings, unresolved risks, and skipped checks.

## Guidance

- Run `ruff check .` when Ruff is configured or already used.
- Run `ruff format --check .` or the project formatter check when present.
- Run the repo's test command, commonly `pytest`, `python -m pytest`, or configured task runners.
- Use `python -m compileall` for syntax checks when no richer project command exists.
- Do not add new lint tools where a project already standardizes on another tool.
