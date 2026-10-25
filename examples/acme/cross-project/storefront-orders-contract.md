# Storefront ↔ orders API contract

This file covers what shop-web and orders-api must keep in agreement. The full API spec is `$ORDERS_API_REPO/docs/openapi.yaml`. This file records only what the spec doesn't make obvious.

## Endpoints shop-web calls

- `GET /carts/{id}` and `PATCH /carts/{id}`: the cart.
- `POST /orders`: place an order. It requires an `Idempotency-Key` header. orders-api returns the original response for a repeated key for 24h.

## Error codes the UI depends on

shop-web maps these response codes to user-facing messages in `$SHOP_WEB_REPO/src/checkout/errors.ts`. Adding a code on the API side without a mapping shows the generic "Something went wrong".

| Code | Meaning | UI message key |
| --- | --- | --- |
| `402` | Payment declined | `checkout.declined` |
| `409` | Cart changed since review | `checkout.cartChanged` |
| `422` | Address failed validation | `checkout.badAddress` |

_(verified against source on both sides, 2026-10-02)_

## Shipping a change across both repos

Ship orders-api first, in a backward-compatible way, then shop-web. orders-api deploys on merge, while shop-web waits for the weekly release, so the reverse order breaks production checkout for up to a week. _(source: Oct 8 release planning)_
