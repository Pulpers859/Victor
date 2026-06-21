#!/usr/bin/env python3
"""Freshness check for Victor's embedded tax/contribution "rules pack".

Tier 3 of the live-intelligence plan. This does NOT auto-edit any financial
figure. It only decides whether a human needs to re-verify the numbers, and
emits a report the GitHub Action turns into (or updates) a single issue.

Two reliable signals, by design:

1. Date-based staleness  -- the thing that actually causes wrong advice.
   Stale when the rules pack is unverified, its tax year is not the current
   year, or it was last reviewed more than STALE_MONTHS ago. This is what
   reminds a maintainer every fall/new-year to confirm the new IRS limits.

2. Source link-rot       -- each figure cites an official URL; if one starts
   404ing, the citation is no longer trustworthy.

Automated value-diffing against IRS pages is intentionally NOT attempted:
scraping those pages for exact dollar amounts is brittle and produces false
positives. The date reminder is what keeps the numbers honest; a human reads
the cited source and updates the value.

Exit code is always 0 (the workflow inspects the written outputs, not the
exit status). Writes:
  - a markdown report to the path in $FRESHNESS_REPORT (default below)
  - stale=true|false and reasons to $GITHUB_OUTPUT when present
"""

from __future__ import annotations

import datetime as dt
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "victor_sterling_financial_advisor_ARTIFACT_v3.html"
REPORT_PATH = Path(os.environ.get("FRESHNESS_REPORT", ROOT / "rules_freshness_report.md"))

# Keep this in sync with rulesStale() in the HTML.
STALE_MONTHS = 10
TODAY = dt.date.today()


def parse_rules(text: str) -> dict:
    """Pull the maintained fields out of the embedded RULES object."""

    def find(pattern: str, default=None, group=1):
        m = re.search(pattern, text)
        return m.group(group) if m else default

    tax_year = find(r"taxYear\s*:\s*(\d{4})")
    as_of = find(r"asOf\s*:\s*'([0-9-]+)'")
    verified = find(r"verified\s*:\s*(true|false)")

    # Each limit: name:{value:NNN,label:'...',source:'<url-or-var>'}
    figures = []
    for m in re.finditer(
        r"(\w+)\s*:\s*\{\s*value\s*:\s*(\d+)\s*,\s*label\s*:\s*'([^']*)'\s*,\s*source\s*:\s*([A-Za-z0-9_]+|'[^']*')",
        text,
    ):
        name, value, label, source = m.groups()
        figures.append({"name": name, "value": int(value), "label": label, "source_token": source})

    # Resolve `var NAME='https://...'` aliases used as source tokens.
    aliases = dict(re.findall(r"var\s+([A-Za-z0-9_]+)\s*=\s*'(https?://[^']+)'", text))
    for f in figures:
        tok = f["source_token"]
        f["source"] = tok[1:-1] if tok.startswith("'") else aliases.get(tok, tok)

    return {
        "tax_year": int(tax_year) if tax_year else None,
        "as_of": as_of,
        "verified": verified == "true",
        "figures": figures,
    }


def months_between(d: dt.date, ref: dt.date) -> float:
    return (ref - d).days / 30.44


def date_reasons(rules: dict) -> list[str]:
    reasons = []
    if not rules["verified"]:
        reasons.append("the rules pack is flagged **UNVERIFIED**")
    if rules["tax_year"] != TODAY.year:
        reasons.append(
            f"the figures are for tax year **{rules['tax_year']}** but the current year is **{TODAY.year}**"
        )
    if rules["as_of"]:
        try:
            as_of = dt.date.fromisoformat(rules["as_of"])
            if months_between(as_of, TODAY) > STALE_MONTHS:
                reasons.append(f"they were last reviewed **{rules['as_of']}** (> {STALE_MONTHS} months ago)")
        except ValueError:
            reasons.append(f"the asOf date `{rules['as_of']}` is unparseable")
    else:
        reasons.append("there is no asOf review date")
    return reasons


def check_links(figures: list[dict]) -> list[dict]:
    """Best-effort HEAD/GET on each unique source URL. Network failures are
    reported, never fatal."""
    seen: dict[str, str] = {}
    results = []
    for url in dict.fromkeys(f["source"] for f in figures if f.get("source", "").startswith("http")):
        status = seen.get(url)
        if status is None:
            status = probe(url)
            seen[url] = status
        results.append({"url": url, "status": status})
    return results


def probe(url: str) -> str:
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "victor-rules-freshness/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return "ok" if resp.status == 200 else f"http {resp.status}"
    except urllib.error.HTTPError as e:
        return f"http {e.code}"
    except Exception as e:  # noqa: BLE001 - any network error is just "could not check"
        return f"unreachable ({type(e).__name__})"


def build_report(rules: dict, reasons: list[str], links: list[dict], dead: list[dict]) -> str:
    lines = [
        "# Victor rules-pack freshness report",
        "",
        f"_Generated {TODAY.isoformat()} by `scripts/check_rules_freshness.py`._",
        "",
        f"- Tax year: **{rules['tax_year']}**",
        f"- Last reviewed (asOf): **{rules['as_of']}**",
        f"- Verified flag: **{rules['verified']}**",
        "",
    ]
    if reasons:
        lines += ["## Action needed: re-verify the figures", "", "These figures may be outdated because:", ""]
        lines += [f"- {r}" for r in reasons]
        lines += [
            "",
            "Confirm each value below against its cited official source, then in "
            "`victor_sterling_financial_advisor_ARTIFACT_v3.html` update the value, "
            "bump `asOf` to today and `taxYear` to the current year, and keep "
            "`verified:true`.",
        ]
    else:
        lines += ["## Figures are current", "", "No date-based staleness detected. No action required."]

    lines += ["", "## Figures and sources", ""]
    for f in rules["figures"]:
        lines.append(f"- [ ] **{f['label']}** — `${f['value']:,}` — <{f.get('source', '')}>")

    if dead:
        lines += ["", "## Broken source links (link-rot)", ""]
        lines += [f"- `{d['status']}` — <{d['url']}>" for d in dead]
    elif links:
        lines += ["", f"_All {len(links)} source links reachable._"]

    lines.append("")
    return "\n".join(lines)


def write_output(stale: bool, reasons: list[str], dead: list[dict]) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    summary = "; ".join(reasons + [f"dead link: {d['url']}" for d in dead]) or "current"
    with open(out, "a", encoding="utf-8") as fh:
        fh.write(f"stale={'true' if stale else 'false'}\n")
        fh.write(f"reasons={summary}\n")


def main() -> int:
    text = HTML.read_text(encoding="utf-8")
    rules = parse_rules(text)
    if rules["tax_year"] is None or not rules["figures"]:
        print("ERROR: could not parse RULES object from HTML", file=sys.stderr)
        REPORT_PATH.write_text("# Freshness report\n\nERROR: could not parse the RULES object.\n", encoding="utf-8")
        write_output(True, ["the RULES object could not be parsed"], [])
        return 0

    reasons = date_reasons(rules)
    if os.environ.get("SKIP_LINK_CHECK") == "1":
        links, dead = [], []
    else:
        links = check_links(rules["figures"])
        dead = [l for l in links if l["status"] != "ok"]
    stale = bool(reasons or dead)

    report = build_report(rules, reasons, links, dead)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(report)
    write_output(stale, reasons, dead)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
