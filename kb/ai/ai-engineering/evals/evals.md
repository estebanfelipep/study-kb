# evals — index

This folder covers evaluating generative and agentic systems: what an eval is, the lifecycle that drives a system toward organizational KPIs, how to plan the evaluation, how to grade subjective output, and how to get test data.

## How to read this folder

- **Before:** [design-document.md](../design-document.md), which fixes the success criteria that evals check, and [genai-poc.md](../genai-poc.md), which names the three evaluation types.
- **Order:** the lifecycle first, as the big picture, and it defines what an eval is and the trace and session an agent leaves behind. Then the plan, which also covers test data, and the rubrics and judge that fill it in.
- **After:** [agent-orchestration.md](../agent-orchestration.md), for the evaluator-optimizer pattern that puts a judge inside a loop.

## Files (in reading order)

**The lifecycle and the plan**

- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): what an eval is, the span, trace and session an agent leaves behind, why tests find a failure but a trace locates it, and Google's six-stage lifecycle for generative and agentic systems, built backward from organizational KPIs: why measure, the ragged edge, the stages from goals to deploy and monitor, worked through a returns and refunds chatbot, and why to diagnose before re-prompting. Read when: you need what evals are for, what a trace or session is, which kind of test catches which failure, how to take an AI system from a business KPI to a measured, hill-climbed launch, what to monitor after it, or why to diagnose before re-prompting.
- [evaluation-plan.md](evaluation-plan.md): builds on the lifecycle: the document that translates organizational KPIs into system goals and metrics, with a draft plan, the nine-step roadmap that maps to the lifecycle stages, and how to simulate test data (single-turn generation and user simulation). Read when: you need how to write an evaluation plan, what order to build evaluation in, or test data for an agent without real traffic or user data.

**Grading**

- [rubrics-and-llm-judge.md](rubrics-and-llm-judge.md): how to write a rubric for subjective output (graduated scales, operational definitions, concrete anchors), fixed versus adaptive rubrics, and the LLM judge (autorater): a second model call that grades output against the rubric and gives reasoning before the score. Read when: you need to evaluate helpfulness, tone or other subjective quality, or to make a model's grading of another model trustworthy.
