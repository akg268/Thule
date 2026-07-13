---
name: go-static-scan
description: Go static analysis and scanner workflow guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Go code for claude.
---

# Go Static Scan

## Scope

Use for Go files and project metadata matching `**/*.go`, `go.mod`, `go.sum`.

Run static analyzers, type checkers, vulnerability scanners, and compiler diagnostics appropriate to the repository.

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

- Run `go vet ./...` for static diagnostics.
- Run `go test ./...` to compile and test all packages with default vet coverage.
- Run `govulncheck ./...` for reachable vulnerability analysis.
- Use `go version -m` when inspecting built binaries for embedded module metadata.
- Report whether vulnerabilities are called by the code or only present in imported modules.
