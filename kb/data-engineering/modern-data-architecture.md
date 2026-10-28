# Modern data architecture

This file covers why modern data architectures exist (data silos), and the five stages data flows through, each in its own section: ingest, store, catalog, process and deliver, plus the security and governance that spans them.

## The problem: teams building in isolation

Teams often build data solutions on their own, each with its **own ingestion, storage, management and governance layers**. This:

- **Delays** data-driven decisions.
- **Raises the cost** of data-driven decisions.
- **Blocks deeper insights** that only come from analyzing all relevant data together.

### Data silos

**Data silos** are **isolated and incompatible data stores** that are **optimized for departmental or individual use cases**. They:

- Make it hard to build a **unified view** of the organization's data.
- **Inhibit data sharing.**
- **Prevent using data for new insights.**

Silos usually aren't anyone's mistake. Each team picks the best store for its own job, such as the database behind one app or a spreadsheet in finance. The problem appears when you need to combine them. Typical signs:

| Sign | Example |
| --- | --- |
| **Isolated** | Marketing's customer list and sales' CRM can't see each other |
| **Incompatible** | Different formats, schemas or IDs for the same customer |
| **Duplicated** | Each team keeps its own copy, and the copies drift apart |
| **Inconsistently governed** | Each store has its own access rules, so nobody can answer "who can see PII?" |

## The solution: a modern data architecture

A modern data architecture for analytics and insights:

- **Breaks down all data silos**, including **third-party data**.
- Creates **end-to-end governance**.
- **Puts data in the hands of everyone** in the organization (democratization).

How the stages fix silos: the data lake gives every source one place to land, the catalog makes it findable, and governance tools control it end to end.

### Modern data strategy

A modern data strategy uses **technology building blocks** to help you:

| Verb | What it means |
| --- | --- |
| **Manage** | Store, catalog and govern data |
| **Access** | Let the right people find and reach it |
| **Analyze** | Query, report and model it |
| **Act** | Turn insights into decisions and actions |

## The five stages

```
Sources (databases, files, logs, IoT, SaaS, streams)
   │
   ▼
1. Ingest ─▶ 2. Store ─▶ 3. Catalog ─▶ 4. Process ─▶ 5. Deliver
             (data lake)                                 │
                                                         ▼
          Consumers (analysts, scientists, business users, apps)

Across every stage: security and governance
```

**Order note.** Data *flows* ingest → store. But you **build** the data lake first: "Before you can ingest data, you need a place to put it." Processed data is usually written back to the lake, so storage is used again after stage 4.

The AWS services for each stage are in [aws-data-pipeline.md](../aws/aws-data-engineering/aws-data-pipeline/aws-data-pipeline.md).

### How the stages map to the role

| Stage | Data engineer function ([data-engineer-role.md](data-engineer-role.md)) | Discovery step ([data-discovery.md](data-discovery.md)) | ETL |
| --- | --- | --- | --- |
| 1. Ingest | 2. Ingest | 3. Data sources | Extract |
| 2. Store | 1. Infrastructure | 4. Storage needs | Load |
| 3. Catalog | 4. Catalog | 4. Catalog needs | — |
| 4. Process | 3. Prepare | 5. Processing | Transform |
| 5. Deliver | — (serve to stakeholders) | 2. Data consumers | Serve |
| Security and governance | 5. Automate, 6. Quality and security | 4. Governance, compliance | — |

## 1. Ingest

**Goal:** once the data lake is in place, use **specialized tools** to bring each type of data into it. Each kind of source needs its own approach.

The sources are the ones classified in discovery step 3 ([data-discovery.md](data-discovery.md)). Their ingest modes (batch, micro-batch, streaming) are defined in [batch-and-streaming.md](batch-and-streaming.md).

| Kind of source | How it's ingested |
| --- | --- |
| **Relational and non-relational databases** | Loaded into the lake, as a full load or ongoing **change data capture** (CDC: copy only the inserts, updates and deletes) |
| **Real-time data streams** (logs, clickstreams, app events) | Delivered continuously into the lake. Delivery can **convert streams to columnar formats** such as Parquet or ORC, decompress data and run custom transformations on the way in |
| **High-throughput event streams** | Run on an event-streaming platform such as **Apache Kafka**, for streaming pipelines and applications |
| **IoT devices** | A device platform connects **billions of devices** and routes **trillions of messages** onward, often into a stream that delivers to the lake |
| **On-premises file shares, object storage and Hadoop clusters** | Transferred to cloud storage over the network, and can **sync on a schedule** |
| **Files from partners and vendors** | Sent over file transfer protocols (**SFTP, FTPS, FTP**, and AS2), with transfers into and out of the lake automated |
| **Huge or sensitive data** | Shipped on **physical devices** when network transfer isn't feasible because of volume or sensitivity |

- **Light transformation can happen during ingest,** such as format conversion. Heavier logic belongs in stage 4.
- **Converting to a columnar format on the way in pays off at delivery:** query engines scan less data, so queries are cheaper and faster ([data-lakes-and-warehouses.md](data-lakes-and-warehouses.md)).

## 2. Store

The store stage is the **data lake**: one central place where every source lands, in any format, at any scale, without extensive preprocessing. Its definition, and how it differs from a warehouse and from an operational database, are in [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md).

The storage under a data lake needs:

| Property | What it gives you |
| --- | --- |
| **Virtually unlimited scalability** | Grow from gigabytes to petabytes **seamlessly and without disruption** |
| **High durability** | Data is safe once it lands |
| **Pay for what you use** | No capacity to provision up front |

- **The lake holds both raw and processed data.** Raw data lands first, and stage 4 writes its curated output back to the lake.
- **The lake is split into zones:** raw (as ingested), cleaned (filtered, standardized, corrected) and curated (merged and consumption-ready), plus optional landing, logs, archived and sandbox zones. Stage 4 moves data from one zone to the next. See [data-lake-zones.md](data-lake-zones.md).
- **Not lakes, but often mistaken for them:** query and processing engines *read* the lake, a warehouse serves the curated part of it (a lake house), and an operational database is a *source* that feeds it.

## 3. Catalog

The **data catalog** is an **essential component** of a data lake. Cataloging lets an organization keep track of its data assets and understand:

| Question | Example metadata |
| --- | --- |
| **What** data exists? | Table names, descriptions, schemas (columns and types) |
| **Where** is it? | Storage location, format (CSV, JSON, Parquet), partitions |
| What's its **quality**? | Quality scores, freshness, row counts |
| **How** is it used? | Owners, consumers, which jobs read and write it |

A data catalog is designed to be the **single source of truth about the contents of the data lake**. People **search it to find relevant data** by attributes such as **name, owner and business terms**.

**Crawlers** fill the catalog. A crawler **scans data, determines its format and schema, groups it into tables and writes the metadata to the catalog**. Flow: data lands in the lake → a crawler catalogs it → it becomes discoverable and queryable.

- Without a catalog, a lake is just millions of files that nobody can find or trust. This is sometimes called a **data swamp**.
- **The catalog stores metadata, not the data itself.** The data stays in the lake; the catalog holds the table definitions that point to it.
- **One catalog, many engines:** define a table once and query it from any engine that reads the catalog. The **Apache Hive metastore** is the common standard engines expect.
- **The catalog anchors governance:** access permissions are granted on catalog objects (databases, tables, columns), so they apply to every engine that reads through it.
- **Technical vs business metadata:** a technical catalog holds schemas, locations and partitions for engines; a business catalog adds a **business glossary**, owners and descriptions for people across the organization.

## 4. Process

After data is **cataloged**, it's **processed or transformed** into formats more useful for analysis and insights. This is the **T** in ETL ("make it useful").

### Types of transformation

| Transformation | Example |
| --- | --- |
| **Data type conversion** | `"2026-10-18"` string → date; `"42"` → integer |
| **Filtering** | Drop test accounts, null rows or irrelevant columns |
| **Aggregation** | Raw orders → daily revenue per region |
| **Standardization** | `US`, `U.S.A.`, `United States` → `US`; consistent units and time zones |
| **Normalizing** | Split repeated data into related tables, or scale values to a common range |

### Kinds of processing engine

| Kind | What it does | Mode |
| --- | --- | --- |
| **Managed ETL** | Prepares and cleanses data from various sources. Can also **classify data, extract schemas and populate the catalog** | Batch (some also run streaming ETL) |
| **Big data frameworks** | Runs **open-source frameworks** on clusters you customize, or serverless | Batch |
| **Real-time stream processing** | Lets you **quickly author SQL** for **filtering, aggregating, joining and deriving** data as it streams in | Real time |

- **Apache Spark** is the open-source distributed engine most managed ETL and big data services run on. **Apache Flink** is the common open-source engine for real-time stream processing, and supports Java, Scala and Python as well as SQL.
- **Managed vs framework, in one line:** managed ETL is less to run and more opinionated. Running frameworks yourself gives more control and more framework choice, but more to manage.
- **A visual editor** for building ETL jobs answers discovery step 5's "Do you have a visual editor?"

## 5. Deliver

**Transformed data is delivered to consumers and stakeholders**, such as data scientists, data analysts and business analysts ([data-personas.md](data-personas.md)).

The **primary purpose of data analytics** is to **extract insights from data that lead to good business or organizational outcomes**. Data can be delivered in several ways:

| Way to deliver | What it does | Typical consumer |
| --- | --- | --- |
| **Data warehouse** | Analyzes **large sets of structured data** across many databases and datasets **without moving the data** | Analysts, BI |
| **SQL directly on the lake** | Queries large datasets **in place** with **standard SQL**, in formats such as **CSV, Parquet and ORC** | Analysts, engineers (ad hoc) |
| **Big data frameworks** | Runs **Spark, Hive, Presto and Flink** on large datasets. Examples: log analysis, ML, data science, web indexing, scientific simulations | Data scientists, engineers |
| **Purpose-built databases** | Store, query and analyze large datasets with the data model that fits (table below) | Applications, specialized analytics |
| **Search and log analytics** | Searches and analyzes data from streams, the lake and databases (full-text search, log analytics, near real-time log dashboards) | Engineers, ops |
| **BI dashboards** | **Visualize and analyze** with SQL, charts, graphs and **dashboards** | Business analysts, executives |
| **Machine learning** | Build, train and deploy models for **predictive analytics, computer vision, NLP, recommendation systems** and more | Data scientists |

A warehouse works "without moving the data" in two ways. It queries files in the lake in place, which is the lake house idea from [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md). It also queries operational databases through **federated queries**.

### Purpose-built databases

| Type | Use it for |
| --- | --- |
| Relational | Transactions, structured app data |
| Key-value | Massive scale, single-digit-millisecond lookups |
| Document | JSON documents |
| In-memory | Caching, microsecond reads |
| Graph | Relationships: social networks, fraud rings, recommendations |
| Time series | IoT and metrics data over time |
| Wide column | Large, sparse tables, such as Apache Cassandra workloads |
| Ledger | Immutable, verifiable history |

### How earlier stages pay off here

- **Ingest:** columnar formats written at ingest mean less data scanned per query.
- **Catalog:** every delivery engine reads the same table definitions from the catalog, so a table is defined once.

## Security and governance across stages

The **entire data analytics system depends on data being secured** and accessible only by authorized users. Security vs governance and the CIA triad are in [data-security-and-monitoring.md](data-security-and-monitoring.md).

## Related

- [aws-data-pipeline.md](../aws/aws-data-engineering/aws-data-pipeline/aws-data-pipeline.md): implements each of the five stages with AWS services, from DMS and Firehose at ingest to Redshift, Athena and QuickSight at deliver, and maps each purpose-built database type to its AWS service.
- [data-lake-zones.md](data-lake-zones.md): stage 2 (store) is organized into raw, cleaned and curated zones, and stage 4 (process) moves data between them.
- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): stage 2 (store) is the data lake. That file defines the lake, how it differs from a warehouse (schema-on-read vs schema-on-write), why an operational database isn't one, and how the stage 5 warehouse works with it as a lake house.
- [batch-and-streaming.md](batch-and-streaming.md): stage 1 (ingest) works differently per ingest mode. Batch loads land files in the lake on a schedule, while streams deliver records continuously and can feed real-time processing in stage 4.
- [data-discovery.md](data-discovery.md): discovery plans the stages before they're built. Step 3 classifies the sources stage 1 ingests, step 4 sets the storage and catalog needs, and step 5 sets the processing requirements.
- [data-personas.md](data-personas.md): defines the consumers stage 5 delivers to. Scientists use big data frameworks and ML, and analysts use SQL, warehouses and dashboards.
- [orchestration-and-automation.md](orchestration-and-automation.md): orchestration chains the stages into one workflow (crawl, transform, load, notify, with retries), and automation runs each repetitive task in them. Zero-ETL removes some of the ingest and process steps altogether.
- [unified-customer-data.md](unified-customer-data.md): a worked example of these stages removing silos, from CDC on a sales CRM to one merged customer record that every department reads.
- [replicating-databases-to-the-lake.md](replicating-databases-to-the-lake.md): explains the databases row of the ingest stage in depth: full load + CDC into the lake, and the merge that turns change files into a current table.
