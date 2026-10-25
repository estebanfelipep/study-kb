# payments-gateway integration surface

This file covers only what Acme's shop projects call on, receive from, or embed from payments-gateway. Its internals are out of scope (black box).

## What orders-api calls

- `POST /v1/authorizations`: on order placement.
- `POST /v1/captures`: once per shipment.
- `POST /v1/authorizations/{id}/void`: on cancellation, and from the stale-authorization job.

All three need the `PAYMENTS_API_KEY` env var in orders-api _(verified against source, 2026-10-02: `$ORDERS_API_REPO/src/payments/client.ts:8`)_.

## What orders-api receives

Webhooks arrive at `POST /webhooks/payments` on orders-api. Each one is signed with `PAYMENTS_WEBHOOK_SECRET`, and a request with a bad signature is rejected with `401`. The secret is issued per environment by the Payments team. Ask in their channel (see [org/teams-and-ownership.md](../org/teams-and-ownership.md)).

## What shop-web embeds

The card-fields iframe, served from `https://pay.example.com/fields.js`. It hands shop-web a one-time card token. shop-web never sees the card number.

## Testing

The sandbox accepts card `4242 4242 4242 4242` (approves) and `4000 0000 0000 0002` (declines). _(source: Payments API reference)_
