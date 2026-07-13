---
name: java-static-scan
description: Java static analysis and scanner workflow guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Java code for cursor.
---

# Java Static Scan

## Scope

Use for Java files and project metadata matching `**/*.java`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle*`.

Run static analyzers, type checkers, vulnerability scanners, and compiler diagnostics appropriate to the repository.

## Official Sources

- [Oracle Code Conventions for the Java Programming Language](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html)
- [Oracle Secure Coding Guidelines for Java SE](https://www.oracle.com/java/technologies/javase/seccodeguide.html)
- [Oracle javac command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/javac.html)
- [Oracle jdeps command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jdeps.html)
- [Oracle jdeprscan command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jdeprscan.html)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)

## Workflow

1. Detect the build tool, package manager, language version, and existing quality commands before changing code.
2. Prefer repository-provided scripts, wrappers, and configuration over introducing new tools.
3. Apply the smallest code change that satisfies the user request and the local conventions.
4. Run the relevant checks below when the toolchain is available.
5. Report commands run, important findings, unresolved risks, and skipped checks.

## Guidance

- Run `jdeps` to inspect dependencies, module boundaries, and JDK internal API use.
- Run `jdeprscan` against built class directories or JARs to find Java SE deprecated API use.
- Run `javac -Xlint:all` through the project build when practical.
- Run OWASP Dependency-Check for Maven, Gradle, CLI, or CI dependency vulnerability scanning when configured.
- Report tool versions, command exits, and any warnings left unresolved.
