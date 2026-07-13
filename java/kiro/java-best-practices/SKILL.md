---
name: java-best-practices
description: Java best practices and idiomatic code guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Java code for kiro.
---

# Java Best Practices

## Scope

Use for Java files and project metadata matching `**/*.java`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle*`.

Write and review maintainable, idiomatic code while preserving the repository's existing architecture and conventions.

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

- Prefer explicit, small APIs with private fields and cohesive classes.
- Follow established Java naming: classes in UpperCamelCase, methods and variables in lowerCamelCase, constants in uppercase words.
- Use packages, imports, declarations, comments, and whitespace consistently with the project style; do not churn unrelated formatting.
- Document public APIs and security-relevant preconditions with Javadoc.
- Use modern language features only when the configured source or release level supports them.
