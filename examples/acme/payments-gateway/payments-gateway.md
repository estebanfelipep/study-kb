# payments-gateway — index

- **Repo:** `$PAYMENTS_GATEWAY_REPO`. Remote: https://git.example.com/payments/payments-gateway.
- **What it is:** the Payments team's service in front of the PSP.
- **Depth:** black box, owned by the Payments team (see [org/teams-and-ownership.md](../org/teams-and-ownership.md)). Only the integration surface is recorded here. See [ADR 0003](../../../docs/adr/0003-depth-per-project.md).
- **Read this folder for:** the endpoints orders-api calls, the webhooks it receives, the card iframe shop-web embeds, and the sandbox for testing.
- **Read the Payments team's docs instead for:** anything about how the gateway works inside.

## Docs in the source repo

The KB points to these and does not copy them:

- `README.md` and the [API reference](https://payments.example.com/docs).

## Files

- [integration.md](integration.md): what orders-api calls and receives, the card iframe, webhook signing, and the sandbox test cards. Read when: changing anything in orders-api that touches payments, testing checkout end to end, or a webhook isn't arriving.
