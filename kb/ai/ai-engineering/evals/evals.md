# evals — index

This folder covers evaluating generative and agentic systems: what an eval is, the lifecycle that drives a system toward organizational KPIs, how to plan the evaluation, how to grade subjective output, and how to get test data.

## How to read this folder

- **Before:** [design-document.md](../design-document.md), which fixes the success criteria that evals check, and [genai-poc.md](../genai-poc.md), which names the three evaluation types.
- **Order:** the building blocks first, then the lifecycle as the big picture, then the plan, the grading and the data that fill it in.
- **After:** [agent-orchestration.md](../agent-orchestration.md), for the evaluator-optimizer pattern that puts a judge inside a loop.

## Files (in reading order)

**Building blocks**

- [core-concepts.md](core-concepts.md): what an eval is, and the span, trace and session an agent leaves behind. Read when: you need what evals are for, or what a trace or session is.

**The lifecycle and the plan**

- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): Google's six-stage lifecycle for generative and agentic systems, built backward from organizational KPIs: why measure, the ragged edge, the stages from goals to deploy and monitor, worked through a returns and refunds chatbot, and why to diagnose before re-prompting. Read when: you need how to take an AI system from a business KPI to a measured, hill-climbed launch, what to monitor after it, or why to diagnose before re-prompting.
- [evaluation-plan.md](evaluation-plan.md): builds on the lifecycle: the document that translates organizational KPIs into system goals and metrics, with a draft plan and the nine-step roadmap that maps to the lifecycle stages. Read when: you need how to write an evaluation plan or what order to build evaluation in.

**Grading and data**

- [rubric-design.md](rubric-design.md): how to write a rubric for subjective output (graduated scales, operational definitions, concrete anchors) and when to use a fixed versus an adaptive one. Read when: you need to evaluate helpfulness, tone or other subjective quality.
- [llm-judge.md](llm-judge.md): the LLM judge (autorater): a second model call that grades output against a rubric, and why it should give reasoning before the score. Read when: you need to make a model's grading of another model trustworthy.
- [synthetic-data-for-agent-evaluation.md](synthetic-data-for-agent-evaluation.md): why real online data falls short for evaluating an agent, and the two kinds of simulation: single turn and user simulation. Read when: you need test data for an agent without real traffic or user data.
