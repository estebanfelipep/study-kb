# AWS Database Migration Service (DMS)

AWS DMS: ingesting relational and non-relational databases into the data lake, by full load or change data capture.

## What it is

AWS DMS (Database Migration Service) ingests data from relational and non-relational databases and loads it into the data lake. It's the ingestion service for the "databases" data source (CRM, ERP, CMS applications).

## Characteristics

- Sources: relational and non-relational databases.
- Modes: **batch (full load)** or **ongoing replication with change data capture (CDC)**. _(added)_
- Latency: seconds to minutes for CDC. _(added)_
- Light transformation only: mappings and filters. _(added)_
- You configure tasks and replication instances. _(added)_
- Supports many database sources and many targets, so it covers migrations and source/target pairs that zero-ETL doesn't support. _(added)_
- Usual exam triggers: "migrate or replicate a database", "change data capture". _(added)_

## Example

- _(added)_ The app's database on [RDS](rds.md) is copied to S3 by DMS, so analysts query the copy in [Redshift](../aws-analytics/redshift.md) or [Athena](../aws-analytics/athena.md) without touching production.

## Related

- [rds.md](rds.md): RDS is the typical source DMS reads from. DMS copies the app's database to S3 by full load or CDC, so analytics never touches production.
- [s3.md](../aws-general-services/s3.md): DMS loads database data into the S3 data lake, where it lands next to every other source.
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): DMS covers two ingest modes defined here: batch (full load) and ongoing replication (change data capture).
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares DMS with DataSync (files, not databases) and with Aurora zero-ETL and Glue jobs. Zero-ETL needs no code but only supports specific pairs; DMS covers migrations and unsupported pairs; Glue handles heavy transformation.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline.md): DMS is the ingest-stage service for relational and non-relational databases.
