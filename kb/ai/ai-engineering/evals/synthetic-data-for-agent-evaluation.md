# Synthetic data for agent evaluation

This file covers why evaluating an agent needs synthetic data alongside real online data, and the two ways to simulate it: single-turn generation and user simulation.

## Why real online data isn't enough

Online data is essential for a comprehensive evaluation, but capturing real online data alone to fill that need falls short:

- **Privacy and compliance barriers:** there are policies around using real user data.
- **Cold start scenarios:** a new system has no real data yet.
- **Absent edge cases:** the real data doesn't cover them.
- **Safety, security and adversarial testing:** real online data alone doesn't cover these either.

Testing an agent with **synthetic data** fills these gaps.

## Two kinds of data simulation

| Kind | How it works |
|---|---|
| Single turn | Prompt a model to generate prompts, then feed them into your system one at a time |
| User simulation | Direct an AI to impersonate a user, and run it against the actual system or agent you are building |

```
  single turn: each generated prompt is sent on its own

   generator model --> prompt 1 --> system under test --> response 1
                   --> prompt 2 --> system under test --> response 2

  user simulation: two agents talk to each other

   simulated user --- message ---> system under test
                  <--- reply ----
                  --- message ---> (the real agent being built)
                  <--- reply ----
```

The test input is itself an agent: it is given instructions to impersonate a user, then used against the actual agent under evaluation.

## Keeping simulated data trustworthy

In the refund chatbot example, the team:

- builds the data simulator from golden historical data;
- validates the simulated sessions for realism;
- has humans partly review the simulated data to ensure quality;
- keeps monitoring the simulator against manual and automated correctness checks.

## Related

- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): the data simulator is built in the Evaluate stage from golden data, and the baseline test in Optimize runs on simulated data.
- [evaluation-plan.md](evaluation-plan.md): simulating data is step 8 of the roadmap, used to fill gaps in the evaluation datasets, especially online data gaps.
- [core-concepts.md](core-concepts.md): a simulated user conversation with the agent is a session, built from one trace per turn.
