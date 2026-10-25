# orders-api — index

- **Repo:** `$ORDERS_API_REPO`. Remote: https://git.example.com/acme/orders-api.
- **What it is:** the service that owns carts and orders, and drives payments through payments-gateway.
- **Depth:** full. See [ADR 0003](../../../docs/adr/0003-depth-per-project.md).
- **Read this folder for:** order states and transitions, when payment is authorized and captured, background jobs, and the Postgres schema.
- **Read `cross-project/` instead for:** the API shop-web calls, and how to ship a checkout change that spans both repos.

## Docs in the source repo

The KB points to these and does not copy them:

- `README.md`: running it locally against a seeded DB.
- `docs/openapi.yaml`: the public API spec. The contract file in `cross-project/` points to it.
- `docs/adr/0004-capture-on-ship.md`: why payment is captured at shipment, not at order time.

## Files

- [order-lifecycle.md](order-lifecycle.md): order states, which transitions call payments-gateway, and the nightly job that voids stale authorizations. Read when: an order is stuck in a state, a customer was charged unexpectedly, or you're adding a state.
- Payments webhooks and endpoints are recorded on the payments-gateway side: see [payments-gateway/integration.md](../payments-gateway/integration.md).
- The storefront ↔ orders contract is cross-repo: see [cross-project/storefront-orders-contract.md](../cross-project/storefront-orders-contract.md).
