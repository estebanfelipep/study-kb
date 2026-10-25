# AWS Entity Resolution

This file covers AWS Entity Resolution: matching and linking records that refer to the same entity across data sources.

## What it is

_(added)_ AWS Entity Resolution matches and links related records, such as one customer stored under different IDs in sales, marketing and support, without building custom matching logic.

## Characteristics

- _(added)_ Reads input tables defined in the [Glue](glue.md) Data Catalog, over data in [S3](../aws-general-services/s3.md), and writes match results back to S3.
- _(added)_ Matching techniques: **rule-based** (exact or fuzzy rules on fields such as email or phone), **ML-based**, or a **data service provider** that supplies its own IDs.
- _(added)_ The output gives each group of matched records a shared match ID. That's the cross-reference table used to build a golden record.
- _(added; verify)_ Priced per record processed.

## Example

- _(added)_ Records S-981 (sales), `ana@x.io` (marketing) and T-55 (support) share a normalized email and phone number. A rule-based workflow gives them one match ID, and a Glue job uses that ID to merge them into one row of `customer_360`.

## Related

- [unified-customer-data-on-aws.md](../../aws-data-engineering/unified-customer-data-on-aws.md): Entity Resolution does the ID-matching step of that example.
- [unified-customer-data.md](../../../data-engineering/unified-customer-data.md): implements entity resolution, the matching step of building a golden record.
- [glue.md](glue.md): Entity Resolution reads its input tables from the Glue Data Catalog, and a Glue job then uses the match IDs to merge records.
