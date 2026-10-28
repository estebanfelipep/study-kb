# Data lakes and data warehouses

This file covers what a data lake is, how it differs from a data warehouse, OLTP vs OLAP, row vs columnar storage, columnar file formats, and the lake house.

## Data lake

A **data lake** is a **centralized repository** that stores **structured, semi-structured and unstructured** data **at scale**. Organizations use it to ingest, store and analyze diverse datasets **without extensive preprocessing**. The three data types are defined in [data-discovery.md](data-discovery.md).

A modern data architecture **starts with the data lake**: you need a place to put data before you can ingest it ([modern-data-architecture.md](modern-data-architecture.md)).

On AWS, the data lake is built on [s3.md](../aws/aws-services/aws-general-services/s3.md).

## Lake vs warehouse

**A lake is storage. A warehouse is a query engine with its own storage, built for analytics.** They usually work together.

|  | **Data lake** | **Data warehouse** |
| --- | --- | --- |
| What it is | Object storage | Managed, columnar SQL analytics database |
| Data it holds | Anything: structured, semi-structured, unstructured, raw files | Mostly structured, modeled tables |
| Schema | Applied when read (**schema-on-read**) | Defined before loading (**schema-on-write**) |
| Preprocessing | Minimal; store raw first | Cleaned and modeled before loading |
| Queries data itself? | No. Add a query engine | Yes. Tuned for fast, complex SQL at high concurrency |
| Typical contents | Raw and lightly processed data, everything kept in full | Curated, cleaned, frequently queried data |
| Cost | Very cheap per GB | More expensive (compute plus storage) |
| Typical users | Data engineers, data scientists | Analysts, BI dashboards |

**Rule of thumb:** raw data from every source lands in the **lake**. A processing engine transforms it, and the curated output stays in the lake. The hot, heavily queried subset goes into the **warehouse** for dashboards, or is queried in place.

### Lake house

A **lake house** combines the two: the lake holds everything, and the warehouse serves the curated, high-performance part. The warehouse can query files in the lake without loading them and export results back to the lake in open formats. The warehouse *reaches into* the lake but isn't the lake.

## OLTP vs OLAP

**An operational database runs the application (OLTP). A warehouse analyzes the data (OLAP).** The purpose drives the design.

|  | **OLTP** (online transaction processing) | **OLAP** (online analytical processing) |
| --- | --- | --- |
| Typical query | "Get order #123", "update this user's address" | "Total revenue by region by month for 3 years" |
| Query shape | Many small, fast reads and writes on a few rows | Few large scans and aggregations over millions or billions of rows |
| Storage layout | **Row-based**: one record is fast to fetch | **Columnar**: `SUM(revenue)` reads only that column, and data compresses well |
| Scale | GB to a few TB; scale up plus read replicas | TB to PB; work spread across nodes (**MPP**, massively parallel processing) |
| Concurrency | Thousands of small concurrent transactions | Fewer, heavier queries |
| Users | The application | Analysts, BI tools, dashboards |

**Why not run BI on the OLTP database:**

- Large analytical queries **compete with application traffic** and slow down the app.
- **Row storage is wasteful for aggregates.** Summing one column reads every full row.
- **A single node can't parallelize** a scan of billions of rows.

**How they fit together:** the OLTP database is usually a **source**. The app writes to it, a pipeline or replication copies the data to the lake and/or warehouse, and analysts query the warehouse without touching the production database.

## Why an operational database isn't a data lake

Every database stores data. A data lake is defined by **what** it stores, **how much**, and **in what state**: one central place for every source, any format, at any scale, with no preprocessing, paid per use. A per-application database fails most of those: it's one store per app (a silo by design), needs a schema first, and handles unstructured data only as blobs. If each team treated its own database as "our data lake", you'd recreate the silos and duplication the lake exists to fix.

The AWS version of this comparison (RDS vs S3) is in [choosing-storage-and-processing-services.md](../aws/aws-data-engineering/choosing-storage-and-processing-services.md).

## Columnar file formats

**Parquet and ORC** are **columnar** file formats. Converting lake data to them makes it cheaper and faster to query, because engines read only the columns a query needs. It's the same columnar idea warehouses use. Combined with **partitioning**, it cuts the data each query scans.
