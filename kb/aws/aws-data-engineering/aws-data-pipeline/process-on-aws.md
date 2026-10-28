# Process on AWS

This file covers stage 4 of the data pipeline on AWS: the services that transform data in the lake.

## Services

| Service | Mode |
| --- | --- |
| [glue.md](../../aws-services/aws-analytics/glue.md): fully managed ETL | Batch (also streaming ETL) |
| [emr.md](../../aws-services/aws-analytics/emr.md): open-source big data frameworks | Batch |
| [managed-service-for-apache-flink.md](../../aws-services/aws-analytics/managed-service-for-apache-flink.md): real-time stream processing | Real time |

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
