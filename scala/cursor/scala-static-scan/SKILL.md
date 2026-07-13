---
name: scala-static-scan
description: Scala static analysis and scanner workflow guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Scala code for cursor.
---

# Scala Static Scan

## Scope

Use for Scala files and project metadata matching `**/*.scala`, `build.sbt`, `project/*.scala`, `.scalafmt.conf`, `.scalafix.conf`.

Run static analyzers, type checkers, vulnerability scanners, and compiler diagnostics appropriate to the repository.

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

- Run `scalafix --check` for configured semantic or syntactic rules.
- Run `scalafmt --check` for formatting drift.
- Run the repo's compiler check with warnings enabled, usually through `sbt Test/compile`, `sbt test`, `mill __.test`, or existing CI scripts.
- Run OWASP Dependency-Check through Maven, Gradle, CLI, or configured CI for dependency vulnerabilities.
- Summarize findings by source file, rule, severity, and whether a fix was applied.
