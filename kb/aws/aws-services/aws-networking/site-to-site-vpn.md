# AWS Site-to-Site VPN

This file covers AWS Site-to-Site VPN: an encrypted connection between an on-premises network and AWS over the public internet.

## What it is

AWS Site-to-Site VPN creates a **secure, encrypted tunnel over the public internet** between an on-premises network and the AWS Cloud. In a data pipeline it protects data **in transit** from an on-premises data center to AWS.

## Characteristics

- Needs a gateway at each end:

  ```
  on-premises network                        AWS
  ┌──────────────────┐   encrypted tunnel   ┌───────────────────┐
  │ customer gateway │ ═══════════════════► │ virtual private   │
  │ (your device)    │   public internet    │ gateway (on VPC)  │
  └──────────────────┘                      └───────────────────┘
  ```

  | Side        | Piece                                          |
  | ----------- | ---------------------------------------------- |
  | AWS         | A virtual private gateway, attached to the VPC |
  | On premises | A customer gateway                             |

- Runs over the **public internet**, so no dedicated line is needed.
- Covers **encryption in transit** for data leaving the data center.

## Example

Example Corp sets up a Site-to-Site VPN so that DMS (replicating its on-premises MySQL database) and the DataSync agent (copying files from its NAS) send data to AWS through an encrypted tunnel. See [example-corp-ingest-on-aws.md](../../aws-data-engineering/aws-data-pipeline/example-corp-ingest-on-aws.md).

## Related

- [vpc.md](vpc.md): the VPN ends at a virtual private gateway attached to a VPC, which connects the on-premises network to the VPC's private subnets.
- [dms.md](../aws-databases/dms.md): DMS replicates an on-premises database to AWS through the VPN tunnel.
- [datasync.md](../aws-migration-and-transfer/datasync.md): the on-premises DataSync agent copies files to AWS through the VPN tunnel.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): the VPN provides encryption in transit between the data center and AWS, part of data and network security.
- [example-corp-ingest-on-aws.md](../../aws-data-engineering/aws-data-pipeline/example-corp-ingest-on-aws.md): Example Corp's on-premises MySQL data and NAS files reach AWS through a Site-to-Site VPN.
