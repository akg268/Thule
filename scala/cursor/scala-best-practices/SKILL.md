---
name: scala-best-practices
description: Scala best practices and idiomatic code guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Scala code for cursor.
---

# Scala Best Practices

## Scope

Use for Scala files and project metadata matching `**/*.scala`, `build.sbt`, `project/*.scala`, `.scalafmt.conf`, `.scalafix.conf`.

Write and review maintainable, idiomatic code while preserving the repository's existing architecture and conventions.

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

- Follow the local Scala version and style before introducing syntax or idioms from another version.
- Use clear names, small expressions, and explicit public API types where inference would hide intent.
- Keep effects, blocking, and concurrency boundaries visible.
- Avoid unnecessary symbolic methods, structural types, and clever implicit or given resolution.
- Prefer standard library and project-established abstractions over new helper layers.
