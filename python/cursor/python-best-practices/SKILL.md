---
name: python-best-practices
description: Python best practices and idiomatic code guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Python code for cursor.
---

# Python Best Practices

## Scope

Use for Python files and project metadata matching `**/*.py`, `pyproject.toml`, `requirements*.txt`, `poetry.lock`, `uv.lock`, `Pipfile.lock`.

Write and review maintainable, idiomatic code while preserving the repository's existing architecture and conventions.

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

- Follow PEP 8 unless the project has a stronger local style.
- Prefer readable, explicit code with clear names, small functions, and grouped imports.
- Use type hints where the project expects them; do not add typing churn to unrelated code.
- Use context managers for resources and avoid broad exception swallowing.
- Keep dependency metadata and lockfiles minimal and intentional.
