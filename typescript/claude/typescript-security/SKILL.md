---
name: typescript-security
description: TypeScript secure coding guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning TypeScript code for claude.
---

# TypeScript Security

## Scope

Use for TypeScript files and project metadata matching `**/*.ts`, `**/*.tsx`, `tsconfig*.json`, `eslint.config.*`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`.

Review code for security risks, validate trust boundaries, and keep secrets and dependency risk visible.

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

- Validate untrusted data at runtime before trusting TypeScript types.
- Avoid unsafe DOM insertion, command execution, dynamic evaluation, and string-built SQL or shell commands.
- Keep secrets out of source, tests, logs, browser bundles, and checked-in env files.
- Use dependency audit tooling from the active package manager before changing lockfiles.
- Prefer least-privilege tokens, scoped permissions, and explicit error handling around security boundaries.
