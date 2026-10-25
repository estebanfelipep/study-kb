# Replicating databases into the data lake

This file covers how an operational database gets into a data lake: a copy written as files, kept current by a full load plus change data capture, and merged into a current-state table.

All content here is _(added)_: general knowledge from Q&A, not the course notes.

## It's a copy

The operational database stays where it is and keeps running its app. **A copy of its tables is written to the lake as files.** The lake never contains the live database, only files that represent its tables. Reasons to copy rather than query the database directly are in [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): analytical queries would compete with the app, row storage is slow for aggregates, and in the lake the data sits next to every other source.

Important concept: 
- **CDC (change data capture):** It's a way of copying a database by sending only its changes: each insert, update and delete as it happens, instead of reloading every table each time.

## Full load, then CDC

**1. Full load: a snapshot of every table.** Each table is written as files, one folder per table:

```
lake/raw/sales-crm/
  customers/
    LOAD00000001.parquet     ← every customer row, as of today
  orders/
    LOAD00000001.parquet
    LOAD00000002.parquet
```

**2. Change data capture (CDC): then only the changes, continuously.** The tool reads the database's change log and writes new files that hold only what changed. A column marks what kind of change each row is:

```
  customers/
    2026/10/25/20261025-104200.parquet

  Op | customer_id | city   | updated_at
  U  | S-981       | Lisbon | 2026-10-25 10:42
  I  | S-982       | Porto  | 2026-10-25 10:43
  D  | S-120       | ...    | 2026-10-25 10:44
```

`I` is insert, `U` is update and `D` is delete. Writing the files as Parquet makes them columnar, which is cheaper to query later.

## Files can't be updated in place

Lake files are written once. The raw folder is a **pile of files**: the full load plus a growing list of changes. It isn't yet a "current customers" table, and a naive query would show a changed customer twice, once per version.

The process stage turns the pile into a current table:

```
raw/sales-crm/customers/     ← full load + change files
        │  job: apply I/U/D, keep latest row per key
        ▼
curated/customers/           ← one row per customer, current state
```

There are two common ways to do it:

- **Rebuild:** a job periodically rewrites the curated table from the full load plus all the changes. It's simple, but slow for big tables.
- **Merge with an open table format:** store the curated table in a format such as **Apache Iceberg**, which adds `MERGE`, `UPDATE` and `DELETE` on top of lake files. Each batch of changes is applied directly. This is the modern approach.

## Other ways to get database data out

| Way | What happens | When to use it |
| --- | --- | --- |
| **Full load + CDC** (above) | Copy once, then changes continuously | The lake must stay close to current |
| **Scheduled snapshot job** | A job queries the tables over a database connection and writes a snapshot to the lake | Daily snapshots are enough |
| **Database snapshot export** | A backup snapshot is exported to the lake as files | Occasional bulk copies, with no load on the live database |
| **Direct replication to a warehouse** | Changes go straight to the warehouse, not the lake | The goal is warehouse analytics with the least effort |
| **Federated query** | Another engine reads the database **in place**, with **no copy** | Occasional queries only. It loads production, and it isn't a lake |

## Related

- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): explains why the database is copied: an OLTP database isn't a lake, and analytics on it competes with the app. This file shows how the copy gets made.
- [batch-and-streaming.md](batch-and-streaming.md): the full load is a batch ingest, and CDC is ongoing replication close to streaming.
- [modern-data-architecture.md](modern-data-architecture.md): replication is how the databases row of the ingest stage works. The raw files land in the store stage, and the merge into a current table is a process-stage job.
- [unified-customer-data.md](unified-customer-data.md): step 2 of that example is this replication, applied to the sales CRM.
- [dms.md](../aws/aws-services/aws-databases/dms.md): DMS implements full load + CDC on AWS and writes the change files to S3 with the `Op` column.
- [choosing-ingestion-services.md](../aws/aws-data-engineering/choosing-ingestion-services.md): maps each way to get RDS data out onto an AWS service.
