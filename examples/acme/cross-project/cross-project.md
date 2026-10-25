# cross-project — index

This folder is for anything true of two or more of the projects at once: the contracts between them, and workflows that span repos. A contract is recorded once, here, and each affected project's index points to it.

## Files

- [storefront-orders-contract.md](storefront-orders-contract.md): the endpoints shop-web calls on orders-api, the `Idempotency-Key` header both sides rely on, error codes the UI maps to messages, and the order to ship changes in. Read when: changing either side of checkout, adding an error state, or planning a change that needs PRs in both repos.
