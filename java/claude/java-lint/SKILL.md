---
name: java-lint
description: Java linting and formatting guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Java code for claude.
---

# Java Lint

## Scope

Use for Java files and project metadata matching `**/*.java`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle*`.

Find and fix lint or formatting issues using existing project tooling before adding anything new.

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

- Prefer the project formatter and build tasks when present.
- Run `javac -Xlint` or the build equivalent to surface compiler lint categories.
- Treat `-Werror` as a project decision; do not introduce it unless the repo already enforces warnings as errors.
- Use `javadoc -Xdoclint` when the change affects public API documentation.
- For Maven or Gradle projects, prefer existing `mvn test`, `mvn verify`, `gradle check`, or wrapper scripts.
