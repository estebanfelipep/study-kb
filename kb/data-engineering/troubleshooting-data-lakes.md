# Troubleshooting data lakes

This file covers how to troubleshoot a data lake: the systematic approach, and the vendor-neutral checks for the common transformation and performance issues.

## The approach

Troubleshooting a data lake means **identifying, diagnosing and resolving** problems systematically, wherever they happen: during **ingestion, storage, processing or analysis**. Knowing the lake's architecture and components well is what makes it fast, because the first job is to find which stage the problem is in.

```
  Symptom: a job fails, a query is slow, a bill is high,
           someone sees data they shouldn't
        │
        ▼
  1. Identify   which stage? ingest │ store │ process │ deliver
        │
        ▼
  2. Diagnose   logs, inputs, permissions, resource usage
        │
        ▼
  3. Resolve    fix the code, the data, the access or the sizing
```

## Transformation issues

| Issue | Checks |
| --- | --- |
| **Job failures** | Read the job's **logs** for error messages and stack traces. Verify the **script logic**, especially for data formats, schemas and transformations. Check the job has enough **memory and compute**, and add more if not. Check that **upstream jobs** it depends on finished successfully. Check that the **endpoint** it reads from or writes to, such as a relational database, is healthy |
| **Data format incompatibilities** | **Inspect the input**: its format, schema and sample records. Check the **transformation code** handles that format, including nested or complex structures. Check the job produces the **output format** the target expects |
| **Data quality issues** | Add **validation and cleansing** steps for missing values, inconsistent formats and corrupt records. **Measure data quality periodically**. Add **error handling** so the code copes with bad data gracefully |
| **Insufficient permissions** | Check the job's **identity** can read the input, write the output and call the services it needs. Check **resource policies**, such as bucket policies, aren't denying the job. Check any **fine-grained data permissions** on the locations and catalog |

Example of a format incompatibility:

| Expected by the job | What arrived | Result |
| --- | --- | --- |
| `amount` as a number | `"59,90"`, a string with a decimal comma | Cast fails, or the row becomes null |
| `address` as a flat string | `{"street": …, "city": …}`, a nested object | The job reads the wrong column, or fails |

## Performance issues

| Issue | Checks |
| --- | --- |
| **Slow processing** | Find bottlenecks in **ingestion**, and confirm the ingestion processes are working. **Optimize storage**: partitioning, compacting small files, columnar formats such as Parquet. Send real-time, high-velocity data to a **streaming service** instead of the lake. **Rightsize** the compute. **Optimize the code and queries**. Use the engine's **monitoring tools** to see the processing flow and bottlenecks |
| **Excessive resource use** | **Optimize storage**: compression, deduplication, lifecycle policies. **Rightsize** compute regularly against the actual workload, and use **auto scaling**. Use **serverless** services, so capacity follows the workload |
| **Governance and access control issues** | **Catalog** the data centrally, with granular access to data and metadata. **Mask or tokenize** sensitive data such as PII. Review roles and policies regularly for **least privilege** |

**Masking vs tokenization:** masking hides part or all of a value, such as `ana@…`, and can't be reversed. Tokenization replaces the value with a random token, such as `tok_8f3a`, and keeps the real value in a separate, secured store, so authorized systems can swap it back.

## Related

- [data-security-and-monitoring.md](data-security-and-monitoring.md): monitoring is how most of these issues are spotted, and masking and least privilege are among its security best practices.
- [partitioning.md](partitioning.md): partitioning is the first storage fix for slow queries.
- [open-table-formats.md](open-table-formats.md): compaction of small files is one of the features a table format adds.
- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): columnar formats such as Parquet are the other storage fix for slow queries.
- [apache-spark.md](apache-spark.md): most transformation jobs are Spark jobs, so rightsizing executors and reading the Spark UI are how slow jobs are diagnosed.
- [batch-and-streaming.md](batch-and-streaming.md): real-time, high-velocity data belongs in a stream, not in batch files in the lake.
- [modern-data-architecture.md](modern-data-architecture.md): the five stages are where step 1 of the approach looks for the problem.
- [troubleshooting-data-lakes-on-aws.md](../aws/aws-data-engineering/troubleshooting-data-lakes-on-aws.md): the AWS tools and settings for each check in this file.
