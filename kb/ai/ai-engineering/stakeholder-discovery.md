# Stakeholder discovery

This file covers how to run a discovery call with a stakeholder: turning what they say in business terms into requirements, assumptions and constraints that a design can follow.

## Sources

- [Stakeholder Engagement, Lifecycle & GTM (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/stakeholder-engagement-lifecycle-gtm/486650/scorm/xdrwlkyjtpf): the discovery lesson, from the Claude Certified Architect – Professional learning path.

## What it is

Evaluating the architecture pattern, the deployment platform and the control posture tells you how to build. Discovery tells you whether you are solving the right problem. A stakeholder describes the problem in business terms, so the engineer's job is to listen to the goal, find the constraints hidden inside the description, and leave the call with a written record the design can follow.

A discovery call is a **structured elicitation, not a conversation.**

## Listen, translate, write down

```
  Business goal         Requirements,             Written record
  in plain words        assumptions,              the design follows
  (what they want)      open constraints
                        (what the design
                         must support)
 +--------------+      +----------------+      +------------------+
 |  1. LISTEN   | ---> | 2. TRANSLATE   | ---> | 3. WRITE DOWN    |
 +--------------+      +----------------+      +------------------+
  Hear the meaning      See what to build,      Record it before the
  behind the word       what to confirm,        conversation moves
                        what could block        on
```

The three steps work as a filter. The artifacts the design depends on are established here, so without the filter the design inherits your assumptions.

| Step | What you do | Why |
|---|---|---|
| 1. Listen | Listen to the business goal in plain language and pay attention to the meaning behind the word. Stakeholders usually describe the outcome they want but not the constraint you need to design for | The constraint is hidden inside the description |
| 2. Translate | Turn the goal into requirements, assumptions and unresolved constraints | Shows what the design must support, what still needs confirmation, and what could block the solution later |
| 3. Write down | Write those items down before the conversation moves on. The design needs a clear record to follow | Without the record, the design inherits your assumptions. The mismatch may not be revealed until much later, when changing trajectory is slower, harder and more expensive |

## The core move: a stated preference hides a constraint

Translation is the most important skill in discovery. Stakeholders speak in **preferences**. Design decisions are made against **constraints**.

Say a stakeholder says, "We want this to feel seamless." If you write down "seamless" as the requirement, you have not learned enough to design anything yet: you only have the stakeholder's summary of the experience they want. The real work starts with the next question: *what would make it feel not seamless?* That is where the hidden constraints begin to appear:

- Maybe the user should never wait more than a second or two for the next step.
- Maybe they should not have to re-enter information that already exists upstream.
- Maybe exceptions should move quietly to a human reviewer instead of exposing a technical error.
- Maybe the workflow must stay inside one application, so the user never has to jump between tools.

Each answer sharpens the design. The exchange transforms "seamless" into requirements the architecture must support: a latency target, an integration requirement, a handoff rule and a safe failure path. The stakeholder names the outcome in business language, and you turn it into something the system can build and be measured against.

```
  "We want this to feel seamless."        <- preference (top level)
        |
        |  what would make it feel not seamless?
        v
  +-- waits longer than a second or two ------> latency target
  +-- re-enters data that exists upstream ----> integration requirement
  +-- exceptions show a technical error ------> handoff rule + safe
  |                                              failure path
  +-- has to jump between tools --------------> one-application rule

  (the constraints sit underneath the preference)
```

The preference sits on the top level, and the constraint sits underneath it. An experience word such as *seamless, easy, fast, simple* or *intuitive* is a signal that more discovery is needed. Ask:

- What would break that experience?
- What must the user never notice?
- What has to happen behind the scenes?
- What must still be true when something goes wrong?

Those answers are what belong in the design record. A **testable, bounded constraint** is what the design can be built against. A stakeholder preference tells you where to investigate, while the follow-up questions produce the constraint itself.

## Four questions turn discovery into requirements

Discovery works best when you force a vague stakeholder statement into four buckets. A statement like "we want this to feel seamless" is not yet something you can design against, because it usually hides one or more specific answers.

| # | Question | What it covers | Where it shows up |
|---|---|---|---|
| 1 | What the system **must do** | Capabilities the deployment must deliver, as business outcomes rather than features | "Read the form and route it" |
| 2 | What the system **must not do** | Boundaries, prohibited actions, and cases that must route to a human | "Clinicians will review the output anyway" |
| 3 | What the system **must cost** | The budget constraint, in terms the stakeholder controls | "Feel seamless" (latency) |
| 4 | What the system **must prove** | The evidence the deployment must be able to produce | "We are in healthcare, so be careful with data" |

### 1. What the system must do

The capabilities the deployment must deliver, expressed as **business outcomes rather than features**.

- This is where you separate the work **Claude owns** from the work that **remains with an existing system or a human**.
- In the form example, Claude owns reading the form, and the existing rule engine keeps the routing. The split only becomes visible when you ask who owns each step.

### 2. What the system must not do

The **boundaries, prohibited actions, and cases that must route to a human.**

- Stakeholders rarely volunteer these, so you must ask for them explicitly.
- In the clinician example, the answer is that output must never become part of a record with legal, financial or clinical consequence without a licensed human authorizing it. That becomes a mandatory checkpoint.

### 3. What the system must cost

The **budget constraint**, expressed in terms the stakeholder controls. Take all three into account:

- A **latency target**, such as the p95 target behind "seamless".
- A **per-interaction cost ceiling**.
- A **volume forecast**.

These become crucial design constraints. [design-document-and-llm-judge.md](design-document-and-llm-judge.md) sets the same ceilings in its cost and latency budget, before the architecture is chosen.

### 4. What the system must prove

The **evidence the deployment must be able to produce**, something of value to whoever audits or reviews it.

- In regulated workflows, **proof obligations are part of the requirement set.**
- Identifying them in discovery is far cheaper than during a legal review weeks later.
- In the healthcare example, the audit trail and data-handling evidence are a core requirement from day one.

### Back to "seamless"

"Seamless" may really mean a latency budget the user should not notice (question 3), a handoff that should not interrupt the flow (question 2), or a failure state that must not expose system internals (question 2 again). Once you discover those answers, you have requirements the team can design for, test and defend.

## The output: a translation table

Each item found in discovery becomes **one row**. A row holds the stakeholder statement as said, the constraint it implies, the architectural decision that constraint forces, and the assumption to document when the constraint is not yet confirmed. One row per item keeps the reasoning intact from discovery into design, and keeps assumptions in view.

| Stakeholder statement | Implied constraint | Required architectural decision | Assumption to document |
|---|---|---|---|
| "We want this to feel seamless." | The experience stays inside an agreed latency budget. Failures must not expose system internals or break the flow | Set a p95 latency target as a design constraint, then design a graceful, internal-safe failure state | Assumes "seamless" means perceived responsiveness and continuity of flow. Confirm understanding |
| "It just needs to read the form and route it." | Routing may be a deterministic business rule | Keep the routing decision in the rule engine. Claude extracts, and the system routes | Assumes the routing logic is owned and maintained outside the model. Confirm owner |
| "Clinicians will review the output anyway." | A licensed human must authorize output before it becomes part of a record with legal, financial or clinical consequence | Build a human-in-the-loop authorization step as a mandatory checkpoint | Assumes review is an architectural gate. Confirm authority and timing |
| "We are in healthcare, so be careful with data." | The workflow likely carries a proof obligation under a health-privacy regime | Treat audit-trail and data-handling evidence as a core requirement from day one | Assumes a covered workflow with a formal obligation. Confirm scope with compliance |

## Cost, complexity, risk

| | |
|---|---|
| **Cost** | A call long enough to find the real constraints is far cheaper than redesigning after a hidden constraint appears in legal or compliance review |
| **Complexity** | The four question categories add structure. Translating preferences into constraints in real time takes deliberate practice |
| **Risk** | The expensive failure is the unstated constraint that survives testing and becomes a production review blocker, when changing the design costs the most |

## Related

- [design-document-and-llm-judge.md](design-document-and-llm-judge.md): the design document is where discovery's output lands. The cost and latency budget comes from the "must cost" answers, the trust boundary from "must not do", and the translation table is the record that feeds it before anything is built.
- [genai-poc.md](genai-poc.md): the PoC's scoping and requirements analysis (accuracy, latency, cost targets) need the constraints that discovery uncovers. Discovery sets them from the stakeholder's words, the PoC then tests the model against them.
- [agent-orchestration.md](agent-orchestration.md): the "keep routing in the rule engine, Claude extracts" row is the workflow side of workflows vs agents: a deterministic business rule belongs in code the system controls, not in the model's judgment.
- [data-discovery.md](../../data-engineering/data-discovery.md): the data-side counterpart. That file finds and understands an organization's data sources. This one elicits the stakeholder's constraints before designing the AI solution.
