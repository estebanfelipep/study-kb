# Amazon AppFlow

This file covers Amazon AppFlow: managed data transfer between SaaS applications and AWS services.

## What it is

Amazon AppFlow is a fully managed integration service. It transfers data between SaaS applications, such as Salesforce, SAP, Zendesk, Slack or ServiceNow, and AWS services such as S3 and Redshift, with no code.

## Characteristics

- A **flow** defines the source, the destination and the trigger: on a schedule, on an event in the SaaS app, or on demand.
- Can filter, map, validate and mask fields during the transfer. This is light transformation only.
- Works in both directions, so it can bring SaaS data into the lake or send data back to a SaaS app.
- Priced per flow run plus the data processed.

## Example

- A nightly flow copies contacts and campaign results from the marketing platform into `raw/marketing/` in S3, where they're joined with the CRM data.

## Related

- [unified-customer-data-on-aws.md](../../aws-data-engineering/unified-customer-data-on-aws.md): AppFlow brings in the batch loads from the SaaS marketing and support tools in that example.
- [s3.md](../aws-general-services/s3.md): AppFlow writes SaaS data into the S3 data lake.
- [glue.md](../aws-analytics/glue.md): Glue jobs can also pull SaaS data. AppFlow needs no code for supported apps, while Glue handles heavier transformation.
