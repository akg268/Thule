---
name: python-static-scan
description: Python static analysis and scanner workflow guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Python code for cursor.
---

# Python Static Scan

## Scope

Use for Python files and project metadata matching `**/*.py`, `pyproject.toml`, `requirements*.txt`, `poetry.lock`, `uv.lock`, `Pipfile.lock`.

Run static analyzers, type checkers, vulnerability scanners, and compiler diagnostics appropriate to the repository.

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

- Run `ruff check .` for lint and static diagnostics.
- Run `bandit -r .` for common Python security issue scanning when Bandit is available.
- Run `pip-audit` against the project or requirements files for known vulnerable dependencies.
- Run `python -m compileall` when syntax coverage is needed without importing application code.
- Report findings with file, rule ID, severity, confidence, and whether auto-fix was used.
