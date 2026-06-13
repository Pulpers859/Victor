# Repo Project Handoff

## Project Identity
- Project name: `Victor`
- Project type: `AI financial assistant / mixed knowledge-system project`
- Source-of-truth repo path: `C:\Dev\Victor`
- Stale/old copies to ignore if applicable: `None known`
- Primary target for normal work if multiple surfaces exist: `Victor knowledge system and future physician-finance assistant surfaces`
- GitHub intent/status: `remote attached`
- GitHub remote: `https://github.com/Pulpers859/Victor.git`

## Repo State
- Stable branch: `main`
- Working branch: `main`
- Expected default branch for normal work: `main`
- Sync-first rule: `Before normal work, fetch from the remote first. If the working tree is clean and the active branch tracks the expected upstream, pull with --ff-only before editing. If local changes exist, fetch and reconcile instead of blindly pulling.`
- If Git is not set up yet for this project, the agent should bootstrap it before doing major feature work.
- Git branch policy: `This repository is main-only unless the user explicitly instructs otherwise. Do not create or use side branches, dev branches, feature branches, or pull-request flow by default.`

## PowerShell / Terminal Standard
- Do not globally pin every PowerShell session to this project.
- A dedicated shortcut should exist:
  - `Victor PowerShell`
- That shortcut should open directly in `C:\Dev\Victor`.
- Avoid fragile startup command strings if the path contains apostrophes or quoting hazards.

## How The Agent Should Operate
- Inspect before assuming.
- Work in `C:\Dev\Victor` as the source of truth.
- Sync from GitHub before normal work so the local repo is not stale.
- Fix root causes, not surface symptoms.
- Be honest and direct.
- Preserve the source hierarchy:
  1. `victor_sterling_financial_project_continuation_brief.md`
  2. `Brains/` constitutional sources
  3. all downstream docs, prompts, app surfaces, and artifacts
- Do not let derivative prompt files or UI artifacts outrank the master continuation brief.
- Treat physician-specific finance as the core domain, not a generic high-income-finance clone.
- Verify current tax, retirement, and student-loan rules from official sources before giving live recommendations.
- Keep normal work on `main`.
- Do not create or use side branches unless the user explicitly says to.
- Audit adjacent risks after making changes.
- Run realistic local checks before handoff.

## Architecture / Product Notes
- Main product purpose: `Build a physician-specific AI financial assistant persona named Victor that turns evidence-backed doctrine into executable guidance.`
- Key modules or directories:
  - `victor_sterling_financial_project_continuation_brief.md` = master project file
  - `Brains/` = constitutional book library
  - `docs/foundation/` = distilled operating doctrine
  - `docs/sources/` = source ranking and usage rules
  - `docs/intake/` = discovery and intake frameworks
  - `docs/product/` = product architecture and roadmap
- Known fragile areas:
  - current HTML artifact depends on JavaScript execution
  - live financial rules can go stale
  - some prior referenced artifacts are not present in this repo yet
- Important evidence/product constraints:
  - physician financial guidance must stay physician-specific
  - timeless doctrine can come from books
  - current law must be verified from live authoritative sources
- Runtime environments that matter: `markdown knowledge system now; possible spreadsheet and web-app surfaces later`

## Project-Specific Instructions For The Next Agent
```text
Project: Victor
Active repo path: C:\Dev\Victor
GitHub remote: https://github.com/Pulpers859/Victor.git
Stable branch: main
Working branch: main

Important:
- Treat C:\Dev\Victor as the source of truth.
- The master file is victor_sterling_financial_project_continuation_brief.md.
- The Brains folder is the doctrinal library immediately beneath the master file.
- All future prompts, workflows, UI surfaces, and assistant behavior should derive from those sources instead of drifting into generic personal-finance advice.
- If Git is already set up, fetch first before normal work.
- Use main as the normal working branch.
- Do not create or use side branches, dev branches, or PR flow unless the user explicitly instructs that exception.
- Before implementing live financial logic, separate timeless doctrine from current-law dependencies.
```
