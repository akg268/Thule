---
name: java-jvm-memory-analysis
description: Java JVM heap, GC, native memory, and leak analysis guidance based on official language, tool, and diagnostic documentation. Use when diagnosing JVM memory behavior for cursor.
---

# Java JVM Memory Analysis

## Scope

Use for Java files and project metadata matching `**/*.java`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `settings.gradle*`.

Analyze JVM memory symptoms with heap, GC, class histogram, native memory, JFR, and leak investigation workflows.

## Official Sources

- [Oracle jcmd command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jcmd.html)
- [Oracle jmap command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jmap.html)
- [Oracle jstat command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jstat.html)
- [Oracle jfr command](https://docs.oracle.com/en/java/javase/26/docs/specs/man/jfr.html)
- [Oracle Diagnostic Tools](https://docs.oracle.com/en/java/javase/26/troubleshoot/diagnostic-tools.html)

## Workflow

1. Identify the runtime, JVM version, process or container context, and symptom before collecting data.
2. Prefer repository-provided runbooks, scripts, JVM flags, and observability output before introducing new tools.
3. Choose the lowest-impact official diagnostic command that can answer the question.
4. Preserve commands, timestamps, sample intervals, tool versions, and evidence needed for reproducible analysis.
5. Report findings, confidence level, operational risk, and follow-up data that would reduce uncertainty.

## Guidance

- Classify the symptom first: Java heap growth, allocation churn, GC pause pressure, metaspace, direct buffer, thread stack, code cache, or native memory.
- Start with lower-impact observations such as `jcmd <pid> GC.heap_info`, `jcmd <pid> GC.class_histogram`, `jstat -gcutil`, and existing metrics.
- Use `jcmd <pid> GC.heap_dump <file>` or `jmap -dump` only after noting heap-dump impact and data sensitivity.
- Use Native Memory Tracking data such as `jcmd <pid> VM.native_memory summary` only when NMT is enabled for the target JVM.
- Correlate heap histograms, GC logs, JFR events, and code paths before naming a leak or recommending tuning.
