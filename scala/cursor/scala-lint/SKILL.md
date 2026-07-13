---
name: scala-lint
description: Scala linting and formatting guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Scala code for cursor.
---

# Scala Lint

## Scope

Use for Scala files and project metadata matching `**/*.scala`, `build.sbt`, `project/*.scala`, `.scalafmt.conf`, `.scalafix.conf`.

Find and fix lint or formatting issues using existing project tooling before adding anything new.

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

- Run `scalafmt --check` or the build-tool equivalent when `.scalafmt.conf` exists.
- Run `scalafix --check` or the sbt/CLI equivalent when `.scalafix.conf` exists.
- Use the repository's sbt, Maven, Gradle, or Mill lint/check tasks before inventing new commands.
- Treat compiler warnings as actionable; preserve existing warning policy.
- Do not reformat files outside the requested change unless the project task already does so.
