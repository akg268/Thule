---
name: rust-best-practices
description: Rust best practices and idiomatic code guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Rust code for kiro.
---

# Rust Best Practices

## Scope

Use for Rust files and project metadata matching `**/*.rs`, `Cargo.toml`, `Cargo.lock`, `rustfmt.toml`, `clippy.toml`.

Write and review maintainable, idiomatic code while preserving the repository's existing architecture and conventions.

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

- Follow Rust API Guidelines for naming, interoperability, documentation, predictability, and type safety.
- Prefer safe Rust and isolate unavoidable `unsafe` behind small, documented invariants.
- Use ownership, borrowing, `Result`, and `Option` deliberately instead of panics in library code.
- Keep public APIs future-proof and avoid exposing unnecessary concrete implementation details.
- Use feature flags and dependency choices conservatively.
