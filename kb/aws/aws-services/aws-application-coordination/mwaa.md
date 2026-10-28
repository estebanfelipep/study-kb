# Amazon MWAA (Managed Workflows for Apache Airflow)

This file covers Amazon MWAA: managed Apache Airflow for orchestrating data workflows, with an example migration.

## What it is

MWAA is a managed service for orchestrating data analytics workflows on AWS with **Apache Airflow**. Its workflows can **ingest, process, transform and load** data into databases and data warehouses, and **run queries** on that data for analysis.

## Characteristics

- Workflows **handle dependencies**, support **parallel tasks**, and run tasks **sequentially** where needed.
- Airflow **workers scale dynamically** with the workload.
- A workflow is a **DAG** (directed acyclic graph) written in **Python**: a set of tasks plus the dependencies between them. See [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md).
- **Operators** are prebuilt task types: run a Glue job, run SQL in Redshift, call an API, run a Spark job on EMR, or call services outside AWS.
- AWS manages the Airflow scheduler, workers, web server and metadata database. You upload DAG files to S3.
- You size an environment, and **it costs money while it's running, even when idle**.
- Suits teams with existing Airflow code, Python-first teams, workflows touching many non-AWS systems, and open-source portability.

## Example

A data team runs 150 Airflow DAGs on self-managed servers on premises. They move to MWAA by uploading the same Python files to S3. One of those DAGs:

1. Waits for a file from a vendor's SFTP server.
2. Runs an EMR Spark job.
3. Loads the result into Redshift.
4. Calls a Salesforce API to update accounts.

The team keeps its code, skills and community operators, and stops patching Airflow servers.

## Related

- [step-functions.md](step-functions.md): both orchestrate pipelines. MWAA runs Python Airflow DAGs across AWS and non-AWS systems and costs money while its environment runs; Step Functions is AWS-native, serverless and visual, billed per state transition.
- [glue.md](../aws-analytics/glue.md): Airflow operators can run Glue jobs as tasks in a DAG.
- [emr.md](../aws-analytics/emr.md): Airflow operators can run Spark jobs on EMR, as in the example DAG.
- [redshift.md](../aws-analytics/redshift.md): Airflow operators can run SQL in Redshift, and the example DAG loads its result there.
- [s3.md](../aws-general-services/s3.md): you deploy workflows to MWAA by uploading the DAG files to S3.
- [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md): MWAA runs workflows defined as DAGs, the concept explained there.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares MWAA with Step Functions and Glue workflows: MWAA for existing Airflow code and non-AWS systems, Step Functions for AWS-native serverless orchestration, Glue workflows when the whole pipeline is Glue.
