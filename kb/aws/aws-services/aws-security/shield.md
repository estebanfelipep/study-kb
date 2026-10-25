# AWS Shield

This file covers Shield: DDoS mitigation, Standard and Advanced.

## What it is

Shield is a **DDoS mitigation** service that protects applications on AWS from **volumetric attacks**. The course lists it under **data and network security**.

## Characteristics

- **Shield Standard:** **free and automatic** for every customer. Protects against common layer 3 and 4 attacks (SYN floods, UDP reflection) _(added)_.
- **Shield Advanced:** paid. Adds layer 7 protection with [WAF](waf.md), a **24/7 response team**, cost protection against scaling charges caused by an attack, and attack reports _(added)_.

## Example

_(added)_ An attacker floods a public dashboard's CloudFront distribution with traffic. Shield Standard absorbs the network-level flood automatically. With Shield Advanced, the response team would also help write WAF rules against the application-level part of the attack, and AWS would credit the extra scaling cost.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Shield with WAF, security groups and Network Firewall: Shield stops DDoS, WAF stops layer 7 exploits, security groups and NACLs stop unwanted ports and IPs.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): Shield is a course service for data and network security, and protects the API Gateway entry point in the example secured pipeline.
- [waf.md](waf.md): Shield Advanced adds layer 7 DDoS protection by using WAF rules, which its response team helps write during an attack.
