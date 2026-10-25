# Order lifecycle

This file covers the states an order moves through, and where payment happens along the way.

```
draft → placed → paid → shipped → fulfilled
           └──────→ cancelled
```

- **draft → placed:** on `POST /orders`. orders-api asks payments-gateway for an **authorization** (see [context.md](../context.md)). A declined authorization leaves the order in `draft` and returns `402`.
- **placed → paid:** when the gateway's `payment.authorized` webhook arrives.
- **paid → shipped:** per shipment. Each shipment triggers one **capture** for its items _(verified against source, 2026-10-02: `$ORDERS_API_REPO/src/orders/ship.ts:41`)_. The reason is recorded in the repo's `docs/adr/0004-capture-on-ship.md`.
- **any → cancelled:** voids the remaining authorization.

## Stale authorizations

Authorizations expire at the PSP after 7 days. A nightly job (`$ORDERS_API_REPO/src/jobs/void-stale-auths.ts`) voids any `paid` order older than 6 days that hasn't shipped, and moves it to `cancelled`. Support sees these as "cancelled — payment expired". _(source: Oct 3 incident review)_
