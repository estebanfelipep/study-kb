# Ingest on AWS

This file covers stage 1 of the data pipeline on AWS: the services that ingest each type of source into the data lake.

## Goal

Once the data lake is in place, use **specialized AWS services** to ingest different types of data into it.

## Services

| Service | What it ingests |
| --- | --- |
| [dms.md](../../aws-services/aws-databases/dms.md) | **Relational and non-relational databases** |
| [data-firehose.md](../../aws-services/aws-analytics/data-firehose.md) | **Real-time data streams**, with conversion to Parquet or ORC |
| [msk.md](../../aws-services/aws-analytics/msk.md) | **Real-time streaming** on Apache Kafka |
| [iot-core.md](../../aws-services/aws-iot/iot-core.md) | **IoT devices** |
| [datasync.md](../../aws-services/aws-migration-and-transfer/datasync.md) | **On-premises file shares, object storage and Hadoop clusters** |
| [transfer-family.md](../../aws-services/aws-migration-and-transfer/transfer-family.md) | **Files over SFTP, FTPS, FTP** (and AS2) into and out of S3 |
| [snow-family.md](../../aws-services/aws-migration-and-transfer/snow-family.md) | **Huge or sensitive data**, on physical devices |

[kinesis-data-streams.md](../../aws-services/aws-analytics/kinesis-data-streams.md) is the real-time stream these services and consumers often sit around.

## Related

- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): its "1. Ingest" section describes the kinds of source and how each is ingested; this file names the AWS service for each.
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): the ingest modes (batch, micro-batch, streaming) decide which of these services fits a source.
- [choosing-ingestion-services.md](../choosing-ingestion-services.md): the pick-rules and comparisons between these services, such as DMS vs DataSync and Firehose vs MSK.
- [store-on-aws.md](store-on-aws.md): the next stage; every service here writes into the S3 data lake described there.
