# Victor Workbook Specification

This file defines the first canonical spreadsheet surface for Victor.

The workbook is not Victor's brain. It is Victor's intake and calculation engine.

## Role In The Project Hierarchy

1. The master authority remains [victor_sterling_financial_project_continuation_brief.md](/C:/Dev/Victor/victor_sterling_financial_project_continuation_brief.md).
2. The physician-finance doctrine remains in [Brains/README.md](/C:/Dev/Victor/Brains/README.md) and the five core books.
3. This workbook exists downstream from those sources as an execution surface.

## Why Spreadsheet First

The first hard problem Victor needs to solve is structured physician-financial triage:

- collect the right data
- identify missing high-stakes facts
- rank actions
- calculate basic financial pressure metrics
- feed a repeatable Victor prompt

Spreadsheet is the right first tool because it is stronger than markdown for numeric intake and more reliable than the current HTML artifact for day-to-day use.

## Workbook Design Principles

- physician-specific, not generic high-earner finance
- structured inputs before narrative advice
- missing data must stay visible
- current-law items must be flagged, not faked
- simple formulas first, complexity later
- doctrine and current-law logic must stay separate

## Workbook Tabs

### 1. `README`

Purpose:

- explain how to use the workbook
- state the source hierarchy
- warn that live tax and student-loan rules require current verification

### 2. `Intake`

Purpose:

- collect identity, training, income, household, and planning data

Core fields:

- client name
- age
- state
- filing status
- dependents
- training stage
- specialty
- expected attending income
- gross household income
- monthly take-home pay
- income stability
- near-term goals
- notes

### 3. `Cash Flow`

Purpose:

- quantify monthly pressure and liquidity

Core fields:

- monthly fixed expenses
- monthly variable expenses
- monthly debt payments
- monthly savings and investing
- cash buffer
- target emergency-fund months
- annual bonus or extra income

### 4. `Debts`

Purpose:

- separate federal loans from other debts
- expose rates, balances, and repayment risk

Columns:

- debt type
- federal loan?
- balance
- interest rate
- minimum monthly payment
- PSLF eligible?
- qualifying payments
- status and notes

### 5. `Accounts`

Purpose:

- capture retirement and savings infrastructure

Columns:

- account type
- balance
- employer match percent
- current annual contribution
- annual contribution limit
- notes

### 6. `Insurance`

Purpose:

- protect against ruin before optimization

Fields:

- own-occupation disability in force?
- employer disability coverage only?
- term life in force?
- umbrella policy?
- malpractice tail issue?
- contract review completed?
- insurance notes

### 7. `Dashboard`

Purpose:

- translate raw inputs into triage metrics and red flags

Core metrics:

- savings rate
- annual savings
- monthly core spend
- emergency-fund months
- total debt
- federal student-loan balance
- employer match available
- high-interest debt flag
- disability-protection gap
- preliminary risk-capacity score

### 8. `Action Plan`

Purpose:

- turn dashboard conditions into a ranked order of operations

Output style:

- category
- priority
- Victor verdict
- reason
- immediate next step

### 9. `Victor Prompt`

Purpose:

- generate a copyable structured prompt for running Victor with the workbook data

It should summarize:

- intake data
- key dashboard metrics
- missing data
- high-risk flags
- instruction to label assumptions rather than fake certainty

## First-Version Formula Logic

Version 1 should stay intentionally simple.

### Dashboard Logic

- `annual savings = monthly savings and investing * 12`
- `monthly core spend = fixed + variable + debt payments`
- `savings rate = annual savings / gross household income`
- `emergency-fund months = cash buffer / monthly core spend`
- `total debt = sum of debt balances`
- `federal student-loan balance = sum of balances where federal loan = Yes`
- `high-interest debt flag = any non-federal balance with rate >= 8%`
- `employer match available = any account with match > 0`

### Preliminary Risk Capacity

Use a simple tiered rule:

- `Constrained` if emergency fund is under 3 months, income is unstable, or high-interest debt exists
- `Moderate` if there is partial stability but the balance sheet is not yet strong
- `Moderate-to-High` if liquidity is solid, income is stable, and no obvious destabilizer is present

### Action Plan Logic

Use doctrine-driven triggers:

1. build starter liquidity if emergency fund is inadequate
2. eliminate high-interest debt before optimization
3. close disability-insurance gaps
4. capture employer match
5. model federal student-loan strategy before refinancing
6. continue emergency-fund build if below target
7. maximize tax-advantaged accounts where appropriate
8. invest in low-cost diversified funds after the foundation is stable

## Hard Rules

- The workbook must never recommend refinancing federal loans without first modeling PSLF and federal-plan value.
- The workbook must not pretend current tax or legal rules are embedded unless they actually are.
- The workbook must expose missing data instead of smoothing over it.
- The workbook should stay understandable enough that another agent can audit every sheet and formula.

## Near-Term Expansion Ideas

- student-loan scenario tab
- contract-review checklist tab
- attending-transition spending guardrails tab
- portfolio allocation tab
- influencer-audit tab
- source-linked notes tab for live-rule verification
