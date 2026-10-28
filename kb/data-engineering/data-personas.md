# Who data engineers work with

This file covers the six personas involved in building, running and using a data analytics system, and what each needs from the data engineer.

Building, running and maintaining a data analytics system is collaborative. The data engineer works with executive, managerial and technical roles.

## The six personas

| Persona | Level | Responsibility | Areas of interest |
| --- | --- | --- | --- |
| **Chief data officer (CDO)** | Executive | Builds a culture of using data to solve problems and accelerate innovation | Data quality, data governance, data and AI strategy, evangelizing the value of data |
| **Data architect** | Technical lead | Designs technical solutions to business needs and solves complex data challenges, so the CDO can deliver the vision | Pipelines, processing, integration, governance, data catalogs |
| **Data engineer** | Technical | Delivers **usable, accurate** datasets **securely** and with **high performance** | The range of pipeline tools, and how easy they are to use, configure and maintain |
| **Data security officer** | Managerial / compliance | Makes sure data security, privacy and governance are strictly defined and followed | Security, privacy regulations, protecting **PII**, **fine-grained access control** and **data masking** |
| **Data scientist** | Technical consumer | Builds ways to pull business insight out of data quickly | Tools for data manipulation, insight deeper than visualization, **ML pipelines** |
| **Data analyst** | Business consumer | Reacts to market conditions in real time; must find and analyze data quickly and easily | **Querying**, analysis, **reports and visualizations** |

The course groups the roles only as executive, managerial and technical; the Level column is a finer split.

## How the personas relate

```
CDO (sets the vision and strategy)
 └─ Data architect (designs the solution)
     └─ Data engineer (builds and runs the pipelines)
         ├─ serves → Data scientist (ML, deep insight)
         └─ serves → Data analyst (queries, reports, dashboards)

Data security officer: sets the rules every role must follow
```

## What each persona needs from the data engineer

| Persona | What they need | Related function ([data-engineer-role.md](data-engineer-role.md)) |
| --- | --- | --- |
| CDO | Trustworthy, high-quality data that shows value | 6. Quality |
| Data architect | Their design implemented and maintained | 1. Infrastructure, 5. Automate |
| Data security officer | PII protected, access fine-grained, masking applied | 6. Security and compliance |
| Data scientist | Clean, enriched data ready for ML | 3. Prepare |
| Data analyst | Data that's easy to find and fast to query | 4. Catalog, 3. Prepare |

## Personas in the pipeline

- The **data engineer** builds the ingest, store, catalog and process stages.
- **Scientists and analysts** consume the deliver stage.
- The **data security officer** owns security and governance across every stage.

The stages are in [modern-data-architecture.md](modern-data-architecture.md). Which AWS services each persona uses is in [functions-and-personas-on-aws.md](../aws/aws-data-engineering/aws-data-pipeline/functions-and-personas-on-aws.md).
