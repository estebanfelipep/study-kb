# Open table formats

This file covers open table formats: the problems a growing data lake runs into, how a table format adds database-like behavior on top of lake files, how it differs from a query engine, the three common formats, and what they add.

## Why a data lake needs them

A data lake is cheap, scalable and flexible storage, but it wasn't designed with database capabilities. As it grows, five problems appear:

| Problem | What goes wrong with plain files |
| --- | --- |
| Record-level updates and deletes | Changing one row as the business changes means rewriting whole files |
| Query performance at scale | Tables grow to millions of files and hundreds of thousands of partitions to list and plan over |
| Concurrent writers and readers | Several writers and readers at once can see or produce inconsistent data |
| Failed writes | A write that fails partway through leaves the table corrupted |
| Schema evolution | Changing a table's schema means rewriting all or part of the dataset |

## What an open table format is

An **open table format** is an open-source library that organizes a data lake's files into **tables**. It adds database-like functionality on top of the files, while they stay on cheap object storage. That cuts the work of optimizing and managing the lake. A lake whose tables use one is a **transactional data lake**.

```
  Engines (SQL, Spark, streaming)
            │  read and write through the table format
            ▼
  Table format: metadata files
    which data files make up the table,
    its schema, its snapshots
            │  points to
            ▼
  Data files, such as Parquet, in object storage
```

## Engine vs table format

A table format isn't a query engine, and doesn't replace one. They're different layers, used together:

- The **query engine** (SQL or Spark) runs the query.
- The **catalog** maps a table name to its location and schema.
- The **table format** decides how the files under that location behave as a table.

The same engine can query a plain table or a table-format table:

```
  Query engine (runs the SQL)
     │
     ▼
  Catalog (table name → location, schema)
     │
     ├──► Plain table: data files only
     │
     └──► Table-format table: metadata files + data files
```

What the table format changes for the engine:

| | Plain files | Open table format |
| --- | --- | --- |
| Read | Yes | Yes |
| Append new data | Yes, as new files | Yes |
| Update, delete or merge one row | No: rewrite the files or partition | Yes |
| Reader during a write | Can see a partial write | Sees the last committed snapshot |
| Write that fails partway | Leaves stray files in the table | Never committed, so the table is intact |
| Schema change | Can break reads of older files, or need a rewrite | Recorded in the metadata |
| Time travel | No | Yes |
| Finding the files of a huge table | List every path in storage | Read the metadata |

Plain files suit data that is only appended, such as logs and events. Once rows must be updated or deleted, as when CDC changes are applied to a current table, the table needs a table format.

## The three common formats

- **Apache Iceberg:** developed at Netflix, now an Apache project.
- **Apache Hudi**
- **Delta Lake**

All three solve the five problems above, with similar capabilities.

## What they add

| Feature | What it does |
| --- | --- |
| **Data compaction** | Merges many small files into fewer, larger ones, so a query opens fewer files |
| **Time travel** | Queries the table as it was at a past snapshot |
| **Fewer file listings** | The metadata files record which data files make up the table, so an engine reads the metadata instead of listing every file in storage |

## Related

- [athena.md](../aws/aws-services/aws-analytics/athena.md): Athena is an engine that reads both plain tables and Iceberg tables. On Iceberg tables it gains `UPDATE`, `DELETE`, `MERGE INTO` and time travel.
- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): a table format brings warehouse-like behavior (updates, deletes, consistent reads) to lake storage, and the data files underneath are still the columnar formats described there.
- [partitioning.md](partitioning.md): partitioning cuts the data a query scans. Once a table has hundreds of thousands of partitions, a table format's metadata also saves listing their files.
- [replicating-databases-to-the-lake.md](replicating-databases-to-the-lake.md): applies CDC changes to the cleaned table with a table format's `MERGE`, and keeps history with its time travel.
- [transactional-data-lake-on-aws.md](../aws/aws-data-engineering/transactional-data-lake-on-aws.md): how AWS implements a transactional data lake with Iceberg on S3, and which services create, ingest into and query the tables.
