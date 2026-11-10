# LLM judge

This file covers the LLM judge, a second model call that grades a feature's output against a rubric, and what makes its scores usable.

## Sources

- [Claude Certified Developer: Foundations (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations): Anthropic's learning path. This file comes from its "Evals and judges" section, the same section as [design-document.md](../design-document.md).

## What it is

A **judge** is a second model call guided by a clear rubric. What makes it usable is asking it to provide:

- strengths
- weaknesses
- reasoning

alongside the score, rather than returning the score alone.

The same mechanism is called an **autorater** in the [hill-climb lifecycle](hill-climb-lifecycle.md): an automated system, typically a foundation model itself, that evaluates, scores or critiques another application's output.

## Score alone versus reasoning first

| Judge asked for | Result |
|---|---|
| The score alone | Models drift toward a safe middle number, usually around six, regardless of the output's actual quality |
| Reasoning first, then the score | The score is anchored to something specific |

## Related

- [rubric-design.md](rubric-design.md): how to write the clear rubric the judge is guided by (graduated scales, operational definitions, concrete anchors), and how to check a judge against human ratings before relying on it.
- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): the autorater there is this mechanism, scaled up from rubrics that human annotators validated, and kept calibrated by weekly human audits in production.
- [design-document.md](../design-document.md): its success criteria say what the feature must produce, which is what the judge's rubric grades against.
- [agent-orchestration.md](../agent-orchestration.md): the evaluator-optimizer pattern uses an LLM to evaluate another LLM's output in a loop, the same mechanism as a judge, here used to grade a feature instead of to refine one response.
- [genai-poc.md](../genai-poc.md): the PoC's model-based evaluation type is this mechanism, and a calibrated judge is one way to run it.
