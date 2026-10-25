# Data security, governance and monitoring

This file covers security vs governance, the CIA triad, the five security areas of a data analytics system, security best practices, and what and how to monitor.

## Why security matters

Security in data analytics workflows **cannot be overstated**. A breach or compromise can lead to **data theft**, **financial loss**, **damage to reputation** and **regulatory penalties**.

## Security vs governance

|  | **Security** | **Governance** |
| --- | --- | --- |
| Definition | Measures that protect data from **unauthorized access, breaches or attacks** | The **policies, procedures and processes** that ensure the proper **management, quality and use** of data |
| Involves | Safeguarding **confidentiality, integrity and availability** | Defining **roles, responsibilities and decision-making processes** for data |
| Question it answers _(added)_ | "Can only the right people reach this data, and is it safe?" | "Who decides what this data is, who may use it, and how?" |

The **entire data analytics system depends on data being secured** and accessible only by authorized users.

### The CIA triad _(added)_

|  | Meaning | Example control |
| --- | --- | --- |
| **Confidentiality** | Only authorized people can read the data | Access control, encryption |
| **Integrity** | Data isn't altered without authorization | Access controls, versioning, audit logs |
| **Availability** | Authorized users can reach the data when needed | Durable storage, backups, redundancy |

## The five security areas

| Area | What it means |
| --- | --- |
| **Access management** | Only authorized users and applications can reach analytics resources and data, with **granular permissions per user or group using policies** |
| **Regulatory compliance** | Regulations like **GDPR** and **HIPAA** require secure data management and privacy best practices. Non-compliance means **heavy fines**. Managed services help **automate compliance controls and auditing** |
| **Sensitive data protection** | Large volumes of sensitive data (**PII, financial records, health records**) must be protected from unauthorized access, theft and leakage, using **encryption, masking, access management and data loss prevention** |
| **Data and network security** | **Security groups, network ACLs and firewalls** restrict network access to compute and storage. **Encryption at rest** adds protection |
| **Data auditability** | Track the **origin, transformation and flow** of data from source to target: where it came from, how it was processed, and who and what can access it |

The AWS services for each area are in [security-and-monitoring-on-aws.md](../aws/aws-data-engineering/security-and-monitoring-on-aws.md).

## Security best practices

| Practice | What it means |
| --- | --- |
| **Implement robust access control** | Roles and policies control who can access which resources |
| **Encrypt data at rest and in transit** | Managed keys for data at rest; **HTTPS/TLS** for data in transit between services |
| **Use data masking** | Masking and **anonymization** protect PII while still **allowing analytics** |
| **Use network isolation** | Private networks and network ACLs keep resources off the public internet |
| **Understand applicable laws** | Follow **industry and geographic** compliance laws and make the architecture conform |
| **Classify data** | Create **classes by sensitivity** and apply controls per class |
| **Plan for disaster recovery** | Recovery plans, **backups and high availability** (redundancy) |
| **Define and implement data governance** | Comprehensive, flexible and robust **governance policies** |

## Why monitoring matters

Monitoring keeps data analytics workflows **reliable, available and performant**.

## What to monitor

| Aspect | What to watch |
| --- | --- |
| **Resources** | Instances, databases, data stores. Metrics: **CPU, memory, network traffic, disk I/O**, to find **performance bottlenecks** |
| **Analytics jobs** | ETL and ELT jobs. Metrics: **run time, errors, records processed**. Job **status** helps troubleshooting |
| **Data pipelines** | Orchestration services. Metrics show **pipeline health and bottlenecks** |
| **Data access** | **Permissions and access logs**, for security and data governance |

## Monitoring best practices

| Practice | What it means | Example _(added)_ |
| --- | --- | --- |
| **Test and validate analytics jobs** | **Test deployments before production** to validate performance and accuracy | Run the new job version on a sample in a dev environment and compare row counts with the old version |
| **Monitor key metrics at each stage** | ETL **success and failure rates**, model **training times**, **number of predictions** | Track records in vs records out at each stage to catch silent data loss |
| **Set up alerts for critical failures** | **Notify the right teams** so they troubleshoot in time | A job failure event → notification → the on-call channel |
| **Integrate monitoring with visualization tools** | Dashboards give a **single view** of system health | One dashboard for the full pipeline |
| **Periodically review metrics** | Find **inefficiencies** and **optimize** over time from usage patterns | A monthly review finds a job over-provisioned at 20 workers that runs fine with 5 |

## Related

- [data-personas.md](data-personas.md): the data security officer is the persona who defines these rules and makes sure every role follows them. Their interests (PII protection, fine-grained access control, data masking) match the sensitive data protection and access management areas here.
- [modern-data-architecture.md](modern-data-architecture.md): security and governance aren't a pipeline stage. They run across all five stages, and the architecture's goal of end-to-end governance is what this file's practices deliver.
