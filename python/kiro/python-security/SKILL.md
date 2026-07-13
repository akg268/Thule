---
name: python-security
description: Python secure coding guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Python code for kiro.
---

# Python Security

## Scope

Use for Python files and project metadata matching `**/*.py`, `pyproject.toml`, `requirements*.txt`, `poetry.lock`, `uv.lock`, `Pipfile.lock`.

Review code for security risks, validate trust boundaries, and keep secrets and dependency risk visible.

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

- Review Python standard library modules with documented security considerations before using them on untrusted data.
- Avoid unsafe `pickle`, `eval`, shell invocation, temp-file races, XML parsing, and weak randomness.
- Use `secrets` instead of `random` for security-sensitive values.
- Keep secrets out of code, tests, logs, notebooks, and generated fixtures.
- Audit dependencies with `pip-audit` when dependency metadata changes.
