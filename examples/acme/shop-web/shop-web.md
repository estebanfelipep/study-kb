# shop-web — index

- **Repo:** `$SHOP_WEB_REPO`. Remote: https://git.example.com/acme/shop-web.
- **What it is:** Acme's storefront. A Next.js app with product pages, cart, and checkout.
- **Depth:** full. See [ADR 0003](../../../docs/adr/0003-depth-per-project.md).
- **Read this folder for:** the checkout UI and its steps, the `checkout-v2` flag, client-side retries, and preview deploys.
- **Read `cross-project/` instead for:** the endpoints it calls on orders-api, and the payload shapes and headers they share.

## Docs in the source repo

The KB points to these and does not copy them:

- `README.md`: local setup and scripts.
- `docs/adr/`: the frontend decisions.
- `AGENTS.md`: the repo's own agent rules.

## Files

- [checkout-flow.md](checkout-flow.md): the checkout steps, the `checkout-v2` flag gate, and how a submit failure is retried. Read when: changing checkout, testing it on a preview deploy, or debugging a double-submit or a stuck "Placing order…" button.
- The storefront ↔ orders contract is cross-repo: see [cross-project/storefront-orders-contract.md](../cross-project/storefront-orders-contract.md).
