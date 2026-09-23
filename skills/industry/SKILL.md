---
name: industry
description: Industry and competitive analysis for a CFA Research Challenge company - market definition and size, five forces, competitive landscape and market share, positioning and moat, SWOT, peer universe for comps, and what it all implies for the forecast and thesis, with a LatAm lens (regulation, FX, informal markets, family groups). Does the research and structure; coaches the team on where the company really competes and what protects it. Use whenever a student asks to analyze the industry or sector, map competitors, pick comparables, build a SWOT or five forces, assess a moat or market share (also in Spanish or Portuguese, e.g. "analiza la industria", "quienes son los comparables") - even if they don't explicitly ask for an industry report.
---

# industry

## Purpose

Give the team a rigorous, sourced picture of the market their company competes
in, fast. The research and structure are the assistant's job; two judgments
belong to the team: where the company really competes, and what protects it.

## Reads

- `company-profile.yaml` — missing: ask company, country and sector in one
  line, suggest `/research-challenge:init-skills`, and continue anyway.
- `filings/` — annual report business and MD&A sections, risk factors —
  empty: say so, use web search, tag every figure, add a todo to drop the
  annual report in `filings/`.
- `research/sources/` — any reports or links the team saved — optional; if
  absent, suggest the team save reports and links there.
- `research/thesis.md` — optional; used for section 7.
- `research/industry.md` — if present, update it instead of starting over.
- `references/industry-report-template.md`.

## Steps

1. **Gather.** Read the business description and MD&A in `filings/`, the team's
   `research/sources/`, and use web search if available. Record every source.
2. **Draft sections 1-6** of `references/industry-report-template.md`. Tag every
   number. Market share you cannot source: `[unverified]` plus a todo item —
   never estimate it silently.
3. **Apply the LatAm lens** checklist at the end of the template; add what
   applies to the relevant section.
4. **Run the coach moments** below before finalizing sections 1, 4 and 6.
5. **Write section 7** linking the findings to the forecast and, if
   `research/thesis.md` exists, to each pillar (supports / weakens / neutral).
6. **Save** `research/industry.md` (update the date line). Close with one next
   step — usually the pillar the analysis weakens most, or the data gap to close.

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Market definition (section 1):** the most common trap. A company that looks
  dominant in a narrow market may be small in the one that sets its prices. Ask
  which market the customer actually chooses within.
- **Moat (section 4):** ask for the evidence that the advantage shows up in
  numbers (margins above peers, stable share, pricing power).
- **Peer set (section 6):** ask them to defend each peer in one sentence; a
  judge will ask why a peer was included or left out.

## Writes

- `research/industry.md`
- Appends to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — industry — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | industry | research/industry.md | researched and drafted sections 1-7; team decided market definition, moat, peers`
- `docs/context/todo.md`: one item per `[unverified]` figure.
- `docs/context/memory.md`: `# decision: peer set = <tickers>` once agreed.
