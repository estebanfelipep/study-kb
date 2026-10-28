# Amazon QuickSight

This file covers Amazon QuickSight: AWS's BI and dashboard service, both for business analysis and for monitoring pipelines, with examples.

## What it is

QuickSight lets you **visualize and analyze** data with SQL, charts, graphs and **dashboards**. In the pipeline it's a **delivery** service for business analysts and executives. The course also recommends it, alongside Managed Grafana, for **monitoring end-to-end workflows** through dashboards.

QuickSight is now sold under the **Amazon Quick Suite** branding, but exams say QuickSight.

## Characteristics

- It's a **BI service** first, built for business users and business metrics.
- It reads business data from Athena, Redshift, S3 and databases.
- For monitoring, it suits **data-quality and pipeline KPIs** tracked over long periods, such as daily rows loaded or freshness by table. These dashboards are usually built on Athena over logs or on a metrics table.
- It's the CDO's usual window into the data, through dashboards.

## Example

- A weekly report for data owners shows freshness and row counts per table over the last 90 days, highlighting tables that missed their SLA.
- A nightly pipeline writes Parquet files to S3. The next day, Athena and QuickSight use them for trend reports.

## Related

- [athena.md](athena.md): QuickSight dashboards are often built on Athena queries over S3 data, including logs and metrics tables for pipeline monitoring.
- [redshift.md](redshift.md): QuickSight reads curated data from Redshift to serve BI dashboards.
- [managed-grafana.md](../aws-monitoring/managed-grafana.md): the course recommends both for end-to-end workflow monitoring; Grafana is for operational dashboards across tools, QuickSight for business and long-term trend reporting.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): QuickSight is the delivery pick when a question says "dashboards", "visualize", "business users" or "BI tool".
- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares QuickSight with Managed Grafana and CloudWatch dashboards: CloudWatch dashboards for quick views of AWS metrics, Grafana for operational dashboards across many sources, QuickSight for business users and trends.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): QuickSight is one of the two visualization tools the course recommends for a single view of system health, and the last step of the example secured pipeline.
- [deliver-on-aws.md](../../aws-data-engineering/aws-data-pipeline/deliver-on-aws.md): QuickSight is a stage 5 (deliver) service for business analysts and executives.
- [data-personas.md](../../../data-engineering/data-personas.md): QuickSight serves the data analyst's need for reports and visualizations, and is the CDO's window into the data through dashboards.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): QuickSight is now sold under the Amazon Quick Suite branding, but exam material still says QuickSight.
