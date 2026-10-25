# data-engineering — index

This folder covers data engineering concepts that hold regardless of vendor: the role, the people, discovery, the pipeline stages, storage models, streaming, orchestration, and security and monitoring.

Read [aws](../aws/aws.md) instead for how AWS implements these concepts.

## How to read this folder

- **Before:** nothing. This is where the data engineering material starts.
- **Order:** from who and why, to how a project starts, to the pipeline's five stages ([modern-data-architecture.md](modern-data-architecture.md), the backbone), then the parts of the pipeline, then what cuts across all stages (orchestration, security, monitoring).
- **After:** [aws-data-engineering](../aws/aws-data-engineering/aws-data-engineering.md), which maps these concepts onto AWS in the same order.

## Files (in reading order)

- [data-engineer-role.md](data-engineer-role.md): why organizations invest in data, data management challenges, the data engineer's job and ETL summary, analytical vs operational use, and the six functions. Read when: you need what a data engineer does or why.
- [data-personas.md](data-personas.md): the six personas (CDO, architect, engineer, security officer, scientist, analyst), how they relate and what each needs. Read when: you need who works with or consumes the data engineer's output.
- [data-discovery.md](data-discovery.md): data discovery, its five steps with example questions, and how data is classified by type and source. Read when: you need how a data project starts, or structured vs semi-structured vs unstructured data.
- [modern-data-architecture.md](modern-data-architecture.md): data silos, the modern data architecture and strategy, and a section per pipeline stage: ingest (kinds of source and how each is ingested), store (what lake storage needs), catalog (metadata, crawlers), process (transformations, kinds of engine) and deliver (ways to deliver, purpose-built database types). Read when: you need the stages data flows through, what happens in one stage, or why silos are a problem.
- [batch-and-streaming.md](batch-and-streaming.md): batch, micro-batch and streaming ingest modes, what a stream is, data in motion vs at rest, and streams vs queues. Read when: you need how streaming works or how ingest modes differ.
- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): data lakes, lake vs warehouse, schema-on-read vs schema-on-write, lake house, OLTP vs OLAP, and columnar file formats. Read when: you need where data should be stored and why.
- [orchestration-and-automation.md](orchestration-and-automation.md): automation vs orchestration, DAGs and state machines, pub/sub vs queues vs event buses, zero-ETL and serverless. Read when: you need how pipeline steps are coordinated and connected.
- [data-security-and-monitoring.md](data-security-and-monitoring.md): security vs governance, the CIA triad, the five security areas, best practices, and what and how to monitor. Read when: you need how a data system is secured, governed or monitored.
