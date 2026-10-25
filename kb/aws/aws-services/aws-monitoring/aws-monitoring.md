# aws-monitoring — index

Metrics, logs, traces, API auditing, configuration tracking, operations and dashboards.

## How to read this folder

- **Before:** What and how to monitor, in [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md).
- **Order:** From "is it working?" to "who changed it?" to fixing it. CloudWatch is the base the others build on.
- **After:** [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md).

## Files (in reading order)

**Performance**

- [cloudwatch.md](cloudwatch.md): CloudWatch metrics, the agent, Logs, Logs Insights, alarms and dashboards. Read when: you need to monitor whether resources, jobs or pipelines are slow or failing, or to alert on it.
- [x-ray.md](x-ray.md): X-Ray request tracing, the service map, and the OpenTelemetry note. Read when: you need to find which call in a request across services is slow.
- [managed-grafana.md](managed-grafana.md): Managed Grafana dashboards across many data sources for end-to-end pipeline monitoring. Read when: you need a single operational view of pipeline health across tools.

**Changes and compliance**

- [cloudtrail.md](cloudtrail.md): CloudTrail management and data events, trails, CloudTrail Lake, and data access auditing. Read when: you need who did what and when, or who read which file.
- [config.md](config.md): AWS Config configuration history, Config rules, conformance packs and auto-remediation. Read when: you need what a resource looked like over time, or whether it complies with a rule.

**Act**

- [systems-manager.md](systems-manager.md): Systems Manager Run Command, Session Manager, Patch Manager, Parameter Store, OpsCenter, Automation runbooks and Inventory. Read when: you need to act on or patch EC2 instances, or fix issues automatically when an alarm fires.
