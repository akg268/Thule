---
name: scala-thread-dump-analysis
description: Scala JVM thread dump capture and analysis guidance based on official language, tool, and diagnostic documentation. Use when diagnosing JVM thread behavior for claude.
---

# Scala Thread Dump Analysis

## Scope

Use for Scala files and project metadata matching `**/*.scala`, `build.sbt`, `project/*.scala`, `.scalafmt.conf`, `.scalafix.conf`.

Capture and interpret JVM thread dumps for hangs, deadlocks, starvation, contention, blocked I/O, and thread pool behavior.

## Official Sources

- [Oracle jcmd command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jcmd.html)
- [Oracle jstack command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jstack.html)
- [Oracle Diagnostic Tools](https://docs.oracle.com/en/java/javase/26/troubleshoot/diagnostic-tools.html)
- [Scala Futures and Promises](https://docs.scala-lang.org/overviews/core/futures.html)

## Workflow

1. Identify the runtime, JVM version, process or container context, and symptom before collecting data.
2. Prefer repository-provided runbooks, scripts, JVM flags, and observability output before introducing new tools.
3. Choose the lowest-impact official diagnostic command that can answer the question.
4. Preserve commands, timestamps, sample intervals, tool versions, and evidence needed for reproducible analysis.
5. Report findings, confidence level, operational risk, and follow-up data that would reduce uncertainty.

## Guidance

- Prefer `jcmd <pid> Thread.print -l` for live JVM thread snapshots; use `jstack -l <pid>` only when it is the available project or runtime tool.
- Capture multiple dumps across intervals and compare repeated stacks before concluding a Scala service is hung.
- Separate normal `ExecutionContext`, `ForkJoinPool`, scheduler, and dispatcher idleness from starvation, blocking, or lock contention.
- Look for `Await.result`, unmanaged blocking, long-running work on shared execution contexts, and missing `blocking` hints around unavoidable blocking.
- Tie thread names and pools back to the Scala runtime, build tool, framework, or application configuration before recommending code or pool changes.
