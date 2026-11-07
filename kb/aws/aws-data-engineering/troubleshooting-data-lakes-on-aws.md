# Troubleshooting data lakes on AWS

This file covers where to look and what to change on AWS for the common data lake issues, by issue. The vendor-neutral checks are in [troubleshooting-data-lakes.md](../../data-engineering/troubleshooting-data-lakes.md).

## Transformation issues

| Issue | On AWS |
| --- | --- |
| **Glue job failures** | Read the **Glue job logs** for errors and stack traces. Verify the **script**. Check the job's **workers** are enough, and add more if not. Check **upstream jobs** succeeded. Check the **endpoint**, such as an RDS database, is healthy |
| **Data format incompatibilities** | Inspect the input format, schema and sample records. Check the Glue script handles nested structures. Check the output format the target expects |
| **Data quality issues** | Add validation and cleansing steps in the job. Evaluate datasets periodically with [Glue Data Quality](../aws-services/aws-analytics/glue.md). Add error handling in the job code |
| **Insufficient permissions** | Three layers to check, in order (diagram below) |

**Insufficient permissions: check the three layers.** A job needs to pass all three:

```
  Glue job
     │
     ▼
  1. IAM role       can it read the input, write the
                    output, call the services it needs?
     │
     ▼
  2. Resource       does an S3 bucket policy deny it?
     policy         (an explicit deny always wins)
     │
     ▼
  3. Lake           is it granted the data locations
     Formation      and catalog tables it uses?
     │
     ▼
  Data in S3
```

- [iam.md](../aws-services/aws-identity/iam.md): the job's role.
- [s3.md](../aws-services/aws-general-services/s3.md): bucket policies.
- [lake-formation.md](../aws-services/aws-analytics/lake-formation.md): grants on data locations and catalog tables.

## Performance issues

| Issue | On AWS |
| --- | --- |
| **Slow processing** | Check ingestion: is [DMS](../aws-services/aws-databases/dms.md) or [DataSync](../aws-services/aws-migration-and-transfer/datasync.md) working? Optimize S3 storage: partitioning, compaction, Parquet. Send real-time, high-velocity data to [Kinesis](../aws-services/aws-analytics/kinesis-data-streams.md). Rightsize **Glue workers**, **EMR Serverless workers** or **EMR on EC2 instances**. Optimize code and queries. Read the **Spark UI** in Glue or EMR to see the processing flow and bottlenecks |
| **Excessive resource use** | Compression, deduplication and **S3 lifecycle policies**. Rightsize EMR clusters and Spark workers against actual use, with **Glue auto scaling**, **EMR managed scaling** or **Spark dynamic allocation**. Use serverless services: Glue, EMR Serverless, Athena |
| **Governance and access control issues** | Govern the Glue Data Catalog with [Lake Formation](../aws-services/aws-analytics/lake-formation.md), for granular access to data and metadata. Mask or tokenize PII, for example with Glue's Detect PII transform. Review IAM roles and policies for least privilege |

**The scaling options:**

| Option | Scales | How |
| --- | --- | --- |
| **Glue auto scaling** | A Glue job's workers | Adds and removes workers during a run, up to the maximum you set |
| **EMR managed scaling** | An EMR on EC2 cluster's instances | Resizes the cluster to the workload, within limits you set |
| **Spark dynamic allocation** | A Spark application's executors | Requests executors when tasks queue up and releases idle ones |

## Related

- [troubleshooting-data-lakes.md](../../data-engineering/troubleshooting-data-lakes.md): the vendor-neutral approach and checks that this file maps onto AWS.
- [glue.md](../aws-services/aws-analytics/glue.md): most transformation issues here are Glue job issues: logs, workers, auto scaling, Data Quality and the Spark UI.
- [emr.md](../aws-services/aws-analytics/emr.md): rightsizing EMR Serverless workers and EC2 instances, managed scaling, and the Spark UI.
- [iam.md](../aws-services/aws-identity/iam.md): the first permissions layer a failing job is checked against.
- [lake-formation.md](../aws-services/aws-analytics/lake-formation.md): the third permissions layer, and the governance fix for access control issues.
- [s3.md](../aws-services/aws-general-services/s3.md): bucket policies can deny a job, and storage fixes (partitioning, compaction, lifecycle policies) are applied in S3.
- [security-and-monitoring-on-aws.md](security-and-monitoring-on-aws.md): the monitoring services that surface these issues in the first place.
- [exam-traps.md](exam-traps.md): logs the two course statements this file words differently (Kinesis as a data store, Lake Formation creating the catalog).
