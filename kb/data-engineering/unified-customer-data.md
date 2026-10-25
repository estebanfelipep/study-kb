# Unified customer data: a worked example

This file follows one customer update from a sales system to marketing, to show how a modern data architecture removes data silos: one copy per source, one merged record per customer, and a view per department.

All content here is _(added)_: general knowledge from Q&A, not the course notes.

The example uses the five stages from [modern-data-architecture.md](modern-data-architecture.md) and the personas from [data-personas.md](data-personas.md). Read those first if the stages are new.

## What "unified" means

| Common assumption | More precisely |
| --- | --- |
| "All departments read from the unified place" | Departments read their **analytical** data from the unified place. Each keeps its own **operational** system (sales keeps its CRM). The lake is a unified *copy* for analysis, not a replacement for the apps |
| "An update in one department changes the data for all of them" | The update is **copied** from the source into the lake, then flows into every dataset built from it. It reaches other teams **after a delay** that the pipeline design sets, from seconds to a day |
| "The data architect makes sure…" | The **architect designs** it. The **data engineer builds and runs** the pipelines. The **security officer** sets who may see what |
| "Each department gets its own data" | Each department gets **curated datasets or views** of the same underlying data, filtered to what it's allowed to see. There aren't separate copies per department |

The hardest part in practice is **agreeing which record is "the" customer**. Sales, marketing and support each have their own customer ID, so the pipeline has to match them up.

## Before: silos

```
 Sales            Marketing          Support
 ┌──────────┐     ┌──────────┐       ┌──────────┐
 │ CRM DB   │     │ Email    │       │ Ticket   │
 │ cust_id  │     │ tool     │       │ system   │
 │ = S-981  │     │ email =  │       │ cust =   │
 │          │     │ ana@x.io │       │ T-55     │
 └──────────┘     └──────────┘       └──────────┘
   no shared ID, no shared copy, different access rules
```

Ana moves from Madrid to Lisbon and tells her sales rep. Sales updates the CRM. Marketing's email tool still says Madrid, so she gets invited to a Madrid event. Every sign of a silo from [modern-data-architecture.md](modern-data-architecture.md) shows up here: isolated, incompatible (three IDs for one person), duplicated (three addresses that drift apart), and inconsistently governed.

## After: one flow, many views

```
 Sources (unchanged)       Pipeline                 Consumers
 ┌──────────┐
 │ Sales CRM│──CDC──┐
 └──────────┘       │      ┌───────────────────┐
 ┌──────────┐       ├────▶ │ 1-2 Ingest+store  │
 │ Email    │─batch─┤      │   raw/ zone       │
 └──────────┘       │      └─────────┬─────────┘
 ┌──────────┐       │                ▼
 │ Tickets  │─batch─┘      ┌───────────────────┐
 └──────────┘              │ 3 Catalog         │
                           │ 4 Process: match  │
                           │   IDs, merge,     │
                           │   pick sources    │
                           └─────────┬─────────┘
                                     ▼
                           ┌───────────────────┐   ┌─────────────┐
                           │ curated/          │──▶│ Sales view  │
                           │ customer_360      │──▶│ Mktg view   │
                           │ (one row per      │──▶│ Support view│
                           │  real customer)   │   └─────────────┘
                           └───────────────────┘
        Governance across all of it: catalog + permissions
```

## Following the update, stage by stage

1. **Sales writes to its own system.** The CRM is an OLTP database, and it stays the **source of truth for the fields sales owns**, such as address and account owner. Nothing about sales' daily work changes.
2. **Ingest: the change is captured.** **Change data capture (CDC)** reads the CRM's change log and copies only what changed: "customer S-981, city: Madrid → Lisbon, at 10:42". It doesn't reload the whole table. The marketing and support tools come in too, often as nightly batch loads. How a database's tables become files in the lake is in [replicating-databases-to-the-lake.md](replicating-databases-to-the-lake.md).
3. **Store: the change lands in the lake's raw zone.** The raw zone keeps every source as it arrived, untouched. That gives a history, and lets you rebuild if a later step is wrong.
4. **Catalog: everyone can find it.** The catalog records that `raw/crm/customers` exists, its schema, where it lives and who owns it. Without it, marketing wouldn't know the table exists.
5. **Process: build the one customer record.** This is where the silos actually get merged:
   - **Match the IDs (entity resolution):** S-981 in sales, `ana@x.io` in marketing and T-55 in support are recognized as the same person, for example by a normalized email or phone number. The output is a cross-reference table: `customer_key 7001 = S-981 = ana@x.io = T-55`.
   - **Standardize:** `Lisboa`, `Lisbon` and `LIS` become `Lisbon`, and dates and country codes follow one format. This is the standardization transformation from the process stage.
   - **Pick a winner per field (survivorship):** the rule is decided once, by the architect with the departments. For example, address comes from the CRM, email preferences from marketing, and open tickets from support. A conflict is solved by the rule, not by whichever copy happened to change last.
   - The result is written back to the lake as `curated/customer_360`, with **one row per real customer**. This single trusted record is the **golden record**. Doing all of this as an ongoing practice is **master data management (MDM)**.
6. **Deliver: each department sees its own view of the same row.**
   - Marketing's customer profile summary is a query or view over `customer_360`. The next time it refreshes, Ana's row says Lisbon.
   - Permissions decide what each team sees. Marketing might get city, segment and email preferences, but not deal values. Sales sees deal values but not ticket text. It's one table with different column and row filters.
7. **Reach the operational tools.** Marketing's email tool doesn't read the lake. How the change gets there is the next section.

## Getting changes into operational tools

The lake is mostly *queried* by analysts and scientists. Reverse ETL jobs and the pipelines themselves read it too. Operational tools, such as the marketing platform, the CRM or the support desk, get data in one of two ways:

| What the tool needs | Path | Why |
| --- | --- | --- |
| A raw field change, such as Ana's new city | **Direct integration** from the source: the CRM sends an event, or a sync, straight to the marketing platform | Faster, and the lake isn't needed, because the data needs no processing |
| Something that only exists after processing: the golden record, a segment ("high-value customers in Lisbon"), a churn score, lifetime value | **Reverse ETL** from the curated tables | The tool can't compute it. It needs the matched, merged and enriched data only the pipeline produces |

**Rule of thumb:** analysis happens in the lake, and reverse ETL pushes the lake's *processed results* back into operational tools so teams can act on them. Simple field changes travel directly between systems. Ana's new city can reach the email tool directly, while her "Lisbon, high-value" segment arrives through reverse ETL.

## How fast other teams see a change

The pipeline design sets the delay. It's a trade-off, not automatic:

| Design | Marketing sees the change after… | Cost and complexity |
| --- | --- | --- |
| Nightly batch for every step | Up to ~24 hours | Lowest |
| CDC into the lake, with processing scheduled hourly | Up to ~1 hour | Medium |
| CDC plus streaming processing | Seconds to minutes | Highest |

Most teams don't need seconds for marketing profiles, so the delay is chosen per use case. A fraud check might need seconds, while a monthly segment report is fine with yesterday's data. The ingest modes behind these designs are in [batch-and-streaming.md](batch-and-streaming.md).

## What is and isn't unified

- **Unified:** one copy of each source in the lake, one merged record per customer, one catalog, one set of permission rules, and every department reading from the same curated tables.
- **Not unified:** each department's operational app. Sales still runs on its CRM. If marketing edits a customer in its own tool, that tool is a *source* too, and the field-ownership rules decide whether the edit wins.
- **The usual mistake:** each team copies `customer_360` into its own database and edits it there. That recreates the silos the lake was built to remove.

## Who does what

| Persona | Role in this example |
| --- | --- |
| CDO | Sets the goal of one trusted view of the customer |
| Data architect | Designs the zones, the matching approach and the field-ownership rules |
| Data engineer | Builds CDC, the matching and merge jobs and the curated table, and keeps them running |
| Data security officer | Decides which departments see which columns and rows, and how PII such as email is masked |
| Data analyst (marketing) | Queries `customer_360` for profile summaries and segments |

## Related

- [data-engineer-role.md](data-engineer-role.md): this example shows the job in practice. The engineer gets data from the sources (CDC, batch loads), makes it useful (matching, standardizing, merging) and serves it (department views, reverse ETL).
- [modern-data-architecture.md](modern-data-architecture.md): the example walks through its five stages and shows how they remove the data silos defined there.
- [replicating-databases-to-the-lake.md](replicating-databases-to-the-lake.md): explains step 2 in depth, meaning how the CRM's tables become full-load and change files in the raw zone and are merged into a current table.
- [data-personas.md](data-personas.md): the "Who does what" table applies the six personas to one project.
- [batch-and-streaming.md](batch-and-streaming.md): the delay table is a choice between the ingest modes defined there.
- [unified-customer-data-on-aws.md](../aws/aws-data-engineering/unified-customer-data-on-aws.md): builds this same example with AWS services, from DMS for CDC to Lake Formation for the department views.
