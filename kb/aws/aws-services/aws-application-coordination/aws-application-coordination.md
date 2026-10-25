# aws-application-coordination — index

Orchestrating workflows and connecting services through events, topics and queues.

## How to read this folder

- **Before:** Automation vs orchestration and the messaging patterns, in [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md).
- **Order:** From the simplest connection between two steps to full orchestration.
- **After:** [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md).

## Files (in reading order)

**Connect steps**

- [sqs.md](sqs.md): Amazon SQS: pull-based message queue, visibility timeout, DLQ, 14-day retention, Standard vs FIFO queues. Read when: you need to decouple or buffer work, or retry failed messages.
- [sns.md](sns.md): Amazon SNS: pub/sub push fan-out to many subscribers, subscriber types, and the SNS + SQS fan-out pattern. Read when: you need to notify several systems or people at once.
- [eventbridge.md](eventbridge.md): Amazon EventBridge: serverless event bus with content-based rules, input transformers, Scheduler, and archive and replay. Read when: you need to react to events, route AWS or SaaS events, or run a pipeline on a schedule.

**Orchestrate**

- [step-functions.md](step-functions.md): AWS Step Functions: visual serverless state-machine orchestration with retries, Standard vs Express workflows, and direct service integrations. Read when: you need to coordinate a multi-step pipeline across AWS services.
- [mwaa.md](mwaa.md): Amazon MWAA: managed Apache Airflow (Python DAGs, operators, DAG files in S3, environment billed while running). Read when: a team runs Airflow, or needs Python-defined workflows that span non-AWS systems.
