# Partitioning

This file covers partitioning a lake table: splitting its files by the values of one or more columns, so that a query reads only the partitions it needs.

## How it works

- **Partition keys** are the columns the data is partitioned by, such as `year`, `month` and `day`.
- Each **partition** is one combination of key values, stored under its own path, in the form `key=value/`.
- A query that filters on the partition keys **reads only the matching paths and skips the rest**. Less data scanned means faster and cheaper queries.

```
 mytable/
 ├─ year=2024/month=3/day=13/   ◄─ WHERE day = 13 reads this
 └─ year=2024/month=3/day=14/      skipped
```

- The catalog records each table's partition keys and the location of every partition.
- Partitioning pairs with columnar formats: partitions cut the files a query reads, and columnar files cut the columns.
- This is a different sense from the partition key of a stream, which decides which shard a record goes to ([batch-and-streaming.md](batch-and-streaming.md)).

## Related

- [modern-data-architecture.md](modern-data-architecture.md): the catalog's "where is it?" metadata includes partitions.
- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): columnar formats cut the columns a query reads, as partitioning cuts the files.
- [batch-and-streaming.md](batch-and-streaming.md): uses "partition key" in its stream sense, the value that routes a record to a shard.
- [glue.md](../aws/aws-services/aws-analytics/glue.md): the Glue Data Catalog stores a table's partition keys and one partition per S3 path, and Glue crawlers detect the partition structure automatically.
- [s3.md](../aws/aws-services/aws-general-services/s3.md): on S3, a partition is only key text, such as `day=2026-10-27`, which engines read as a partition value.
- [athena.md](../aws/aws-services/aws-analytics/athena.md): Athena scans less, and costs less, when a query filters on partition keys.
