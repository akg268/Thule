---
name: typescript-static-scan
description: TypeScript static analysis and scanner workflow guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning TypeScript code for codex.
---

# TypeScript Static Scan

## Scope

Use for TypeScript files and project metadata matching `**/*.ts`, `**/*.tsx`, `tsconfig*.json`, `eslint.config.*`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`.

Run static analyzers, type checkers, vulnerability scanners, and compiler diagnostics appropriate to the repository.

## Official Sources

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TSConfig strict option](https://www.typescriptlang.org/tsconfig/strict.html)
- [typescript-eslint Getting Started](https://typescript-eslint.io/getting-started/)
- [npm audit documentation](https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities/)

## Workflow

1. Detect the build tool, package manager, language version, and existing quality commands before changing code.
2. Prefer repository-provided scripts, wrappers, and configuration over introducing new tools.
3. Apply the smallest code change that satisfies the user request and the local conventions.
4. Run the relevant checks below when the toolchain is available.
5. Report commands run, important findings, unresolved risks, and skipped checks.

## Guidance

- Run `tsc --noEmit` for static type analysis.
- Run ESLint with the existing `eslint.config.*` or package script.
- Run `npm audit`, `pnpm audit`, or `yarn npm audit` according to the lockfile and package manager.
- Review lockfile-only changes carefully and avoid broad dependency upgrades without need.
- Report type errors, lint rules, vulnerable packages, severities, and fix versions separately.
