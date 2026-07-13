---
name: java-thread-dump-analysis
description: Java JVM thread dump capture and analysis guidance based on official language, tool, and diagnostic documentation. Use when diagnosing JVM thread behavior for claude.
---

# Java Thread Dump Analysis

## Scope

Use for Java files and project metadata matching `**/*.java`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle*`.

Capture and interpret JVM thread dumps for hangs, deadlocks, starvation, contention, blocked I/O, and thread pool behavior.

## Official Sources

- [Oracle jcmd command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jcmd.html)
- [Oracle jstack command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jstack.html)
- [Oracle Diagnostic Tools](https://docs.oracle.com/en/java/javase/26/troubleshoot/diagnostic-tools.html)

## Workflow

1. Identify the runtime, JVM version, process or container context, and symptom before collecting data.
2. Prefer repository-provided runbooks, scripts, JVM flags, and observability output before introducing new tools.
3. Choose the lowest-impact official diagnostic command that can answer the question.
4. Preserve commands, timestamps, sample intervals, tool versions, and evidence needed for reproducible analysis.
5. Report findings, confidence level, operational risk, and follow-up data that would reduce uncertainty.

## Guidance

- Prefer `jcmd <pid> Thread.print -l` for live JVM thread snapshots; use `jstack -l <pid>` only when it is the available project or runtime tool.
- Capture at least three dumps across short intervals before identifying a hang, starvation pattern, or transient blocker.
- Preserve timestamps, JVM version, process ID, host/container context, CPU state, and the command used to collect each dump.
- Group threads by state, stack shape, pool name, lock owner, monitor, parking point, and repeated top frames.
- Separate evidence for deadlock, lock contention, thread pool starvation, blocked I/O, GC pressure, and normal idle waiting.
