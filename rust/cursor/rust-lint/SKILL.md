---
name: rust-lint
description: Rust linting and formatting guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Rust code for cursor.
---

# Rust Lint

## Scope

Use for Rust files and project metadata matching `**/*.rs`, `Cargo.toml`, `Cargo.lock`, `rustfmt.toml`, `clippy.toml`.

Find and fix lint or formatting issues using existing project tooling before adding anything new.

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

- Run `cargo fmt --check` when rustfmt is available.
- Run `cargo clippy --all-targets --all-features` or the repo's clippy command.
- Do not enable all `clippy::restriction`; choose restriction lints case by case.
- Run `cargo test` or the repo's test matrix before finalizing behavioral changes.
- Preserve existing `clippy.toml`, `rustfmt.toml`, and workspace policy.
