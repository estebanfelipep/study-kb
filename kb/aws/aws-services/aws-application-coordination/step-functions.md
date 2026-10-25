# AWS Step Functions

This file covers AWS Step Functions: visual, serverless orchestration of multi-step workflows, with an example pipeline.

## What it is

Step Functions is a **visual workflow service** that orchestrates and automates workflows, pipelines and processes. It **ensures tasks run in the correct order**. In data engineering, it's the AWS-native way to coordinate the steps of a pipeline across services.

## Characteristics

### In data analytics

- **Orchestrates ETL workflows** by connecting Lambda functions that extract data from sources, transform it, and load it into databases and data lakes.
- **Runs batch jobs** on data in Glue, EMR or other services.
- **Processes streaming data** by connecting Lambda functions that process data from Kinesis Data Streams or Data Firehose, for real-time analytics.
- [EventBridge](eventbridge.md) events and [SNS](sns.md) messages can start workflows. A workflow then coordinates Glue, Redshift and Athena.

### Key features _(added)_

- Workflows are **state machines**. Each step is a state: run a task, choose a branch, run steps in parallel, wait, or loop over items.
- **Retries, error catching and timeouts** are built in per step, so failure handling isn't buried in your code.
- **Direct integrations** with 200+ services let a step start a Glue job, run an Athena query, call EMR or send to SNS without writing Lambda glue code.
- Workflows are defined in a visual designer or in JSON/YAML (**Amazon States Language**).
- **Serverless:** you pay per state transition.
- There are two workflow types:
  - **Standard:** long-running (up to 1 year), exactly-once, with full history.
  - **Express:** high-volume (up to 5 minutes) and cheaper per run.
- The console shows each run as a diagram, with a failed step highlighted in red.

## Example

_(added)_ A nightly sales pipeline:

1. Start a **Glue crawler** to register yesterday's files.
2. Run a **Glue ETL job** that cleans the data and converts it to Parquet.
3. In **parallel**, run two **Athena** queries: a row-count check and a null check.
4. A **Choice** state loads the data into **Redshift** if the checks pass. If they fail, it publishes to **SNS** to alert the data team.
5. Each step retries up to 3 times with backoff before the whole run fails.

## Related

- [lambda.md](../aws-compute/lambda.md): Step Functions coordinates many Lambda functions as workflow steps, adding error handling, retries and visualization. Lambda does one task; Step Functions coordinates many.
- [glue.md](../aws-analytics/glue.md): a workflow step can start a Glue crawler or Glue ETL job directly, as in the nightly sales pipeline.
- [athena.md](../aws-analytics/athena.md): a workflow step can run Athena queries directly, such as the parallel row-count and null checks in the example.
- [redshift.md](../aws-analytics/redshift.md): the example workflow loads data into Redshift once the checks pass.
- [eventbridge.md](eventbridge.md): EventBridge rules and schedules start Step Functions workflows.
- [sns.md](sns.md): SNS messages can start workflows, and a workflow can publish to SNS to alert the data team.
- [mwaa.md](mwaa.md): the alternative orchestrator. MWAA runs Python Airflow DAGs and suits existing Airflow code; Step Functions is AWS-native, serverless and visual.
- [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md): Step Functions is AWS's orchestration service, coordinating many automated tasks, and its workflows are the state machines described there.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares Step Functions with MWAA, Glue workflows and Lambda: Step Functions for AWS-native multi-step workflows with retries, MWAA for Airflow, Glue workflows for Glue-only pipelines, Lambda for one small task.
