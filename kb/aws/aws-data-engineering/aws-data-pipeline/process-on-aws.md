# Process on AWS

This file covers stage 4 of the data pipeline on AWS: the services that transform data in the lake.

## Services

| Service | Use it for | Considerations |
| --- | --- | --- |
| [glue.md](../../aws-services/aws-analytics/glue.md) | Building and running ETL workflows: fully managed ETL | Batch (also streaming ETL). The main processing service |
| [emr.md](../../aws-services/aws-analytics/emr.md) | Big data processing with open-source frameworks | Batch. EMR on EC2 clusters, EMR Serverless or EMR on EKS clusters. For teams comfortable writing Apache Spark code |
| [athena.md](../../aws-services/aws-analytics/athena.md) | Impromptu log analysis, report generation, business intelligence | Serverless, which reduces costs. Good for basic transformations |
| [managed-service-for-apache-flink.md](../../aws-services/aws-analytics/managed-service-for-apache-flink.md) | Real-time stream processing | Real time |
| [eventbridge.md](../../aws-services/aws-application-coordination/eventbridge.md) with [step-functions.md](../../aws-services/aws-application-coordination/step-functions.md) | Building event-driven transform pipelines | Scheduling and orchestration |
| [mwaa.md](../../aws-services/aws-application-coordination/mwaa.md) | Orchestrating transform pipeline workflows | Scheduling and orchestration |

Glue appears across the whole flow: jobs for ingestion, crawlers and the Data Catalog, ETL, and workflows for automation. It's the central service of this training.

In the lake, processing is what moves data between zones, usually S3 to S3:

```
S3 raw/ ──Glue or EMR──► S3 cleaned/ ──Glue or EMR──► S3 curated/
           filter,                      join,
           standardize                  aggregate
```

## Related

- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): its "4. Process" section lists the types of transformation and kinds of engine; these services implement them.
- [data-lake-zones.md](../../../data-engineering/data-lake-zones.md): processing moves data from raw to cleaned to curated.
- [choosing-storage-and-processing-services.md](../choosing-storage-and-processing-services.md): compares Glue with EMR, EMR Serverless and Flink.
- [catalog-on-aws.md](catalog-on-aws.md): the previous stage; jobs read table definitions from the Data Catalog.
- [deliver-on-aws.md](deliver-on-aws.md): the next stage; consumers query the curated output.
- [example-corp-pipeline-on-aws.md](example-corp-pipeline-on-aws.md): section 4 is a worked example of this stage: two scheduled Glue jobs, raw to cleaned and cleaned to curated.
- [choosing-orchestration-services.md](../choosing-orchestration-services.md): how to choose between Step Functions, MWAA and Glue workflows to schedule and chain transform jobs.
