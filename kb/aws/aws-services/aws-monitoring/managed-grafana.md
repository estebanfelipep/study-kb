# Amazon Managed Grafana

This file covers Managed Grafana: operational dashboards across many data sources for end-to-end pipeline monitoring.

## What it is

Managed Grafana is used for **monitoring end-to-end workflows** through dashboards. The course recommends **integrating monitoring with visualization tools** like it for a **single view of overall system health**.

## Characteristics

- Fully managed **Grafana**, the open-source dashboard tool.
- Pulls from many sources at once: **CloudWatch, Prometheus, X-Ray, OpenSearch, Athena, Redshift** and non-AWS tools.
- Sign-in through IAM Identity Center.
- Audience is engineers and operations; business reporting is [QuickSight](../aws-analytics/quicksight.md)'s role.

## Example

One Grafana dashboard shows Kinesis throughput, Glue job durations, Redshift query queues and the count of failed Step Functions runs, so the data team sees the whole pipeline on one screen.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Managed Grafana with CloudWatch dashboards and QuickSight: Grafana is for operational dashboards across many sources, CloudWatch dashboards for quick AWS metric views, QuickSight for business and trend reporting.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): the course recommends Managed Grafana for a single view of overall system health, and it is the one pipeline dashboard in the example secured pipeline.
- [cloudwatch.md](cloudwatch.md): CloudWatch is one of the data sources Grafana pulls metrics from.
- [quicksight.md](../aws-analytics/quicksight.md): both can show end-to-end workflow dashboards, but Grafana targets engineers and operations, while QuickSight targets business users.
