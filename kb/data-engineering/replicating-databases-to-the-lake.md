# Replicating databases into the data lake

This file covers how an operational database gets into a data lake: a copy written as files, kept current by a full load plus change data capture, merged into a current-state table, a three-table example of what lands in the lake, and the history the raw files keep.

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

## Example: three tables, from full load to current state

An online shop's database has three tables: `customers`, `orders` and `products`.

**Day 1, 09:00: the full load.** One `LOAD` file per table holds every row as it is now. These files are a **copy**, not a log.

```
lake/raw/shop/
  customers/LOAD00000001.parquet
  orders/LOAD00000001.parquet
  products/LOAD00000001.parquet
```

`customers/LOAD00000001.parquet`

| customer_id | name | city |
| --- | --- | --- |
| 981 | Ana | Madrid |
| 982 | Luis | Porto |

`orders/LOAD00000001.parquet`

| order_id | customer_id | product_id | qty | status |
| --- | --- | --- | --- | --- |
| 5001 | 981 | P-10 | 1 | shipped |

`products/LOAD00000001.parquet`

| product_id | name | price |
| --- | --- | --- |
| P-10 | Desk lamp | 39.00 |
| P-11 | Chair | 120.00 |

**Day 1, from 09:01: CDC.** The app keeps working. Ana moves to Lisbon (10:42), Luis places an order (10:43) and cancels it (10:50), and the chair is deleted (11:15). New files appear, only for the tables that changed. These files are a **log**: one row per change, in order, marked by `Op`.

```
lake/raw/shop/
  customers/LOAD00000001.parquet
  customers/20261027-104230.parquet    ← new
  orders/LOAD00000001.parquet
  orders/20261027-105000.parquet       ← new
  products/LOAD00000001.parquet
  products/20261027-111500.parquet     ← new
```

`customers/20261027-104230.parquet`

| Op | customer_id | name | city |
| --- | --- | --- | --- |
| U | 981 | Ana | Lisbon |

`orders/20261027-105000.parquet`

| Op | order_id | customer_id | product_id | qty | status |
| --- | --- | --- | --- | --- | --- |
| I | 5002 | 982 | P-10 | 2 | placed |
| U | 5002 | 982 | P-10 | 2 | cancelled |

`products/20261027-111500.parquet`

| Op | product_id | name | price |
| --- | --- | --- | --- |
| D | P-11 | Chair | 120.00 |

What the change files show:

- **An update carries the whole new row,** not only the changed field. Madrid is still in the `LOAD` file, so raw holds both versions of Ana.
- **The same row can appear several times.** Order 5002 is there as `I`, then as `U`. Nothing is combined.
- **A delete is a new row too.** `D` says the row is gone, while the `LOAD` file still has the chair.

So querying `raw/` as it is shows Ana twice and the chair as still on sale. The merge keeps the latest row per key and drops deleted rows, which gives the same state as the database right now:

`curated/customers`

| customer_id | name | city |
| --- | --- | --- |
| 981 | Ana | Lisbon |
| 982 | Luis | Porto |

`curated/orders`

| order_id | customer_id | product_id | qty | status |
| --- | --- | --- | --- | --- |
| 5001 | 981 | P-10 | 1 | shipped |
| 5002 | 982 | P-10 | 2 | cancelled |

`curated/products`

| product_id | name | price |
| --- | --- | --- |
| P-10 | Desk lamp | 39.00 |

**In one line:** `raw/` is a snapshot of each table plus every change since, the full history but not queryable as it is. `curated/` is one current row per key, like the database.

## History: what the raw zone keeps

The operational database usually keeps only the current state: when Ana moves, Madrid is overwritten. The raw zone keeps **every version since the full load**, so you can see that Ana lived in Madrid until 10:42, or rebuild any table as it was at a past moment by replaying the log up to that time. It's also what lets the curated table be rebuilt if a merge job had a bug.

Its limits:

- **History starts at the full load.** Changes made before replication began aren't there.
- **It lasts only as long as the files are kept.** Lifecycle rules that expire old raw files delete that history.
- **The curated table keeps only the current state** unless it's designed to keep history. Two common ways:
  - **Table snapshots ("time travel")** in an open table format such as Iceberg: query the table as of a past snapshot.
  - **A history table** with one row per version and `valid_from` / `valid_to` columns, so a query can ask "where did Ana live on day 1 at 10:00?". This is called a **slowly changing dimension, type 2** (SCD2).

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
