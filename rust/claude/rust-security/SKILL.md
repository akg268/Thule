---
name: rust-security
description: Rust secure coding guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Rust code for claude.
---

# Rust Security

## Scope

Use for Rust files and project metadata matching `**/*.rs`, `Cargo.toml`, `Cargo.lock`, `rustfmt.toml`, `clippy.toml`.

Review code for security risks, validate trust boundaries, and keep secrets and dependency risk visible.

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

- Treat `unsafe` as security-sensitive: document invariants and minimize scope.
- Avoid panics, unchecked indexing, path traversal, command injection, and secret leakage on untrusted inputs.
- Use constant-time and audited crypto crates where security properties matter.
- Audit dependencies with RustSec tooling when `Cargo.lock` changes.
- Review transitive dependency, license, and source policies when `cargo-deny` is configured.
