# Building a PoC on Amazon Bedrock

This file covers how to build a generative AI proof of concept on Amazon Bedrock: why Bedrock suits a PoC, the security to build in from day one, and a real-world healthcare example.

## Why Bedrock suits a PoC

[Bedrock](../aws-services/aws-ai/bedrock.md) gives managed foundation models behind a straightforward API, so a PoC can start with no infrastructure. Its integration options climb in complexity, and a PoC starts at the bottom:

```
 complexity
     ^
     |  Agents            multi-step tasks with tools and APIs
     |  Knowledge Bases   RAG without running a vector database
     |  Model Evaluation  compare models on your own data
     |  Inference API     prompt in, response out (start here)
     +------------------------------------------------------->
```

The vendor-neutral PoC method (scoping, model selection, performance testing, value calculation) is in [genai-poc.md](../../ai/ai-engineering/genai-poc.md). On Bedrock, the comparative evaluation step runs in **Model Evaluation**.

## Security from the start

Security is built into the PoC from the beginning, so practices are in place before production and no gaps open in the transition.

| Area | What to do on AWS |
|---|---|
| Access | [IAM](../aws-services/aws-identity/iam.md) roles and policies with **least privilege**: only the permissions the PoC needs |
| Encryption in transit | Automatic: TLS 1.2+ over HTTPS endpoints, SigV4-signed API requests, and optional AWS PrivateLink for private VPC connectivity |
| Encryption at rest | Automatic with AWS-owned keys; customer managed [KMS](../aws-services/aws-security/kms.md) keys for more control |
| Logging | [CloudTrail](../aws-services/aws-monitoring/cloudtrail.md) for API usage and security auditing; [CloudWatch](../aws-services/aws-monitoring/cloudwatch.md) for performance monitoring |

## Example: extracting medical conditions from patient notes

**Problem:** a healthcare startup needed to extract medical conditions from unstructured patient notes to improve care coordination and billing accuracy. Manual extraction took a lot of clinical staff time and was inconsistent, which hurt patient care and revenue cycle management.

**Goal of the PoC:** validate that AI extraction could match human accuracy while cutting processing time and cost.

| Step | What the team did |
|---|---|
| Model selection | Compared Claude, Jurassic and Titan models with Bedrock's Model Evaluation |
| Test dataset | 500 anonymized patient notes with ground-truth annotations from clinical experts |
| Integration | The API integration pattern (Inference API) with Claude 3.5 Sonnet |
| Prompting | Structured prompts asking for specific condition categories and a confidence score; few-shot examples for accuracy and consistency |
| Security and compliance | HIPAA-compliant handling: encryption in transit and at rest, audit logging, restricted access, and only de-identified data in testing |

```
 de-identified       structured prompt      Claude 3.5    conditions
 patient note  --->  + few-shot examples -> Sonnet   ---> + category
                                            (Bedrock)     + confidence
                                                               |
                     500 expert-annotated notes  <-- compared -+
                     (ground truth)
```

## Related

- [genai-poc.md](../../ai/ai-engineering/genai-poc.md): this file applies that vendor-neutral PoC method on Bedrock.
- [bedrock.md](../aws-services/aws-ai/bedrock.md): the service whose models, integration options, Model Evaluation and encryption this PoC uses.
- [prompt-engineering.md](../../ai/ai-engineering/prompt-engineering.md): the structured prompts and few-shot examples in the healthcare example are techniques from there.
- [iam.md](../aws-services/aws-identity/iam.md): IAM roles with least privilege control who can call Bedrock during the PoC.
- [kms.md](../aws-services/aws-security/kms.md): customer managed KMS keys replace Bedrock's default AWS-owned keys when the PoC needs control over encryption at rest.
- [cloudtrail.md](../aws-services/aws-monitoring/cloudtrail.md): CloudTrail logs every Bedrock API call for security auditing.
- [cloudwatch.md](../aws-services/aws-monitoring/cloudwatch.md): CloudWatch tracks Bedrock usage and performance during the PoC.
