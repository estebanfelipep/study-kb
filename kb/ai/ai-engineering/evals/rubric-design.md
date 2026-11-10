# Rubric design

This file covers how to write a rubric for evaluating subjective generative AI output: what a rubric is, three practices that make one usable, and when to use a fixed versus an adaptive rubric.

## What it is

Useful evaluation of a subjective task needs a **rubric**. In agentic and generative systems, a rubric is a set of guidelines that defines a high-quality output when many valid outputs exist. It is a structured task for evaluating open-ended outputs.

A rubric is first validated by human annotators, then scaled up with **autoraters**: automated systems, typically a foundation model itself, that evaluate, score or critique the outputs of another generative AI application. Before scaling, compare the autorater's outputs with human ratings and test that it applies the rubric consistently.

## Three practices

### Graduated scales versus binary checks

Avoid simple pass/fail checks. A binary scale is too rigid for a subjective task such as helpfulness or tone, and it forces annotators to treat a minor typo with the same severity as a dangerous fabrication.

| Design | What it is |
|---|---|
| Bad | A binary pass/fail checkbox for **Helpfulness** |
| Better | A graduated scale, with a distinct criteria definition for each intermediate rating level |
| Best | A graduated scale with labels customized to the specific rubric dimension |

### Clear operational definitions versus subjective vibes

Define precisely what counts as good and bad, and name the exact information that must be present.

| Bad definition | Good definition |
|---|---|
| "The response should be polite and not sound robotic." | "The response must address the user by name, use active voice, and avoid templates like 'As an AI...'" |
| "Ensure the summary is high quality." | "The summary must include the customer's main issue, the transaction date, and the resolution." |
| "The response should not be too long or wordy." | "The response must contain fewer than three sentences and repeat no facts." |

### Concrete anchors versus abstract instructions

Don't leave the scale definitions abstract. Give an actual model output example for each rating level. The examples act as reference anchors for annotators and reduce subjective interpretation.

| Design | What it is |
|---|---|
| Bad | Defining Rating 5 only as "Strongly agree" with the statement "The response is excellent and helpful." |
| Good | Defining Rating 5 as "The response successfully resolves the user's issue," with a short sample transcript of a model resolving a return request |

## Fixed versus adaptive rubrics

| | Fixed rubric | Adaptive rubric |
|---|---|---|
| Best use case | Systems with limited scope that need very high output quality | Open-ended systems, creative generation, malfunction analysis |
| Primary advantage | High auditability, consistent longitudinal metrics, high quality, works best with autoraters | Infinite task flexibility, customized criteria, easy scaling of analysis of system internals |
| Core risk | Rigid, can't scale to an extremely wide variety of input tasks | Lower-quality rubrics, less useful for aggregate analysis, unpredictable rubrics |

## Related

- [design-document.md](../design-document.md): a judge is a model call guided by a clear rubric. This file is how to write that rubric, and that one is how to get the judge to reason before it scores.
- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): the lifecycle builds a helpfulness rubric in the Evaluate stage and returns to it in Optimize when satisfaction comes in low.
- [evaluation-plan.md](evaluation-plan.md): its roadmap places structured rubrics at step 5 and autorater calibration at step 6.
- [agent-orchestration.md](../agent-orchestration.md): the autorater plays the evaluator role of the evaluator-optimizer pattern, scoring output against a rubric instead of feeding a refinement loop.
