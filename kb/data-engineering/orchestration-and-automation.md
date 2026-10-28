# Orchestration and automation

This file covers automation vs orchestration, messaging patterns (pub/sub, queues, event buses), workflow DAGs, zero-ETL and serverless architectures.

## The problem

As businesses rely more on data analytics, **managing the complexity of data workflows, processing and analysis** becomes a significant challenge. Without efficient coordination and automation, data pipelines become:

- **Fragmented**
- **Error-prone**
- **Time-consuming to manage**
- **Hard to scale** as data volumes grow

## Automation vs orchestration

|  | **Automation** | **Orchestration** |
| --- | --- | --- |
| Definition | Using tools and services to **automate repetitive tasks** related to data ingestion, processing and analytics | **Coordinating multiple services** to define and manage the **flow of data through a series of steps** |
| Involves | A single task that runs without manual effort | **Workflows and dependencies** between steps |
| Suitable for | **Simple, repetitive tasks** | **Complex workflows** involving multiple **services, teams and dependencies** across stages |
| Example | A function converts every new file in the lake to Parquet | A workflow runs: crawl new data → run an ETL job → load the warehouse → notify the team, with retries on failure |

**They're typically used together.** Orchestration often means coordinating multiple automated tasks in a defined sequence. Together they **streamline operations**, **improve reliability** and **empower non-programmers** to manage complex workflows.

Analogy: automation is each musician playing their part; orchestration is the conductor deciding who plays when.

## Workflows as DAGs

Many orchestrators (Apache Airflow, for example) define a workflow as a **DAG** (directed acyclic graph): tasks plus the dependencies between them. **Operators** are prebuilt task types, such as "run SQL" or "run a Spark job". Other orchestrators model workflows as **state machines**, where each step is a state: run a task, branch, run in parallel, wait, or loop.

## Messaging patterns

|  | **Publish/subscribe** | **Queue** | **Event bus** |
| --- | --- | --- | --- |
| Model | **Push**: publishers send to a topic, every subscriber gets a copy | **Pull**: consumers ask for messages | **Push with rules**: events are routed to targets that match |
| Delivery | One message → **many subscribers** | One message → **one consumer** | One event → the targets whose rules match |
| Stores messages? | No | **Yes**, until processed | No (some offer archive and replay) |
| Best for | Notifications, fan-out | **Buffering work**, decoupling, smoothing load spikes | Routing events between systems; schedules |

- **Fan-out with queues:** a topic sends to several queues, and each queue buffers work for a different consumer that runs at its own pace. If one consumer is down, its queue holds the messages until it recovers.
- **Dead-letter queue:** messages that fail too many times move aside, so one bad message doesn't block the queue.
- Queues vs streams is in [batch-and-streaming.md](batch-and-streaming.md).

The AWS services are SNS (pub/sub), SQS (queues) and EventBridge (event bus); see [choosing-orchestration-services.md](../aws/aws-data-engineering/choosing-orchestration-services.md).

## Zero-ETL

**Zero-ETL** is an approach to data integration that **minimizes or eliminates the need for ETL** processes.

- **Traditional ETL:** data is extracted from source systems, transformed or cleaned, and loaded into a data warehouse or data lake. These processes are **time-consuming and complex** to develop and maintain.
- **Zero-ETL:** data can be **queried directly from its original sources** without requiring data movement or transformation.

Zero-ETL doesn't mean zero transformation forever. It removes the **pipeline-building** step; you may still model the data afterward, for example with SQL views in the warehouse. The two main forms are **querying data in place** and **managed replication** from a source to a target.

## Serverless architecture

A **serverless architecture** is a way to build and run applications and services **without managing infrastructure**. The application still runs on servers, but the cloud provider does all the server management.

- **Extremely cost effective:** you **pay only for the time your code is running**.
- **Efficiently orchestrated and automated workflows depend significantly on serverless applications.**

Serverless is usually cheapest for spiky or unpredictable workloads. For steady, round-the-clock heavy load, provisioned capacity can cost less.

The AWS zero-ETL and serverless services are in [zero-etl-and-serverless-on-aws.md](../aws/aws-data-engineering/zero-etl-and-serverless-on-aws.md).
