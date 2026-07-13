---
name: scala-jvm-memory-analysis
description: Scala JVM heap, GC, native memory, and leak analysis guidance based on official language, tool, and diagnostic documentation. Use when diagnosing JVM memory behavior for cursor.
---

# Scala JVM Memory Analysis

## Scope

Use for Scala files and project metadata matching `**/*.scala`, `build.sbt`, `project/*.scala`, `.scalafmt.conf`, `.scalafix.conf`.

Analyze JVM memory symptoms with heap, GC, class histogram, native memory, JFR, and leak investigation workflows.

## Official Sources

- [Oracle jcmd command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jcmd.html)
- [Oracle jmap command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jmap.html)
- [Oracle jstat command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jstat.html)
- [Oracle jfr command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jfr.html)
- [Oracle Diagnostic Tools](https://docs.oracle.com/en/java/javase/26/troubleshoot/diagnostic-tools.html)
- [Scala Futures and Promises](https://docs.scala-lang.org/overviews/core/futures.html)

## Workflow

1. Identify the runtime, JVM version, process or container context, and symptom before collecting data.
2. Prefer repository-provided runbooks, scripts, JVM flags, and observability output before introducing new tools.
3. Choose the lowest-impact official diagnostic command that can answer the question.
4. Preserve commands, timestamps, sample intervals, tool versions, and evidence needed for reproducible analysis.
5. Report findings, confidence level, operational risk, and follow-up data that would reduce uncertainty.

## Guidance

- Classify JVM memory symptoms before selecting tools: heap retention, allocation churn, GC pressure, metaspace, direct buffers, thread stacks, or native memory.
- Start with low-impact JDK observations such as `jcmd <pid> GC.heap_info`, `jcmd <pid> GC.class_histogram`, `jstat -gcutil`, and existing metrics.
- Treat heap dumps as sensitive and potentially disruptive; collect them only with an explicit reason and enough context to interpret them.
- Inspect Scala-specific retention patterns such as captured closures, long-lived `Future` or `Promise` chains, cached collections, lazy vals, and effect runtimes.
- Correlate heap histograms, GC behavior, JFR events, and code ownership before calling a retention path a leak.
