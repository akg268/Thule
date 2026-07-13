---
name: typescript-lint
description: TypeScript linting and formatting guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning TypeScript code for cursor.
---

# TypeScript Lint

## Scope

Use for TypeScript files and project metadata matching `**/*.ts`, `**/*.tsx`, `tsconfig*.json`, `eslint.config.*`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`.

Find and fix lint or formatting issues using existing project tooling before adding anything new.

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

- Run `tsc --noEmit` or the repo's typecheck script.
- Run ESLint through the repo script, usually `npm run lint`, `pnpm lint`, or `yarn lint`.
- Use `typescript-eslint` recommended or type-aware linting only when the repo is configured for it.
- Do not introduce Prettier, ESLint, or config migrations unless the task requests it.
- Keep generated files, build outputs, and vendored code out of lint fixes.
