---
name: rust-static-scan
description: Rust static analysis and scanner workflow guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Rust code for claude.
---

# Rust Static Scan

## Scope

Use for Rust files and project metadata matching `**/*.rs`, `Cargo.toml`, `Cargo.lock`, `rustfmt.toml`, `clippy.toml`.

Run static analyzers, type checkers, vulnerability scanners, and compiler diagnostics appropriate to the repository.

## Official Sources

- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [Clippy documentation](https://doc.rust-lang.org/clippy/)
- [rustfmt documentation](https://rust-lang.github.io/rustfmt/)
- [RustSec Advisory Database](https://rustsec.org/)

## Workflow

1. Detect the build tool, package manager, language version, and existing quality commands before changing code.
2. Prefer repository-provided scripts, wrappers, and configuration over introducing new tools.
3. Apply the smallest code change that satisfies the user request and the local conventions.
4. Run the relevant checks below when the toolchain is available.
5. Report commands run, important findings, unresolved risks, and skipped checks.

## Guidance

- Run `cargo check --all-targets --all-features` for static type and borrow checking.
- Run `cargo clippy --all-targets --all-features` for Rust lints.
- Run `cargo fmt --check` for formatting.
- Run `cargo audit` or `cargo deny check advisories` when configured for dependency vulnerability scanning.
- Report any `unsafe`, clippy warnings, advisory IDs, affected crates, and fix versions.
