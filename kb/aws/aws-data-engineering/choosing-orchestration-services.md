# Choosing orchestration services

This file holds the comparisons and exam pick-rules for orchestrating, automating and connecting pipeline steps: Step Functions, MWAA, Glue workflows, Lambda, EventBridge, SNS, SQS and API Gateway.

All content here is _(added)_ general knowledge. Service details are in each service's file in [aws-services](../aws-services/aws-services.md). The vendor-neutral concepts are in [orchestration-and-automation.md](../../data-engineering/orchestration-and-automation.md).

## If the question says… pick

| If the question says… | Pick |
| --- | --- |
| "Visual workflow", "coordinate multiple AWS services", "retries and error handling", "serverless orchestration" | [Step Functions](../aws-services/aws-application-coordination/step-functions.md) |
| "Apache Airflow", "existing Airflow DAGs", "Python-defined workflows", "open source" | [MWAA](../aws-services/aws-application-coordination/mwaa.md) |
| "Chain Glue crawlers and Glue jobs only" | [Glue workflows](../aws-services/aws-analytics/glue.md) |
| "React to an event" (file uploaded, record changed), "run on a schedule", "SaaS events" | [EventBridge](../aws-services/aws-application-coordination/eventbridge.md) (often → Step Functions or Lambda) |
| "Run a small piece of code when X happens" | [Lambda](../aws-services/aws-compute/lambda.md) |
| "Notify multiple systems or people at once", "fan-out" | [SNS](../aws-services/aws-application-coordination/sns.md) |
| "Decouple", "buffer requests", "process at its own pace", "retry failed messages" | [SQS](../aws-services/aws-application-coordination/sqs.md) |

## Step Functions vs MWAA vs Glue workflows

|  | **Step Functions** | **MWAA (Airflow)** | **Glue workflows** |
| --- | --- | --- | --- |
| Scope | Any AWS service | Any service, AWS or not, via Airflow operators | **Only Glue** crawlers, jobs and triggers |
| Defined in | Visual designer or JSON/YAML (Amazon States Language) | **Python** code (DAGs) | Glue console or API |
| Infrastructure | **Serverless** | An Airflow environment you size and pay for while it runs | Serverless |
| Pick it when | AWS-native orchestration, least overhead, visual workflow | Team already uses Airflow, or needs open-source portability | The whole pipeline is Glue |

**MWAA vs Step Functions in one line:** MWAA for existing Airflow code, Python-first teams and many non-AWS systems (costs money while the environment runs, even idle). Step Functions for AWS-native, serverless, visual workflows billed per state transition, better for event-driven and short, high-volume workflows.

## Lambda vs Step Functions vs a Glue job

|  | **Lambda** | **Step Functions** | **Glue job** |
| --- | --- | --- | --- |
| Role | **Does the work** (one task) | **Coordinates the work** (many tasks) | **Does heavy ETL work** |
| Duration | Up to 15 minutes | Up to 1 year (Standard) | Hours |
| Data size | Small to medium (one file, one batch of records) | Doesn't process data itself | Large (GB to TB, distributed Spark) |
| Pick it when | Small, event-driven tasks | Multi-step workflows with retries and branches | Big transformations that would time out in Lambda |

## SNS vs SQS vs EventBridge

|  | **SNS** | **SQS** | **EventBridge** |
| --- | --- | --- | --- |
| Pattern | **Publish/subscribe (push)** | **Queue (pull)** | **Event bus (push, with rules)** |
| Delivery | One message → **many subscribers** at once | One message → **one consumer** | One event → targets that **match rules** |
| Stores messages? | No (delivers immediately) | **Yes**, up to 14 days, until processed | No (with optional archive and replay) |
| Filtering | Subscription filter policies | None (consumer reads everything) | **Rich content-based rules**, input transformation |
| Best for | Notifications, fan-out to several systems or people | **Buffering work**, decoupling, smoothing load spikes | Routing events from AWS services, SaaS apps and your apps; schedules |

### EventBridge vs SNS

Both push events to several targets.

- **EventBridge:** rich content-based filtering, SaaS and AWS service events built in, input transformation, scheduling, archive and replay. Best for **routing events between systems**.
- **SNS:** simpler, higher-throughput **fan-out**, and can notify **people** directly (email, SMS, mobile push).

### SNS vs SQS

- **SNS pushes** one message to **many** subscribers immediately and doesn't store it.
- **SQS stores** messages until **one** consumer **pulls** and processes each one.
- **Together (SNS + SQS fan-out):** SNS sends to several SQS queues, and each queue buffers work for a different consumer that runs at its own pace.

### SQS vs Kinesis Data Streams

Both buffer data between producers and consumers.

- **SQS:** each message is a **job** for **one** consumer and is **deleted** once processed. No replay.
- **Kinesis:** each record is an **event** that **many** consumers can read, in order per shard, and **replay** until it expires.

## API Gateway vs Application Load Balancer

Both can send HTTP requests to Lambda.

- **API Gateway:** API features (keys, usage plans, throttling, request validation, caching), pay per request. Best for **public or partner APIs**.
- **ALB:** simpler, cheaper at very high steady traffic, and also routes to EC2 and containers. Best for **web apps** with mixed backends.
