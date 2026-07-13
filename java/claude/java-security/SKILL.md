---
name: java-security
description: Java secure coding guidance based on official language, tool, and scanner documentation. Use when writing, reviewing, linting, securing, or statically scanning Java code for claude.
---

# Java Security

## Scope

Use for Java files and project metadata matching `**/*.java`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle*`.

Review code for security risks, validate trust boundaries, and keep secrets and dependency risk visible.

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

- Model trust boundaries and validate data crossing them before use.
- Restrict privileges and isolate untrusted code, users, data, services, and dependencies.
- Release resources in all paths with try-with-resources or clear acquire/release pairing.
- Avoid unsafe deserialization, reflection exposure, injection sinks, and unbounded resource consumption.
- Track third-party dependency updates and apply security fixes promptly.
