# Data discovery

This file covers data discovery: what it is, the questions it answers, its five steps with example questions, and how data is classified by type, source and ingest mode.

## What it is

**Data discovery** is the process of finding and understanding the relevant data sources in an organization, and the relationships between them. It's the first step to getting value from data.

- It's a **prerequisite** to architecting and deploying a data analytics system.
- It's also **ongoing**. New sources, opportunities and business goals keep appearing, and discovery lets you respond quickly and accurately.
- The steps usually happen at the start of a project but are **iterative and cyclical** throughout it.

## The questions discovery answers

| Question | Answered in step |
| --- | --- |
| Which data should be analyzed, and what is it worth to the business? | 1. Business value |
| Who owns the data, and where is it? | 3. Data sources |
| Is it usable as is, or what transformations does it need? | 4. Storage/catalog, 5. Processing |
| Who needs to see it? | 2. Data consumers |
| Once curated, how should it be presented? | 2. Data consumers |

## The five steps

| # | Step | What you do |
| --- | --- | --- |
| 1 | **Define business value** | Kick-off workshops with stakeholders: understand business goals, prioritize use cases, identify potential sources |
| 2 | **Identify your data consumers** | Interactive sessions with stakeholders such as data scientists and analysts |
| 3 | **Identify your data sources** | Research internal and external sources where data is generated and stored (databases, applications, files) |
| 4 | **Define storage, catalog and data access needs** | Pick the best storage per data type, assess data quality to find processing needs, catalog and register sources |
| 5 | **Define data processing requirements** | Extract relevant data, then curate and transform it |

The AWS tools the course names for step 5 are in [functions-and-personas-on-aws.md](../aws/aws-data-engineering/aws-data-pipeline/functions-and-personas-on-aws.md).

### Step 1: Define business value

- How would insight into the data provide value?
- Do you want a **new revenue stream** from your data?
- What are the challenges with your current approach and tools?
- Would you benefit from **fraud detection, predictive maintenance or root-cause analysis** to reduce **mean time to detection (MTTD)** and **mean time to recovery (MTTR)**?
- How are you continually innovating for customers and improving their experience?

### Step 2: Identify your data consumers

- Who are the end users (business analysts, data engineers, data analysts, data scientists)?
- Which insights do you get today? Which are on the roadmap?
- What are the consumption models?
- Which tool or interface do consumers use?
- **How real-time** must the data be (near real time, every 15 minutes, hourly, daily)?
- How many consumers per consumption model? What's the **peak concurrency**?

### Step 3: Identify your data sources

Classify data along **three lines: data type, data source and ingest mode.**

**Data types**

| Type | Examples |
| --- | --- |
| **Structured** | Relational databases, spreadsheets, CSV, XML |
| **Semi-structured** | Non-relational databases, JSON, log files, XML with attributes, IoT sensor data |
| **Unstructured** | Text documents, images, audio, video |

The course lists XML under both: plain XML is structured, and **XML with attributes** is semi-structured.

**Data sources**

| Source | Examples |
| --- | --- |
| Databases | CRM, ERP and CMS applications |
| Files | On-premises file servers, document libraries, archives |
| Logs | Application logs, device logs |
| IoT devices | Sensor data, device metadata, time-series data |
| Mobile devices | Social media, messaging apps |
| Video | Media and entertainment services, surveillance cameras, video libraries |
| SaaS apps | User activity logs, transactional data, marketing analytics, e-commerce data |
| Datasets | Demographic, weather, geospatial mapping, transportation data |

**Ingest modes:** streaming, micro-batch and batch. They're defined, with examples, in [batch-and-streaming.md](batch-and-streaming.md).

Example questions:

- How many sources must you support? Where and how is data generated?
- What types and **formats** of data?
- Does it come from **on premises, a third-party vendor or the cloud**?
- Streaming, batch or micro-batch?
- What's the **velocity and volume** of ingestion?
- What's the ingestion interface?
- How does your team onboard new sources?

### Step 4: Define storage, catalog and data access needs

- Which data stores do you have, what's each one for, and **why that storage method** (files, SQL, NoSQL, data warehouse)?
- How is data organized today (**tiering, partitioning**)?
- How much data now, and how much later (for example, **18 months out**)?
- How do you manage governance? Which **regulatory and compliance standards** apply?
- What's your **disaster recovery** strategy?

### Step 5: Define data processing requirements

- Must data be transformed or enriched before use?
- Which transformation tools do you use? Is there a **visual editor** for transformation code?
- How often do transformations run (real time, micro-batch, overnight batch)?
- Any constraints with your current tool?

## Connections to the rest of the role

| Discovery step | Related |
| --- | --- |
| 1. Business value | The three business questions in [data-engineer-role.md](data-engineer-role.md) |
| 2. Data consumers | The personas in [data-personas.md](data-personas.md) |
| 3. Data sources | Function 2, Ingest |
| 4. Storage, catalog, access | Functions 1 (infrastructure), 4 (catalog) and 6 (governance) |
| 5. Processing | Function 3, Prepare |
