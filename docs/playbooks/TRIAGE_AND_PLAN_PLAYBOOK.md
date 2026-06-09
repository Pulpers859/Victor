# Triage And Plan Playbook

This playbook explains how Victor should interpret `Dashboard`, `Action Plan`, and `Victor Prompt`.

## `Dashboard` Sheet

The dashboard is a compression layer. Victor should treat it as useful, not sacred.

### Metric Interpretation

- `Savings rate`
  This is one of the best summary indicators in the workbook, but it still needs context. A resident and a mid-career attending should not be judged identically.
- `Annual savings`
  Useful for scale, but meaningless if built on unstable cash flow or fake precision.
- `Monthly core spend`
  This reveals whether the household actually has room to maneuver.
- `Emergency-fund months`
  This is a ruin-protection metric, not just a comfort metric.
- `Total debt`
  Large debt matters, but debt type matters more than raw size.
- `Federal student-loan balance`
  This is a warning that federal-loan options may still be valuable.
- `High-interest debt flag`
  This should move debt cleanup near the top of the queue.
- `Employer match available`
  This is a simple but high-value optimization checkpoint.
- `Disability protection gap`
  This should be treated as strategically important, not optional polish.
- `Preliminary risk capacity`
  This is only a first-pass estimate. Behavioral risk and career-stage context still matter.
- `Missing core inputs`
  This should directly lower the confidence level of any recommendation.

### Confidence Rule

Victor should mentally classify the workbook into one of three states:

1. `Usable`
   Most key inputs are present and no major ambiguity dominates the case.
2. `Partially usable`
   Enough exists for triage, but major recommendations still need clarification.
3. `Not reliable enough`
   Missing data is too material for anything beyond broad doctrine.

## `Action Plan` Sheet

### How Victor Should Use It

- Use it as the default ranked order of operations.
- Check that the ranking matches the actual facts from upstream sheets.
- Override it if upstream nuance proves the template ranking is wrong in this specific case.

### Non-Negotiable Ordering Logic

Victor should generally prefer:

1. liquidity
2. high-interest debt cleanup
3. disability and core protection
4. employer match capture
5. federal student-loan modeling
6. emergency-fund strengthening
7. tax-advantaged optimization
8. long-term portfolio refinement

### When To Override The Template

- a pending attending transition changes the cash-flow horizon
- PSLF status makes debt strategy more important than ordinary payoff logic
- contract or malpractice issues are immediately wealth-relevant
- a household is so underinsured that protection clearly outranks optimization

## `Victor Prompt` Sheet

### Purpose

This sheet exists to export the workbook state into a structured AI conversation.

### Rules For Use

- Treat it as a summary artifact, not the only source.
- If the prompt omits meaningful nuance from notes fields, Victor should go back to the raw sheets.
- If the workbook has many missing inputs, the prompt should trigger clarification rather than fake specificity.
- If current tax or loan rules matter, Victor must verify them from live official sources before making a decisive recommendation.

## Final Output Standard

When Victor turns workbook data into advice, the output should still follow the broader project structure:

1. Executive Summary
2. Current Financial Diagnosis
3. Assumptions and Missing Data
4. Risk Assessment
5. Debt / Student Loan Strategy
6. Insurance and Risk Controls
7. Retirement Account Strategy
8. Investment Policy / Portfolio Strategy
9. Tax Optimization Strategy
10. Lifestyle Inflation Controls
11. Action Timeline
12. Blunt conclusion
