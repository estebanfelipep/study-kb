# Acme Shop KB — index

> **This is a fictional example** of a KB built from the blueprint. Acme, its repos, people, and URLs are all made up. Its purpose is to show what good entries look like. `kb-init` deletes `examples/`.

Start here. This file is the map of the KB's **topics**: the subjects people ask about, each of which may span several repos. To answer a question, read only as deep as you need to:

1. Find the topic, or topics, the question is about.
2. Open the files that topic lists. They may sit in different folders.
3. For more context, read the index of the folder a file sits in (`<folder>/<folder>.md`). It lists that file's neighbors.

## How the projects fit together

- The storefront calls the orders service for carts, orders, and checkout.
- The orders service owns orders. It calls the Payments team's gateway to authorize and capture payments, and receives that gateway's webhooks.
- The gateway belongs to the Payments team. This KB documents it as a black box.

## Topics

- **Checkout**: the steps a shopper goes through, the `checkout-v2` flag that gates the new flow, retrying a failed submit, and the API contract behind it. Read when: changing or testing checkout, debugging a double-submit or a stuck "Placing order…" button, or adding an error state.
  - [checkout-flow.md](shop-web/checkout-flow.md)
  - [storefront-orders-contract.md](cross-project/storefront-orders-contract.md)
- **Orders and payments**: order states, when a card is authorized and captured, the stale-authorization job, the gateway's endpoints and webhooks, and the sandbox test cards. Read when: an order is stuck, a customer was charged unexpectedly, a webhook isn't arriving, or you're testing payments end to end.
  - [order-lifecycle.md](orders-api/order-lifecycle.md)
  - [integration.md](payments-gateway/integration.md)
- **Shipping changes across repos**: which repo ships first, and why. Read when: a change needs PRs in both the storefront and the orders service.
  - [storefront-orders-contract.md](cross-project/storefront-orders-contract.md), under "Shipping a change across both repos"
- **Ownership and getting help**: which team owns each repo, and how to reach Payments for secrets, sandbox keys, or incidents. Read when: you need an owner, a reviewer, a secret issued, or to escalate.
  - [teams-and-ownership.md](org/teams-and-ownership.md)

## Repos

| Repo | What it is | Depth | Variable |
| --- | --- | --- | --- |
| [shop-web](shop-web/shop-web.md) | The Next.js storefront: product pages, cart, checkout UI. | full | `$SHOP_WEB_REPO` |
| [orders-api](orders-api/orders-api.md) | The orders service: carts, orders, payment orchestration. | full | `$ORDERS_API_REPO` |
| [payments-gateway](payments-gateway/payments-gateway.md) | The Payments team's gateway in front of the PSP. | black box | `$PAYMENTS_GATEWAY_REPO` |

## Reference

- [context.md](context.md): the glossary (PSP, auth/capture, idempotency key, …). Read when: a term, acronym, or codename is unfamiliar.
- [links.md](links.md): every external link in the KB. Read when: you need a dashboard, console, doc, or repo URL.
- [How the KB is run](../../AGENTS.md): in a real KB, this is `AGENTS.md` at the repo root.
