# Victor

Victor is an early-stage AI financial assistant designed for physicians and physician trainees.

Git policy for this repo: `main` is the only normal working branch. Do not use `dev`, feature branches, or PR flow unless the user explicitly asks for that exception.

The project is built around one non-negotiable hierarchy:

1. The master source of truth is [victor_sterling_financial_project_continuation_brief.md](/C:/Dev/Victor/victor_sterling_financial_project_continuation_brief.md).
2. The supporting constitutional knowledge base lives in [Brains/README.md](/C:/Dev/Victor/Brains/README.md) and the five physician-finance books in `Brains/`.
3. All derived architecture, roadmap, prompts, artifacts, and future product layers sit underneath those sources.

## Current Repository Shape

```text
Victor/
├── Brains/
│   ├── README.md
│   └── physician-finance source PDFs
├── AGENTS.md
├── docs/
│   ├── foundation/
│   ├── intake/
│   ├── playbooks/
│   ├── product/
│   └── sources/
├── artifacts/
├── scripts/
├── victor_sterling_financial_project_continuation_brief.md
├── victor_sterling_financial_advisor_ARTIFACT_v3.html
├── PROJECT_HANDOFF.md
└── README.md
```

## What Victor Is Supposed To Be

Victor is not a generic budgeting bot. He is meant to be a physician-specific financial strategy system:

- blunt but not sloppy
- evidence-based
- skeptical of expensive complexity
- focused on long-term after-tax, risk-adjusted wealth
- protective against disability, student-loan mistakes, lifestyle inflation, and predatory financial sales

## Current State

- The master continuation brief is present.
- The constitutional source library is present in `Brains/`.
- The repo is intentionally `main`-only for normal work. Side branches and PR flow are off-limits unless explicitly requested by the user.
- A browser-based intake/triage artifact exists in [victor_sterling_financial_advisor_ARTIFACT_v3.html](/C:/Dev/Victor/victor_sterling_financial_advisor_ARTIFACT_v3.html).
- A spreadsheet-first workflow spec lives in [VICTOR_WORKBOOK_SPEC.md](/C:/Dev/Victor/docs/product/VICTOR_WORKBOOK_SPEC.md), and the workbook can be generated from `scripts/create_victor_workbook.py`.
- A markdown interpretation layer for the workbook lives in [docs/playbooks/README.md](/C:/Dev/Victor/docs/playbooks/README.md).
- The repo foundation and internal document architecture are now in place for future product work.

## Suggested Build Order

1. Preserve and refine Victor's doctrine.
2. Convert doctrine into structured intake and decision frameworks.
3. Decide the primary product surface:
   - markdown workflow system
   - spreadsheet workflow
   - web app
   - hybrid
4. Build the first durable user flow around physician intake, triage, and action planning.
5. Add live-rule verification for tax and student-loan logic only where current law matters.
