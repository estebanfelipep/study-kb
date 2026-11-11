# Rubrics and the LLM judge

This file covers how to evaluate subjective generative AI output: how to write a rubric, three practices that make one usable, when to use a fixed versus an adaptive one, and the LLM judge, the second model call that grades output against the rubric.

## Sources

- [Claude Certified Developer: Foundations (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations): Anthropic's learning path. The LLM judge section comes from its "Evals and judges" section, the same section as [design-document.md](../design-document.md).

## What a rubric is

Useful evaluation of a subjective task needs a **rubric**. In agentic and generative systems, a rubric is a set of guidelines that defines a high-quality output when many valid outputs exist. It is a structured task for evaluating open-ended outputs.

A rubric is first validated by human annotators, then scaled up with an LLM judge (below).

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

## The LLM judge

A **judge** is a second model call guided by a clear rubric. The same mechanism is called an **autorater** in the [hill-climb lifecycle](hill-climb-lifecycle.md): an automated system, typically a foundation model itself, that evaluates, scores or critiques another application's output.

What makes a judge usable is asking it to provide strengths, weaknesses and reasoning alongside the score, rather than returning the score alone.

| Judge asked for | Result |
|---|---|
| The score alone | Models drift toward a safe middle number, usually around six, regardless of the output's actual quality |
| Reasoning first, then the score | The score is anchored to something specific |

Before scaling a judge up, compare its outputs with human ratings and test that it applies the rubric consistently.

```
  rubric (validated by humans)
        |
        v
  judge call: output + rubric --> strengths, weaknesses, reasoning,
                                  then the score
        |
        v
  compare with human ratings before scaling up
```

## Related

- [design-document.md](../design-document.md): its success criteria say what the feature must produce, which is what the rubric grades against. Its calibrated LLM judge is the same mechanism as the judge here.
- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): the lifecycle builds a helpfulness rubric in the Evaluate stage and returns to it in Optimize when satisfaction comes in low. Its autorater is the judge, scaled up from rubrics that human annotators validated and kept calibrated by weekly human audits in production.
- [evaluation-plan.md](evaluation-plan.md): its roadmap places structured rubrics at step 5 and autorater calibration at step 6.
- [agent-orchestration.md](../agent-orchestration.md): the evaluator-optimizer pattern uses an LLM to evaluate another LLM's output in a loop, the same mechanism as the judge, here used to grade a feature against a rubric instead of to refine one response.
- [genai-poc.md](../genai-poc.md): the PoC's model-based evaluation type is this mechanism, and a calibrated judge is one way to run it.
