# Amazon CloudWatch

This file covers CloudWatch: metrics, logs, alarms and dashboards for monitoring data pipelines.

## What it is

CloudWatch collects **metrics** from AWS resources such as EC2 instances, databases and data pipelines. You can **set alarms** and **visualize** performance metrics. It's the main monitoring service for resources, analytics jobs and data pipelines. It answers "**Is** the Glue job slow or failing?".

## Characteristics

- Monitors **resources** (CPU, memory, network traffic, disk I/O, to find performance bottlenecks), **analytics jobs** (run time, errors, records processed, job status) and **data pipelines** (Glue, Step Functions, Lambda health and bottlenecks).
- **Metrics:** most services publish them automatically (Glue job duration, Lambda errors, Kinesis iterator age, Redshift CPU). You can publish **custom metrics**, such as "rows rejected".
- **Memory and disk usage on EC2 aren't collected by default.** You need the **CloudWatch agent**.
- **Logs:** CloudWatch Logs stores output from Lambda, Glue, EMR and apps. **Logs Insights** queries them.
- **Alarms** trigger [SNS](../aws-application-coordination/sns.md) notifications, Auto Scaling or [Systems Manager](systems-manager.md) actions.
- **Dashboards** show metrics in one view, for engineers.
- Aggregates over time per resource; tracing one request across services is [X-Ray](x-ray.md)'s job.
- Observes; Systems Manager acts. An alarm in CloudWatch commonly triggers a Systems Manager runbook.

## Example

An alarm on the Kinesis `GetRecords.IteratorAgeMilliseconds` metric fires when consumers fall more than 5 minutes behind. It notifies the on-call engineer through SNS before the stream's retention period runs out and data is lost.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares CloudWatch with X-Ray (aggregated metrics per resource vs one request's path), Systems Manager (observes vs acts), CloudTrail and Config, and CloudWatch dashboards with Managed Grafana and QuickSight.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): CloudWatch is the course service for monitoring resources, analytics jobs and data pipelines, and raises the alarms in the example secured pipeline.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): CloudWatch implements "what to monitor" (resources, jobs, pipelines) and the "set up alerts for critical failures" best practice.
- [x-ray.md](x-ray.md): CloudWatch aggregates metrics and logs per resource over time; X-Ray traces individual requests across services to find which call is slow.
- [systems-manager.md](systems-manager.md): a CloudWatch alarm commonly triggers a Systems Manager Automation runbook, so CloudWatch observes and Systems Manager acts.
- [sns.md](../aws-application-coordination/sns.md): CloudWatch alarms publish to SNS to notify the on-call engineer.
- [managed-grafana.md](managed-grafana.md): Managed Grafana pulls CloudWatch metrics into dashboards that combine them with other sources.
- [kinesis-data-streams.md](../aws-analytics/kinesis-data-streams.md): CloudWatch tracks the Kinesis `GetRecords.IteratorAgeMilliseconds` metric to alarm when consumers fall behind, before records expire.
