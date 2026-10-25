# Glossary

This file holds the domain vocabulary shared across Acme's shop projects.

## Language

**Auth / capture**: The two steps of taking a card payment. An *authorization* reserves the funds, and a *capture* takes them. orders-api captures only when an order ships. See [orders-api/order-lifecycle.md](orders-api/order-lifecycle.md).
_Avoid:_ charge (ambiguous between the two)

**Idempotency key**: A client-generated UUID, sent as `Idempotency-Key`, that makes a retried `POST /orders` safe. See [cross-project/storefront-orders-contract.md](cross-project/storefront-orders-contract.md).

**Order (API)**: The orders-api record, from `draft` to `fulfilled`. See [orders-api/order-lifecycle.md](orders-api/order-lifecycle.md).

**Order (analytics)**: In the analytics dashboards, a *paid* order only. A `draft` order is not counted.

**PSP**: Payment service provider. The external processor behind payments-gateway. See [payments-gateway/integration.md](payments-gateway/integration.md).

## Relationships

- An **Order (API)** has exactly one payment **authorization**, and zero or more **captures** (one per shipment).
