# aws-databases — index

Operational and purpose-built databases, search, and database migration.

## How to read this folder

- **Before:** OLTP vs OLAP, in [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md).
- **Order:** From where data is created (RDS, DynamoDB), to how it leaves (DMS), to where some of it is served (OpenSearch).
- **After:** [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md).

## Files (in reading order)

- [rds.md](rds.md): Amazon RDS and Aurora as OLTP sources, why they aren't lakes, and Aurora zero-ETL integration with Redshift. Read when: you need RDS/Aurora's role in a pipeline or how Aurora data reaches Redshift without ETL.
- [dms.md](dms.md): AWS DMS: database ingestion by full load or CDC. Read when: you need to move or replicate a database into the lake.
- [dynamodb.md](dynamodb.md): Amazon DynamoDB: key-value and document model, capacity modes, DynamoDB Streams, TTL. Read when: you need DynamoDB's characteristics or its use as an event source or state store in pipelines.
- [opensearch-service.md](opensearch-service.md): Amazon OpenSearch Service: managed domains, OpenSearch Serverless collections (search, time series, vector search) and zero-ETL direct query on S3. Read when: you need full-text search, log analytics, vector search, or querying cold logs in S3 from OpenSearch.
