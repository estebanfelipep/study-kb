# Evaluation plan

This file covers the evaluation plan, the document that translates organizational KPIs into system goals and measurable metrics, how to build one, a short worked example, and a nine-step roadmap to implement it. 

It builds on [hill-climb-lifecycle.md](hill-climb-lifecycle.md), which owns the process and the refund chatbot walk-through.

## What it is

An evaluation plan is a structured document that details how you will evaluate your system to verify it meets organizational goals.

It is the **interface between stakeholders and engineers**. It translates high-level corporate KPIs into system capabilities, target metrics and individual evaluation tasks.

In the lifecycle, stages 1 and 2 produce the KPIs and agent capabilities this plan starts from, and stages 4 to 6 use the plan: the pre-launch plan is written in stage 4 and the post-launch plan in stage 6.

## Building the plan: a translation in three steps

```
  Organizational KPI    System goal         Evaluation metrics
  (the business goal)   (how the system     (what you measure and
                         supports it)        hill climb)
 +------------------+  +----------------+  +--------------------+
 | 1. Identify      |->| 2. Define      |->| 3. Define          |
 |    KPIs          |  |    system goals|  |    metrics         |
 +------------------+  +----------------+  +--------------------+
```

| Step | What you do |
|---|---|
| 1. Identify organizational KPIs | Determine the high-level goals the project must support |
| 2. Define system goals | Identify how the generative system supports those KPIs |
| 3. Define evaluation metrics | Determine the specific, measurable technical indicators you hill climb to tell whether the system is hitting its goals |

### Example: two goals from one chatbot

The KPIs are the ones set in [stage 1 of the lifecycle](hill-climb-lifecycle.md). This is what the plan adds for each:

**Goal 1: decrease resolution time.** A request resolved through the chatbot is resolved faster than 2 hours, so the system goal is to resolve a high percentage of return and refund queries entirely through the chatbot, with no human agent involved. The metrics to hill climb are the correctness of the return request response, the absolute error of refund amounts, and the correctness of order and refund database lookup tool use. They are measured on a mix of sampled historic and simulated data, and later in a live A/B test.

**Goal 2: maintain customer satisfaction.** The system goal is to keep chatbot interactions polite, helpful and localized in key languages. The metrics are tone rubrics, helpfulness rubrics and a low turn count to resolution, measured on simulated data and later in a live A/B test.

| Organizational KPI | System goal | Technical metrics and rubrics |
|---|---|---|
| Resolve 30% of return requests within 2 hours | Resolve a high % of queries entirely by the chatbot | Correctness of return requests, absolute error of refund amounts, order and refund lookup tool use correctness |
| Keep customer satisfaction above 4.5/5 | Provide polite, efficient chatbot support in key languages | Tone rubric, helpfulness rubric, low turn count to resolution |

The first row as a tree, from KPI down to the metrics:

```
        Organizational KPI:
        resolve 30% of return requests within 2 hours
                          |
                          v
        System goal: resolve a high % of queries
        entirely by the chatbot
                          |
        +-----------------+------------------+
        |                 |                  |
        v                 v                  v
  Technical metric:  Technical metric:  Technical metric:
  correctness of     absolute error     database lookup
  return request     of refund          tool correctness
  response           amounts
```

## A short example of a plan

The targeted KPIs and the agent capabilities of the refund chatbot are the outputs of [stages 1 and 2 of the lifecycle](hill-climb-lifecycle.md). On top of them, a plan for the chatbot has three parts. Items marked TBD are still to be decided. [Stage 4 of the lifecycle](hill-climb-lifecycle.md) holds the pre-launch plan in its finished form.

| Part | Content |
|---|---|
| Measurable metrics | Rubric ratings for helpfulness, professionalism and friendliness. Precision and recall for return and refund requests, calculated on simulated user sessions based on historic chat logs. Mean Absolute Error (MAE) under $0.50 for refund amounts. Agent determination of escalation requirement in simulated user sessions (TBD) |
| Evaluation work | Develop helpfulness, professionalism and friendliness rubrics with human annotators, then scale with autoraters. Simulate user sessions and validate them for realism. Run rubric analyses on historical chats to see whether rubric ratings correlate with customer satisfaction scores. Validate refund amounts using synthetic ground-truth data (TBD). Investigate safety guardrails and edge cases to establish release gates (TBD) |
| Deployment plan | A suggestion mode where human support agents confirm or rewrite chatbot recommendations (TBD). A live A/B test on a small user sample (TBD) |

## The nine-step roadmap

| Step | Name | What you do | Lifecycle stage |
|---|---|---|---|
| 1 | Translate KPIs | Translate organizational KPIs into system goals and measurable hill-climbing metrics | 1 and 2 |
| 2 | Vibe out | Prototype and gather data. Review early behavior exploratorily ("vibes"). Write the first complete version of the plan and keep refining it | 3 |
| 3 | Begin human annotation | Collect human annotations to anchor rubric development and the first evaluations | 4 |
| 4 | Establish deterministic metrics | Configure cheap, fast deterministic filters, such as token bounds and regex, as early quality gates | not named |
| 5 | Construct structured rubrics | Write clear rubrics and refine them with the human annotations | 4 and 5 |
| 6 | Calibrate autoraters | Compare autorater outputs with human ratings before scaling. This completes the move from vibes to formal hill climbing | 4 and 5 |
| 7 | Analyze system internals | Evaluate trajectories and intermediate steps, such as tool calls, to diagnose internal failures | not named |
| 8 | Simulate data | Simulate data to fill gaps in the evaluation datasets, especially online data gaps | 4 and 5 |
| 9 | Deploy and monitor | Launch in phases and use production data to feed the quality flywheel | 6 |

### Where the three evaluation types show up

[genai-poc.md](../genai-poc.md) names three evaluation types for choosing a model. The roadmap keeps using them after the choice, each in a different step:

| Evaluation type | Roadmap steps |
|---|---|
| Human evaluation | 3 (human annotation), 6 (calibrate autoraters) |
| Model-based evaluation | 5 (rubrics), 6 (autoraters) |
| Metrics-based evaluation | 4 (deterministic metrics), 7 (system internals) |

The deterministic metrics come first as cheap, fast early quality gates. Rubrics and autoraters then cover the subjective output those gates can't check.

## Related

- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): the source of truth this plan builds on. It owns the six stages, the refund chatbot walk-through, and the pre-launch and post-launch plans. This file adds the KPI-to-metric translation, a draft plan, and the roadmap for building the evaluation.
- [stakeholder-discovery.md](../stakeholder-discovery.md): a discovery call's translation table turns a stakeholder statement into a constraint and a design decision. This plan does the matching translation from a KPI to a system goal and a metric, so both sit between a stakeholder and the build.
- [rubric-design.md](rubric-design.md): how to write the rubrics of steps 5 and 6, and when to pick a fixed or an adaptive one.
- [synthetic-data-for-agent-evaluation.md](synthetic-data-for-agent-evaluation.md): the simulation of step 8, single-turn generation and user simulation.
- [core-concepts.md](core-concepts.md): the records that step 7's trajectories and tool calls are read from.
- [design-document.md](../design-document.md): the design document fixes success criteria before the build, which this plan then turns into KPIs, metrics and evaluation tasks.
- [genai-poc.md](../genai-poc.md): the PoC's "set success metrics" phase and its three evaluation types are the starting point. This plan is how those metrics are derived from KPIs and kept running after the PoC.
- [bedrock.md](../../../aws/aws-services/aws-ai/bedrock.md): Bedrock's Model Evaluation is the AWS implementation of the three evaluation types in the table above.
- [prompt-and-context-engineering.md](../prompt-and-context-engineering.md): its metrics for a memory-enabled agent (precision and recall, Recall@K, task success) are one set of capability metrics of the kind this plan defines per capability.
- [claude-api-foundations.md](../claude-api-foundations.md): sampling makes the same prompt return different wording each run, which is why evaluation can't rely on exact text. Its rule "pick the smallest model that meets your eval" needs the eval this plan produces.
