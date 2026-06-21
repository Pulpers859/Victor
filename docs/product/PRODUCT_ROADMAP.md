# Victor Product Roadmap

Victor is still at the foundation stage. The next work should be sequenced so doctrine stays stable before UI complexity expands.

## Phase 1: Foundation

- preserve the master brief as the top-level source of truth
- map and rank the doctrine sources
- create durable handoff and repo standards
- define Victor's operating constitution
- define the physician discovery framework

## Phase 2: Structured Knowledge System

- convert doctrine into reusable markdown playbooks
- create dedicated modules for:
  - student loans
  - disability insurance
  - retirement accounts
  - index investing
  - attending-transition lifestyle controls
  - advisor and influencer audits
- restore or recreate missing prior artifacts only if still useful

## Phase 3: Primary User Workflow

Choose the first real operating surface:

- spreadsheet-first
- markdown-first
- web app
- hybrid

Selection criteria:

- works reliably on the user's devices
- handles structured intake cleanly
- does not depend on fragile runtime behavior
- makes current-law verification possible where needed

## Phase 4: Live Intelligence Layer

- add current-law verification rules for taxes and student loans
- separate timeless doctrine from live, date-sensitive logic
- define which recommendations require official-source confirmation

### Started: dated rules pack (Tier 1 + 2)

The HTML triage console now carries a versioned, sourced `RULES` object
(contribution limits, catch-ups, HSA tiers, Roth phase-outs). Each value has a
tax year, an `asOf` review date, and a source URL. The console:

- shows a staleness banner whenever the figures are unverified, off-year, or
  older than ~10 months;
- computes deterministic tax-advantaged-space and Roth-phase-out triage from
  those figures (no LLM needed); and
- injects the dated figures into the generated AI prompt so the model is
  anchored to real numbers instead of guessing.

Maintenance contract: confirm each value against its official source, update
the value, set `verified:true`, and bump `asOf`/`taxYear` (IRS publishes most
limits each fall). The embedded figures were verified for **tax year 2026** on
2026-06-21 against official IRS sources (Notice / newsroom COLA release and
Rev. Proc. 2025-19 for HSA).

### Implemented: Tier 3 freshness automation

- `scripts/check_rules_freshness.py` parses the embedded `RULES` object and
  flags staleness when the pack is unverified, off-year, older than ~10 months,
  or when a cited source URL has rotted. It edits no figures.
- `.github/workflows/rules-freshness.yml` runs that check monthly (and on
  demand) and opens/updates a single tracking issue when attention is needed,
  closing it automatically once the figures read current. A human still reads
  the official source and applies the value change on `main`.
- Deliberately *not* automated: scraping IRS pages for exact dollar amounts.
  That is brittle and false-positive-prone; the date reminder plus link check
  is what reliably keeps the numbers honest.
- Requires GitHub Actions to be enabled for the repository. Scheduled runs
  fire from the default branch (`main`).

## Phase 5: Assistant Experience

- build Victor's response templates
- add source-aware reasoning guardrails
- add influencer-audit workflows
- add user-specific planning outputs and tracking

## Immediate Next Best Steps

1. Decide Victor's primary first product surface.
2. Recreate the missing physician-finance source file if it cannot be recovered elsewhere.
3. Build one canonical physician intake and action-plan workflow from the doctrine already in the repo.
