---
name: go-best-practices
description: Go best practices and idiomatic code guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Go code for claude.
---

# Go Best Practices

## Scope

Use for Go files and project metadata matching `**/*.go`, `go.mod`, `go.sum`.

Write and review maintainable, idiomatic code while preserving the repository's existing architecture and conventions.

## Official Sources

- [Effective Go](https://go.dev/doc/effective_go)
- [Go security documentation](https://go.dev/doc/security/)
- [go command documentation](https://pkg.go.dev/cmd/go)
- [govulncheck tutorial](https://go.dev/doc/tutorial/govulncheck)

## Workflow

1. Detect the build tool, package manager, language version, and existing quality commands before changing code.
2. Prefer repository-provided scripts, wrappers, and configuration over introducing new tools.
3. Apply the smallest code change that satisfies the user request and the local conventions.
4. Run the relevant checks below when the toolchain is available.
5. Report commands run, important findings, unresolved risks, and skipped checks.

## Guidance

- Let `gofmt` decide formatting; do not hand-align code in ways gofmt will undo.
- Use short, clear package names and avoid underscores or mixedCaps in package names.
- Return errors directly and keep the successful path easy to read.
- Prefer simple interfaces defined near consumers, especially one-method interfaces with conventional names.
- Use context-aware APIs for cancellation, timeouts, and request-scoped values.
