# Modern data architecture

This file covers why modern data architectures exist (data silos), the five stages data flows through, data catalogs, types of transformation, and security and governance across stages.

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

_(Added)_ Silos usually aren't anyone's mistake. Each team picks the best store for its own job, such as the database behind one app or a spreadsheet in finance. The problem appears when you need to combine them. Typical signs:

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

_(Added)_ How the stages fix silos: the data lake gives every source one place to land, the catalog makes it findable, and governance tools control it end to end.

### Modern data strategy

A modern data strategy uses **technology building blocks** to help you:

| Verb | What it means _(added)_ |
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

| Stage | What happens |
| --- | --- |
| **1. Ingest** | Specialized services bring each type of data into the lake |
| **2. Store** | A **data lake** holds structured, semi-structured and unstructured data at scale ([data-lakes-and-warehouses.md](data-lakes-and-warehouses.md)) |
| **3. Catalog** | Metadata makes the lake's contents findable and understandable |
| **4. Process** | Data is transformed into formats more useful for analysis (the **T** in ETL) |
| **5. Deliver** | Transformed data reaches consumers. The **primary purpose of data analytics** is to **extract insights from data that lead to good business or organizational outcomes** |

The AWS services for each stage are in [aws-data-pipeline.md](../aws/aws-data-engineering/aws-data-pipeline.md).

### How the stages map to the role _(added)_

| Stage | Data engineer function ([data-engineer-role.md](data-engineer-role.md)) | Discovery step ([data-discovery.md](data-discovery.md)) | ETL |
| --- | --- | --- | --- |
| 1. Ingest | 2. Ingest | 3. Data sources | Extract |
| 2. Store | 1. Infrastructure | 4. Storage needs | Load |
| 3. Catalog | 4. Catalog | 4. Catalog needs | — |
| 4. Process | 3. Prepare | 5. Processing | Transform |
| 5. Deliver | — (serve to stakeholders) | 2. Data consumers | Serve |
| Security and governance | 5. Automate, 6. Quality and security | 4. Governance, compliance | — |

## Data catalogs

The **data catalog** is an **essential component** of a data lake. Cataloging lets an organization keep track of its data assets and understand:

| Question | Example metadata _(added)_ |
| --- | --- |
| **What** data exists? | Table names, descriptions, schemas (columns and types) |
| **Where** is it? | Storage location, format (CSV, JSON, Parquet), partitions |
| What's its **quality**? | Quality scores, freshness, row counts |
| **How** is it used? | Owners, consumers, which jobs read and write it |

A data catalog is designed to be the **single source of truth about the contents of the data lake**.

- _(Added)_ Without a catalog, a lake is just millions of files that nobody can find or trust. This is sometimes called a **data swamp**.
- _(Added)_ **The catalog stores metadata, not the data itself.** The data stays in the lake; the catalog holds the table definitions that point to it.
- _(Added)_ **One catalog, many engines:** define a table once and query it from any engine that reads the catalog.
- _(Added)_ **Technical vs business metadata:** a technical catalog holds schemas, locations and partitions for engines; a business catalog adds a **business glossary**, owners and descriptions for people across the organization.

## Types of transformation

| Transformation | Example _(added)_ |
| --- | --- |
| **Data type conversion** | `"2026-10-18"` string → date; `"42"` → integer |
| **Filtering** | Drop test accounts, null rows or irrelevant columns |
| **Aggregation** | Raw orders → daily revenue per region |
| **Standardization** | `US`, `U.S.A.`, `United States` → `US`; consistent units and time zones |
| **Normalizing** | Split repeated data into related tables, or scale values to a common range |

## Security and governance across stages

The **entire data analytics system depends on data being secured** and accessible only by authorized users. Security vs governance and the CIA triad are in [data-security-and-monitoring.md](data-security-and-monitoring.md).

## Related

- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): stage 2 (store) is the data lake. That file defines the lake, how it differs from a warehouse (schema-on-read vs schema-on-write), and how the deliver stage's warehouse works with it as a lake house.
- [batch-and-streaming.md](batch-and-streaming.md): stage 1 (ingest) works differently per ingest mode. Batch loads land files in the lake on a schedule, while streams deliver records continuously and can feed real-time processing in stage 4.
- [orchestration-and-automation.md](orchestration-and-automation.md): orchestration chains the stages into one workflow (crawl, transform, load, notify, with retries), and automation runs each repetitive task in them. Zero-ETL removes some of the ingest and process steps altogether.
