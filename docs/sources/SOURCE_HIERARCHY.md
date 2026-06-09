# Victor Source Hierarchy

This project should be built with a strict authority order so Victor stays consistent over time.

## Authority Order

1. [victor_sterling_financial_project_continuation_brief.md](/C:/Dev/Victor/victor_sterling_financial_project_continuation_brief.md)
   This is the master file and final local source of truth for project intent, persona, doctrine, and continuation context.
2. [Brains/README.md](/C:/Dev/Victor/Brains/README.md) plus the five source PDFs in `Brains/`
   These are Victor's financial-literacy constitution.
3. `docs/foundation/`
   Distilled operating doctrine and reusable assistant rules.
4. `docs/intake/`
   Intake sequencing, discovery logic, and planning frameworks.
5. `docs/product/`
   Product architecture, roadmap, and build direction.
6. Product surfaces and artifacts
   HTML tools, spreadsheets, prompts, exports, audits, and future apps all sit beneath the doctrine layer.

## Usage Rule

If a derivative file contradicts the master brief or the ranked doctrine sources, the derivative file is wrong and should be corrected.

## Doctrine Versus Live Rules

Use the books and foundation docs for:

- timeless principles
- risk framing
- debt philosophy
- investing doctrine
- behavioral guardrails

Use live authoritative sources for:

- IRS thresholds and contribution limits
- Department of Education / Federal Student Aid rules
- state tax rules
- legal and contract specifics
- plan-specific retirement documents

## Practical Build Rule

Before building a new prompt, UI surface, spreadsheet, or workflow, first answer:

1. Which source file authorizes this?
2. Is this timeless doctrine or live-rule logic?
3. If it is live-rule logic, where will it be verified?
