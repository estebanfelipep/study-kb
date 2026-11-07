# Amazon Nova Forge

This file covers Amazon Nova Forge, the AWS service for building custom frontier models on Amazon's Nova technology.

## What it is

Nova Forge enables building custom frontier models with Amazon's Nova technology, providing infrastructure and tools to create large language models from scratch. It serves organizations needing highly specialized AI capabilities beyond adapting existing models.

## Characteristics

- Supports models up to 1 trillion parameters, with flexible deployment.
- Doesn't need the model's weights: AWS holds the Nova checkpoints.
- Starts from an early, middle or late Nova checkpoint (pre-training, mid-training or post-training).
- Mixes your data with Amazon's curated data. Mixing it in at an earlier stage is why Nova Forge forgets less: the domain becomes part of the model's foundation instead of a layer on top.
- Cost and effort are high, aimed at large organizations.

## Related

- [core-concepts.md](../../../ai/core-concepts.md): Nova Forge is compared there with Continued Pre-Training: CPT adds only your domain text on top of a finished model, while Nova Forge starts from any Nova checkpoint and mixes your data with Amazon's.
