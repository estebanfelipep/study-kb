# Generative AI proof of concept (PoC)

This file covers how to build a generative AI proof of concept: scoping it, selecting and evaluating the model, testing performance, and calculating its business value.

## What it is

A PoC is the phase that validates technical feasibility, measures performance and demonstrates business value before committing to full-scale deployment. It succeeds with careful scoping, clear success criteria and systematic evaluation, while balancing technical validation against business objectives under time and resource limits. Scoping plans the work and sets the time-box. Development, the building and testing of the solution, happens inside that time-box, through the steps below.

```
 1 SCOPING (before building)
   problem, data, metrics, risks, stakeholders
   sets the time-box: 2 to 8 weeks
        |
        v
 +--- DEVELOPMENT (inside the time-box) --------------------+
 |                                                          |
 |  2 pick the model --> 3 test performance --> 4 prove     |
 |    requirements,        latency, throughput,   value     |
 |    evaluation,          regions                cost,     |
 |    iteration                                   time,     |
 |                                                impact    |
 +----------------------------+-----------------------------+
                              |
                              v
        go / no-go against the success metrics
```

## 1. Scoping

Scoping focuses the PoC on what matters most while managing time and resource constraints. Clear objectives, measurable success criteria and stakeholder alignment make a meaningful, decision-ready result more likely.

| #   | Phase                                 | What to do                                                                                                                                                                                                                                                                                         | Output                                              |
| --- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| 1   | Define the business problem           | Pick a problem where generative AI gives measurable value. <br><br>**Good fit:** content creation, data analysis, customer interaction, process automation. <br><br>**Poor fit:** real-time decisions with real-world consequences, and tasks that demand perfect accuracy without human oversight | A suitable use case                                 |
| 2   | Assess data                           | Check the data for fine-tuning and for running the app: quality, quantity, access, privacy, permissions, bias                                                                                                                                                                                      | Confirmation that enough representative data exists |
| 3   | Set success metrics                   | Quantitative and qualitative metrics tied to business objectives: accuracy measurements, performance benchmarks, user satisfaction scores and cost comparisons                                                                                                                                     | Go/no-go criteria                                   |
| 4   | Address responsible AI and compliance | Find edge cases and risks; add controls for bias, fairness, transparency and privacy; document regulatory requirements                                                                                                                                                                             | Controls, and risks in the evaluation criteria      |
| 5   | Time-box                              | Limit the PoC to **2 to 8 weeks**, with deliverables and checkpoints per week                                                                                                                                                                                                                      | A schedule that prevents scope creep                |
| 6   | Identify stakeholders                 | Engage business, technical and decision makers early; agree objectives, criteria and resources                                                                                                                                                                                                     | Alignment and sustained support                     |

## 2. Model selection and evaluation

Choosing the model means evaluating its technical capabilities systematically against your requirements. A structured approach reduces risk and finds the best performer for the use case. Evaluation keeps mattering after the choice, to keep the application's quality up.

```
 1 requirements      2 comparative        3 iterative testing
   analysis    --->    evaluation   --->    simple cases first,
   (modalities,        (candidates on       then edge cases
    accuracy,           your own data)            |
    latency, cost)           ^                    |
                             +---- not good enough+
```

| Stage | What to do |
|---|---|
| Requirements analysis | Document input/output modalities, accuracy expectations, latency constraints and cost targets. They guide every evaluation decision. |
| Comparative evaluation | Compare candidate models on **your actual data and use cases**. It gives an objective comparison, unlike published benchmarks alone. |
| Iterative testing | Start with straightforward cases to set a baseline, then add edge cases and challenging inputs to find the model's limits. |

**Evaluation types:**

| Type | Who or what judges the output |
|---|---|
| Human evaluation | Human evaluators give direct feedback on the outputs |
| Model-based evaluation | An AI model evaluates another model's outputs |
| Metrics-based evaluation | Quantitative performance metrics, calculated automatically |

## 3. Performance testing

Performance testing validates speed, throughput and cost-effectiveness against business requirements, and finds bottlenecks and optimization opportunities before full-scale deployment.

| Test | How | What it reveals |
|---|---|---|
| Latency | Measure end-to-end response time across prompt lengths, model types and concurrent request volumes, with a consistent method | Reliable comparisons between setups |
| Throughput | Raise concurrent requests gradually until performance degrades | Scaling characteristics and the capacity to plan for |
| Geographic performance | For global users, test from different regions | Latency by geography, and where to deploy |

```
 response
 time
   |                                  x
   |                               x
   |                           x       <- degradation point:
   |  x   x   x   x   x   x               plan capacity below it
   +--------------------------------------> concurrent requests
```

## 4. Value calculation

Demonstrating business value secures PoC approval and justifies full-scale implementation. It has three layers, from the most to the least directly measurable:

```
 +--------------------------------------------------+
 | Business impact: revenue, risk, strategic value  |
 |  +--------------------------------------------+  |
 |  | Automation benefits: time, quality, scale  |  |
 |  |  +--------------------------------------+  |  |
 |  |  | Cost comparison: TCO, per            |  |  |
 |  |  | transaction, break-even              |  |  |
 |  |  +--------------------------------------+  |  |
 |  +--------------------------------------------+  |
 +--------------------------------------------------+
```

**Cost comparison** is the financial baseline, accounting for every implementation and operational cost:

| Method | What it calculates |
|---|---|
| Total cost of ownership (TCO) | Model inference, infrastructure, development time and ongoing maintenance, compared against the current manual process or alternatives |
| Cost per transaction | Cost of one transaction across every system component, for a direct comparison with the existing process |
| Break-even analysis | The usage volume that justifies the cost, counting one-time development and ongoing operational costs |

**Process automation benefits** are operational value beyond cost reduction, and often the most compelling justification for a PoC:

| Benefit | What to quantify |
|---|---|
| Time savings | Time saved against the manual process: direct task time, plus indirect gains such as less context switching and better focus |
| Quality improvements | Fewer errors, more consistency, better output quality |
| Scalability | Handling peak loads and growth without a proportional increase in staff |

**Business impact** is broader organizational value beyond direct savings and operations. It can justify a PoC even when the immediate ROI is unclear:

| Area | What it covers |
|---|---|
| Revenue impact | New revenue opportunities |
| Risk reduction | Better compliance, less human error, stronger security, from automated and consistent application of business rules |
| Strategic value | Competitive advantage, innovation capability and organizational learning, without immediate quantifiable value |

## Related

- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): prompts are refined during iterative testing, so each candidate model is judged with good prompts rather than naive ones.
- [agent-orchestration.md](agent-orchestration.md): model-based evaluation is the same idea as the evaluator in the evaluator-optimizer pattern, one LLM judging another's output.
- [bedrock-poc.md](../../aws/aws-ai-engineering/bedrock-poc.md): applies this method on Amazon Bedrock, with a healthcare example that used de-identified, HIPAA-compliant data and set out to cut processing time and cost against manual extraction.
- [bedrock.md](../../aws/aws-services/aws-ai/bedrock.md): Bedrock's Model Evaluation runs the comparative evaluation and offers all three evaluation types.
- [design-document-and-llm-judge.md](design-document-and-llm-judge.md): Anthropic's feature-level counterpart, from a Claude course. Its design document (success criteria, budget, trust boundary, failure handling) maps onto scoping, and its calibrated LLM judge is one way to run model-based evaluation.
