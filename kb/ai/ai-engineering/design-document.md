# Design document

This file covers how to decide what "right" means before building an LLM feature, with a design document: success criteria, failure handling (retriable vs terminal errors, tool errors), a cost and latency budget (what to measure and the levers), and a trust boundary (prompt injection, least privilege, regulated-industry scoping).

## Sources

- [Claude Certified Developer: Foundations (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations): Anthropic's learning path. This file and the LLM judge in [rubrics-and-llm-judge.md](evals/rubrics-and-llm-judge.md) come from its "Evals and judges" section, so it reflects Claude's own guidance, unlike [genai-poc.md](genai-poc.md), which comes from an AWS course.

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

The design document sits **before** the build, next to PoC scoping. The judge, in [rubrics-and-llm-judge.md](evals/rubrics-and-llm-judge.md), is one way to run the PoC's evaluation at scale.

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

## Failure handling in detail

The document marks each production error **retriable** or **terminal**. One question sorts them: would waiting and sending the exact same request again plausibly work? If yes, it is retriable. If not, it is terminal.

| | Retriable | Terminal |
|---|---|---|
| Cause | Transient: the service was momentarily over capacity, a connection dropped, a per-minute limit was briefly exceeded | In the request itself: a malformed body, an expired key, a model name that does not exist |
| Does time fix it? | Yes, a later attempt is likely to succeed | No, every identical request fails identically until the request is fixed |
| Handling | Exponential backoff, with a cap and a retry budget, never an immediate loop that only deepens the problem | A named fallback, and a defined message for the user. Without one, an unhandled exception becomes the default behavior and one bad response takes down the whole flow |

### When a tool fails

When your code runs a tool and the tool fails, return the result to Claude with `is_error` explicitly set to `true`. Never return a silent empty result.

| Tool failure returned as | What the model can do |
|---|---|
| `is_error: true` with the error text | React: try a different approach, ask for clarification, or stop |
| A silent empty result | Nothing, it reads the empty result as data. The answer downstream is confident and wrong |

[agent-orchestration.md](agent-orchestration.md) adds the checkpoint for the same signal: an error flag, an empty result or an out-of-bounds result is a trigger for a human check, because retry logic alone won't resolve it.

## Cost and latency budget in detail

You cannot budget what you do not measure. Instrument three metrics on **every call**: token usage (input and output), latency, and error rate. With them you can see which step is expensive or slow, instead of guessing from a total monthly bill.

### The levers

| Lever | What it does |
|---|---|
| Model selection for the task | A smaller, faster model cuts cost and latency. Reserve the most capable model for the steps that need it ([claude-api-foundations.md](claude-api-foundations.md)) |
| Prompt and context size | Every input token adds to cost. Trimming context and unneeded tool output cuts per-call cost directly ([prompt-and-context-engineering.md](prompt-and-context-engineering.md)) |
| Number of tool calls | Each call adds cost and latency. A flow that makes more calls than it needs is a common, measurable source of waste that shows up once calls are instrumented |
| Streaming vs batched output | Streaming changes how latency is perceived: a reply that starts in 300 ms feels faster than the same content delivered as one block after two seconds, even with identical total generation time |
| Prompt caching | Repeated context is paid for at a fraction of the cost ([prompt-and-context-engineering.md](prompt-and-context-engineering.md)) |
| Single agent vs orchestrator-workers | Fanning out multiplies tokens (about 15x in Anthropic's reported case). Worth it only when the work truly runs in parallel ([agent-orchestration.md](agent-orchestration.md)) |

### Reliability is the floor

Cost is half of the budget, and reliability is the other half: it sets a baseline that cost must not go below. The cheapest configuration is rarely the most reliable, so tune cost within the reliability floor the document wrote down, not below it.

## Trust boundary in detail

### Prompt injection

The model reads its entire context the way you read a page: it cannot tell which sentences you wrote from those embedded in whatever it retrieved. When an agent fetches a web page, a document or a tool result, instructions hidden inside sit in the same context as your prompt, and the model may treat them as commands. That is **prompt injection**.

- **Any content someone else can write is a vector:** a document in a shared drive, a database record, an email body, or the output of a tool that itself fetched from somewhere else.
- **Trusting your own users does not help:** the injection arrives through the content the agent reads, not through the user's message.
- **Wrapping untrusted content in delimiters and telling the model to treat it as data helps, but is a soft boundary:** the content can mimic your delimiters or argue persuasively that it is an exception.

| | Jailbreak | Prompt injection |
|---|---|---|
| Tries to | Get the model to ignore its own safety constraints | Hijack your application's instructions |
| Target | The model's own safety behavior | Your application's instructions, so defend the action, not only the prompt |

Defending only the prompt, and not the action, leaves the model free to cause damage once it has been steered.

### Least privilege

A production agent acts with an identity, and that identity should carry only the permissions the task requires. Least privilege is a design principle, not a setting, because it is the control that still holds when every other defense fails. No system can rule out a steered model, so what decides how bad an incident is is how much damage a steered agent can do, and least privilege minimizes it.

### Scoping for a regulated industry

Raise these before the review stalls the project:

- **Zero data retention (ZDR):** eligibility varies by model and by platform, and is not guaranteed for every model even under an existing ZDR agreement. Newer or higher-capability models may not have confirmed ZDR status yet. When a regulated customer requires ZDR, the deployment surface must use a model confirmed ZDR-eligible at scoping time, which can constrain model or platform choice. [agent-orchestration.md](agent-orchestration.md) names one such stop: Managed Agents is ruled out under ZDR.
- **Data residency:** where the data is physically stored: which region processes the request, whether any data leaves the customer's boundary, and whether the deployment surface (the direct API or a cloud provider's hosted version) satisfies the customer's constraint.

### Security is layered

| Layer | Its job |
|---|---|
| 1. Model training and classifiers | Reduce how often an injection lands |
| 2. Treating fetched content as data | Reduce how often a landed injection is acted on |
| 3. Least privilege and locked configuration | Bound what a successful action can reach |
| 4. Hooks | Enforce those boundaries before the action occurs, and record them |
| 5. Regulated-review scoping | Make the whole arrangement understandable to the person who must sign off |

No single layer is enough. A defense that depends on one control failing closed is one bug away from an incident, while a layered defense degrades instead of collapsing when one layer is bypassed.

## Related

- [genai-poc.md](genai-poc.md): the AWS-sourced PoC method. Its success metrics (phase 3), requirements analysis, responsible AI controls (phase 4) and model-based evaluation each overlap one part of the design document or the judge, as the diagram above maps. It has no equivalent of failure handling, and it only names model-based evaluation without saying how to calibrate it, which [rubrics-and-llm-judge.md](evals/rubrics-and-llm-judge.md) does.
- [stakeholder-discovery.md](stakeholder-discovery.md): the step before this one. A discovery call's translation table supplies the design document's budget ("must cost"), trust boundary ("must not do") and proof obligations, so the document records confirmed constraints rather than assumptions.
- [bedrock-poc.md](../../aws/aws-ai-engineering/bedrock-poc.md): its least-privilege IAM and security-from-day-one steps are one way to enforce a trust boundary on AWS.
- [rubrics-and-llm-judge.md](evals/rubrics-and-llm-judge.md): the second model call (the LLM judge) that grades the feature's output against the success criteria written here, calibrated so its scores can be trusted, and how to write the rubric it grades by.
- [tool-use.md](tool-use.md): the `is_error` rule above applies to the tools that file defines, and a tool's output is one of the prompt-injection vectors listed above when the tool itself fetched from somewhere else.
- [agent-orchestration.md](agent-orchestration.md): its orchestrator-workers pattern is the 15x token multiplier in the budget, and its human-in-the-loop checkpoints are one way to enforce the trust boundary before an irreversible action.
- [hill-climb-lifecycle.md](evals/hill-climb-lifecycle.md): the trace it defines is how you find which step of a failing flow is the expensive, slow or erroring one.
- [claude-api-foundations.md](claude-api-foundations.md): the sampling it describes (same prompt, different wording each run) is why evals and judges exist, and its tier and reasoning-mode choices are what an eval decides.
- [evaluation-plan.md](evals/evaluation-plan.md): picks up where the success criteria stop. It turns organizational KPIs into system goals and metrics, then into a roadmap that builds toward calibrated autoraters, where this file stops at the single feature.
