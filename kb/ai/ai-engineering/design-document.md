# Design document

This file covers how to decide what "right" means before building an LLM feature, with a design document: success criteria, failure handling, a cost and latency budget, and a trust boundary.

## Sources

- [Claude Certified Developer: Foundations (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations): Anthropic's learning path. This file and [llm-judge.md](evals/llm-judge.md) come from its "Evals and judges" section, so it reflects Claude's own guidance, unlike [genai-poc.md](genai-poc.md), which comes from an AWS course.

## How it relates to the PoC

[genai-poc.md](genai-poc.md) is the AWS course's method for validating a whole generative AI solution in a time-boxed PoC. This file is Anthropic's method for the same underlying job at the level of one feature: write down the decisions first, so the built system can be checked against them.

```
  PoC (AWS course)                    Design document (Claude course)
  ----------------                    -------------------------------
  3  success metrics           <--->  success criteria
  2  requirements (cost,       <--->  cost and latency budget
        latency)
  4  responsible AI controls   <--->  trust boundary
  (nothing equivalent)                failure handling
  2  model-based evaluation    <--->  LLM judge, calibrated
```

The design document sits **before** the build, next to PoC scoping. The judge, in [llm-judge.md](evals/llm-judge.md), is one way to run the PoC's evaluation at scale.

## The design document

Before you write any production code, write down what you are going to build and how you will know it is right. A design document is that written record.

A useful design document holds four decisions, each stated concretely enough that someone could check the built system against it:

- **Success criteria** name what the feature must produce.
	- State the output for representative cases in terms specific enough to grade.
	- A vague goal like "summarize the thread" cannot be checked, while "a two-sentence summary that lists every action item and its owner" can.
	- These criteria are what your eval set is built from, so writing them first is what makes the eval possible.
- **Failure handling** names the failures the system must survive and what it does for each.
	- List the errors production will throw, and mark each one **retriable** or **terminal**.
	- Say what the user gets when a failure cannot be recovered.
	- Deciding this on paper stops the first real rate-limit response from being the moment you discover you have no error path.
- **Cost and latency budget** names the ceiling the system must stay under and the reliability floor it cannot trade away.
	- Set hard cost and latency budgets before the architecture is determined. Write down:
		- the per-request budget
		- the monthly cost ceiling
		- the latency target
		- the minimum reliability the design must hold
	- Setting these numbers first lets you check the architecture against the budget before a line of code is written.
- **Trust boundary** names which inputs are untrusted and what the system is allowed to do.
	- Write down which content the agent reads that someone else can write, and the smallest set of actions and access the feature needs to do its job.
	- Naming the boundary on paper turns least privilege into a design decision you can enforce with a hook, rather than a setting you remember to add later.

## Related

- [genai-poc.md](genai-poc.md): the AWS-sourced PoC method. Its success metrics (phase 3), requirements analysis, responsible AI controls (phase 4) and model-based evaluation each overlap one part of the design document or the judge, as the diagram above maps. It has no equivalent of failure handling, and it only names model-based evaluation without saying how to calibrate it, which [llm-judge.md](evals/llm-judge.md) does.
- [stakeholder-discovery.md](stakeholder-discovery.md): the step before this one. A discovery call's translation table supplies the design document's budget ("must cost"), trust boundary ("must not do") and proof obligations, so the document records confirmed constraints rather than assumptions.
- [bedrock-poc.md](../../aws/aws-ai-engineering/bedrock-poc.md): its least-privilege IAM and security-from-day-one steps are one way to enforce a trust boundary on AWS.
- [llm-judge.md](evals/llm-judge.md): the second model call that grades the feature's output against the success criteria written here, calibrated so its scores can be trusted.
- [claude-api-foundations.md](claude-api-foundations.md): the sampling it describes (same prompt, different wording each run) is why evals and judges exist, and its tier and reasoning-mode choices are what an eval decides.
- [evaluation-plan.md](evals/evaluation-plan.md): picks up where the success criteria stop. It turns organizational KPIs into system goals and metrics, then into a roadmap that builds toward calibrated autoraters, where this file stops at the single feature.
