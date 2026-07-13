---
name: go-lint
description: Go linting and formatting guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Go code for cursor.
---

# Go Lint

## Scope

Use for Go files and project metadata matching `**/*.go`, `go.mod`, `go.sum`.

Find and fix lint or formatting issues using existing project tooling before adding anything new.

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

- Run `gofmt` or `go fmt ./...` for formatting.
- Run `go vet ./...` for likely mistakes and high-confidence diagnostics.
- Run `go test ./...` because it also runs a curated subset of vet checks by default.
- Preserve module compatibility and avoid unnecessary `go mod tidy` churn.
- Use existing `make`, `just`, or CI lint targets when present.
