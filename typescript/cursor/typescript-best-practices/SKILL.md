---
name: typescript-best-practices
description: TypeScript best practices and idiomatic code guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning TypeScript code for cursor.
---

# TypeScript Best Practices

## Scope

Use for TypeScript files and project metadata matching `**/*.ts`, `**/*.tsx`, `tsconfig*.json`, `eslint.config.*`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`.

Write and review maintainable, idiomatic code while preserving the repository's existing architecture and conventions.

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

- Prefer precise types, narrowing, discriminated unions, and explicit public API boundaries.
- Keep `strict` enabled when already configured; do not weaken strictness to silence errors.
- Avoid `any`, non-null assertions, broad type assertions, and suppressed errors unless the risk is documented.
- Respect the repo's module system, runtime target, JSX mode, and package manager.
- Separate validation of untrusted runtime data from compile-time TypeScript types.
