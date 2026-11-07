# AWS AI Factories

This file covers AWS AI Factories: AI infrastructure that AWS owns and operates inside the customer's own data center.

## What it is

AWS ships, installs and operates its own AI infrastructure inside the customer's data center. "On-premises" describes where the hardware sits, not who owns and runs it.

## Characteristics

- **Split of responsibilities:**

  | The customer provides | AWS provides and operates |
  |---|---|
  | The building, floor space, power, cooling, physical security and the network uplink | The hardware: GPUs, Trainium chips, servers, storage, networking |
  | Their data, models and apps, which stay inside their own security perimeter | Patching, monitoring and replacing failed parts, and AI services such as Bedrock and SageMaker AI on top |

- **Connection to AWS:** the site stays connected to an AWS Region, but that link mostly carries management traffic (health checks, software updates, telemetry, billing). Inference and training run locally, next to the data.

  ```
    CUSTOMER DATA CENTER                      AWS REGION
   +-----------------------------------+     +-------------------+
   |  AWS-owned AI racks               |     |                   |
   |  +-----------------------------+  |     |  control plane:   |
   |  | Bedrock / SageMaker AI      |  |<--->|  monitoring,      |
   |  | GPUs / Trainium, storage    |  | mgmt|  updates, health, |
   |  +-----------------------------+  | link|  billing          |
   |        ^                          |     |                   |
   |        | local, low-latency       |     +-------------------+
   |  customer apps + data             |
   |  (data stays here)                |
   +-----------------------------------+
  ```

- **The reverse of a typical hybrid setup:** there, on-premises servers send data or workloads up to the cloud. Here, the cloud's hardware comes down to the customer.
- **When it fits:** data residency requirements, regulated industries with strict compliance needs, low-latency inference close to data sources, and enterprises wanting cloud-like AI capabilities within their own security perimeter. The data never leaves the building, and the customer still doesn't build or run their own GPU cluster.

## Related

- [bedrock.md](bedrock.md): AI Factories runs Bedrock on the AWS-owned hardware inside the customer's data center.
- [sagemaker.md](sagemaker.md): AI Factories runs SageMaker AI on the AWS-owned hardware inside the customer's data center.
- [core-concepts.md](../../../ai/core-concepts.md): AI Factories is the on-premises way to integrate a foundation model, beside Bedrock's unified API, self-hosting on SageMaker AI and direct provider APIs.
