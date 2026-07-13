---
name: go-security
description: Go secure coding guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Go code for kiro.
---

# Go Security

## Scope

Use for Go files and project metadata matching `**/*.go`, `go.mod`, `go.sum`.

Review code for security risks, validate trust boundaries, and keep secrets and dependency risk visible.

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

- Use `govulncheck ./...` to identify known vulnerabilities that are reachable from code paths.
- Validate external input before parsing, file operations, templates, SQL, shell commands, or network calls.
- Use `crypto/rand` or appropriate crypto packages for security-sensitive randomness.
- Propagate and handle errors; never ignore errors from security-relevant operations.
- Keep dependencies updated with minimal, reviewable `go.mod` and `go.sum` changes.
