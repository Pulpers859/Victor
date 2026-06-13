# Victor Agent Instructions

This file exists to make Victor's repo policy explicit for all future agents.

## Source Hierarchy

1. `victor_sterling_financial_project_continuation_brief.md`
2. `Brains/`
3. `docs/`
4. generated artifacts and product surfaces

If a downstream file conflicts with the master brief or the doctrine layer, the downstream file is wrong.

## Git Branch Policy

- `main` is the only normal working branch for this repository.
- Commits should be made directly on `main`.
- Pushes should go directly to `origin/main`.
- Do not create or use `dev`, feature branches, side branches, or pull-request workflows unless the user explicitly instructs you to do so in that session.
- Do not suggest PR flow, draft PRs, or branch promotion flow by default.

## Working Rules

- Treat `C:\Dev\Victor` as the source of truth.
- Fetch first when the repo is clean so local context is current.
- Fix root causes, not surface symptoms.
- Preserve physician-specific financial doctrine.
- Verify current live financial rules from official sources before making recommendations that depend on them.
