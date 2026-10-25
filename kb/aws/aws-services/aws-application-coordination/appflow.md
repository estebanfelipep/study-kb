# Amazon AppFlow

This file covers Amazon AppFlow: managed data transfer between SaaS applications and AWS services.

## What it is

_(added)_ Amazon AppFlow is a fully managed integration service. It transfers data between SaaS applications, such as Salesforce, SAP, Zendesk, Slack or ServiceNow, and AWS services such as S3 and Redshift, with no code.

## Characteristics

- _(added)_ A **flow** defines the source, the destination and the trigger: on a schedule, on an event in the SaaS app, or on demand.
- _(added)_ Can filter, map, validate and mask fields during the transfer. This is light transformation only.
- _(added)_ Works in both directions, so it can bring SaaS data into the lake or send data back to a SaaS app.
- _(added; verify)_ Priced per flow run plus the data processed.

## Example

- _(added)_ A nightly flow copies contacts and campaign results from the marketing platform into `raw/marketing/` in S3, where they're joined with the CRM data.

## Related

- [unified-customer-data-on-aws.md](../../aws-data-engineering/unified-customer-data-on-aws.md): AppFlow brings in the batch loads from the SaaS marketing and support tools in that example.
- [s3.md](../aws-general-services/s3.md): AppFlow writes SaaS data into the S3 data lake.
- [glue.md](../aws-analytics/glue.md): Glue jobs can also pull SaaS data. AppFlow needs no code for supported apps, while Glue handles heavier transformation.
