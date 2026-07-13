---
name: scala-security
description: Scala secure coding guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Scala code for codex.
---

# Scala Security

## Scope

Use for Scala files and project metadata matching `**/*.scala`, `build.sbt`, `project/*.scala`, `.scalafmt.conf`, `.scalafix.conf`.

Review code for security risks, validate trust boundaries, and keep secrets and dependency risk visible.

## Official Sources

- [Scala Style Guide](https://docs.scala-lang.org/style/)
- [Scala Futures and Promises](https://docs.scala-lang.org/overviews/core/futures.html)
- [Scalafmt documentation](https://scalameta.org/scalafmt/)
- [Scalafix documentation](https://scalacenter.github.io/scalafix/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)

## Workflow

1. Detect the build tool, package manager, language version, and existing quality commands before changing code.
2. Prefer repository-provided scripts, wrappers, and configuration over introducing new tools.
3. Apply the smallest code change that satisfies the user request and the local conventions.
4. Run the relevant checks below when the toolchain is available.
5. Report commands run, important findings, unresolved risks, and skipped checks.

## Guidance

- Validate untrusted input at trust boundaries before parsing, interpolation, file access, or command execution.
- Avoid blocking on the global execution context; mark unavoidable blocking with `blocking` and prefer dedicated execution contexts.
- Keep secrets out of source, tests, logs, and generated examples.
- Handle failed futures and effects explicitly; do not discard errors with unsafe callbacks.
- Scan JVM dependencies for known vulnerable components when dependency metadata changes.
