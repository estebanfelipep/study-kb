# The role of the data engineer

This file covers why organizations invest in data, the data management problems they face, what a data engineer does, and the six functions of the job.

## Why organizations invest in data

Organizations of every type and size ask the same three questions:

| Question | What it's really about |
| --- | --- |
| How can we offer **hyper-personalized experiences** to customers? | Using customer data to tailor products and interactions |
| How can we help **business users make data-driven decisions**? | Getting trustworthy data and insights to non-technical people |
| Where can we **innovate, improve operations and optimize costs**? | Finding efficiencies and new opportunities in the data |

To answer them, an organization needs three things:

1. **A data-driven culture.**
2. **Democratized access** to data and insights, so more people can use them.
3. **Innovative technologies**: data analytics, machine learning and generative AI.

## Data management challenges

| Challenge | What it means |
| --- | --- |
| **Data and processing silos** | Each business unit keeps its own data and tools, so nobody sees the full picture |
| **Excessive data movement** | Data is copied between systems over and over, which adds cost, latency and risk |
| **Data duplication** | The same data lives in several places and drifts out of sync, so there's no single source of truth |

Silos are covered in depth in [modern-data-architecture.md](modern-data-architecture.md).

## The data engineer's job

A data engineer **turns raw data into valuable insights**. They:

- **Design, develop and maintain data architectures.**
- **Build ETL (extract, transform, load) pipelines.**

Data analysts, data scientists and other **data consumers** ([data-personas.md](data-personas.md)) use these to access and analyze data.

### The one-line summary

> **Get data from sources → make it useful → serve it to stakeholders.**

| Step | ETL stage | What happens |
| --- | --- | --- |
| Get data from sources | **Extract** | Pull data out of databases, apps, logs, streams and other sources |
| Make it useful | **Transform** | Clean, validate, join, reshape and enrich it |
| Serve it to stakeholders | **Load** (and serve) | Put it where consumers can query it, such as a data lake, a warehouse or a dashboard |

## Analytical vs operational use _(added: Q&A)_

**Question:** is data engineering only about turning data into something analysts use for business decisions, without directly affecting the product?

**Answer:** mostly, but only half true. Turning raw data into something people use for decisions is the core of it. But the data often **flows back into the product**.

### Analytical use: beside the product

- Data comes **out of** the product (orders, clicks, logs, sensor readings), is cleaned and combined, and lands in a warehouse, a data lake or a dashboard.
- Analysts use it to answer business questions, such as "which region is losing customers?"
- If the pipeline breaks, **the product keeps running**, but reports go stale.

### Operational use: back into the product

- **Recommendations:** watch or purchase history goes through a pipeline into a model, and the model's output drives the "Recommended for you" row users see.
- **Fraud detection:** transactions stream through a real-time stream and are scored as they arrive. A fraudulent one is blocked, so the pipeline decides what happens in the product.
- **Personalization and pricing:** customer segments built by pipelines drive marketing emails, in-app offers or dynamic prices.
- **Operational features:** "your order is out for delivery", or a video service lowering playback quality when streaming metrics show buffering. These are streams driving live behavior.
- **Reverse ETL:** cleaned data is pushed back into operational tools, such as a customer's lifetime value sent to the CRM so support agents see it.

This is why **data scientists** are a persona next to analysts: their models often end up as product features.

**Takeaway:** the data engineer builds the plumbing either way. Whether that plumbing **informs** the product or **runs part of it** depends on who consumes the data at the end.

## The six functions

A data engineer might do all six functions, or share them with other specialists.

| # | Function | What it involves |
| --- | --- | --- |
| 1 | **Build and manage data infrastructure and platforms** | Set up databases, data lakes and data warehouses |
| 2 | **Ingest data from various sources** | Bring data from databases, applications, files and streaming devices into the central platform |
| 3 | **Prepare ingested data for analytics** | Clean, transform and enrich it |
| 4 | **Catalog and document curated datasets** | Detect format and schema, group data into tables, write metadata; tag metadata for governance and discoverability |
| 5 | **Automate regular workflows and pipelines** | Simplify and speed up data processing |
| 6 | **Ensure data quality, security and compliance** | Access controls, authorization policies, monitoring; fine-grained access so people get the right privileges in the right context |

The AWS services for each function are in [aws-data-pipeline.md](../aws/aws-data-engineering/aws-data-pipeline.md).

### How the functions map to the one-line summary _(added)_

| Summary step | Functions |
| --- | --- |
| Foundation everything runs on | 1. Infrastructure |
| Get data from sources | 2. Ingest |
| Make it useful | 3. Prepare, 4. Catalog |
| Serve it to stakeholders | 4. Catalog (so they can find it), 6. Govern access |
| Across all steps | 5. Automate, 6. Quality and security |

## Related

- [data-personas.md](data-personas.md): the data engineer is one of six personas. The CDO and the data architect set the vision and design that the engineer builds. Scientists and analysts are the data consumers the engineer serves, and the data security officer sets the rules for function 6.
- [data-discovery.md](data-discovery.md): discovery comes before the functions. Its five steps find the business value, consumers, sources, storage needs and processing needs that functions 1 to 6 then build for. Its step 1 answers the three business questions at the top of this file.
- [modern-data-architecture.md](modern-data-architecture.md): the six functions build the five pipeline stages. Ingest builds stage 1, infrastructure stage 2, catalog stage 3 and prepare stage 4. Automate and quality and security span all of them. That file also covers the data silos behind the management challenges listed here.
