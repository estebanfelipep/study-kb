# Checkout flow

This file covers the storefront's checkout: its steps, the flag that gates the new flow, and how a failed submit is retried.

## Steps

1. **Cart review** (`/cart`).
2. **Shipping** (`/checkout/shipping`): address and method.
3. **Payment** (`/checkout/payment`): the card fields are an iframe served by payments-gateway, so the card number never touches shop-web.
4. **Place order** (`/checkout/review`): calls `POST /orders` on orders-api (see [the contract](../cross-project/storefront-orders-contract.md)).

## The `checkout-v2` gate

The single-page checkout is behind the `checkout-v2` flag. It is read in `$SHOP_WEB_REPO/src/lib/flags.ts:12`, and defaults to `false` everywhere except dev _(verified against source, 2026-10-02)_. A preview deploy shows the old multi-page flow unless the flag is targeted at the preview's environment in the flag console (see [links.md](../links.md)). This is the most common reason a reviewer reports "the change isn't there".

## Retrying a failed submit

The **Place order** button generates one idempotency key per checkout attempt and reuses it on every retry. That makes a double-click or a network retry safe. A *new* key is generated only when the cart changes. _(source: Priya, Sep 30 checkout sync)_

Gotcha: the button stays on "Placing order…" until orders-api answers, and orders-api can take up to 10s when the PSP is slow. Don't add a client timeout shorter than that.
