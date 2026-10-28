# Catalog on AWS

This file covers stage 3 of the data pipeline on AWS: how data in the lake becomes findable and queryable.

## Services

- [Glue Data Catalog](../../aws-services/aws-analytics/glue.md) creates a **catalog of metadata** about stored assets, searchable by **name, owner, business terms** and other attributes.
- [Glue crawlers](../../aws-services/aws-analytics/glue.md) scan data, determine format and schema, group data into tables and write metadata to the Data Catalog.
- The business glossary lives in [datazone.md](../../aws-services/aws-analytics/datazone.md).

```
data lands in S3 ─► crawlers catalog it ─► discoverable and queryable
```

## Related

- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): its "3. Catalog" section explains metadata, crawlers and the data swamp; the Glue Data Catalog is the AWS implementation.
- [choosing-security-and-monitoring-services.md](../choosing-security-and-monitoring-services.md): compares the Glue Data Catalog (technical metadata) with DataZone (business metadata).
- [store-on-aws.md](store-on-aws.md): the previous stage; crawlers scan what lands in S3.
- [process-on-aws.md](process-on-aws.md): the next stage; processing engines read and write tables registered here.
