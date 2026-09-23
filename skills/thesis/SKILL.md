---
name: thesis
description: Coach a CFA Research Challenge team to a sharp, defensible investment thesis - 2-3 pillars, variant perception versus consensus, catalysts and kill criteria. Stress-tests the story Socratically in graded levels (Frame, Probe, Stress), then co-writes research/thesis.md once the team owns the ideas. Use whenever a student is choosing or shaping the story, asks "is our thesis good", "why buy or sell", "what is our angle", "roast our thesis", wants a buy/sell/hold argument challenged, or is about to lock the recommendation - even if they don't explicitly ask for coaching.
---

# thesis

## Purpose

The thesis is the one thing the team must own. Help them find it, test it until
it holds, then write it up well. Challenge ideas; never supply the pillars.

## Reads

- `company-profile.yaml` — missing: ask company and sector in one line and
  suggest `/research-challenge:init-skills`; continue anyway.
- `research/thesis.md` — if present, resume from the latest version.
- `docs/context/thesis-journal.md` — grep the last entries for open questions.
- Optional evidence: `research/industry.md`, `data/financials.csv`,
  `model/model-summary.json`. Use what exists; never block on what does not.
- `references/question-bank.md` and `references/synthesis-template.md`.

## Steps

1. **Load state.** If `research/thesis.md` exists, summarize the current
   one-line thesis, pillars and open red flags in five lines. Ask what changed.
2. **Frame (L1).** Ask for the thesis in one sentence. Restate it in the
   student's own words and ask "is that right?". Do not move on until confirmed.
   No thesis yet: use L1 questions to help them find one — ask, do not propose.
3. **Probe (L2).** Pillar by pillar: evidence, model line, consensus view, why
   the market is wrong, size of the effect. 2-3 questions per turn from the bank.
   When a student cites a number, check its tag; untagged numbers get flagged.
4. **Stress (L3).** Opposite case, kill criteria, catalysts and timing,
   "already priced in". Escalate only after L2 is answered cleanly.
5. **Stop** when answers stop producing new information, or when the student
   asks. If the thesis is genuinely solid, say so plainly.
6. **Synthesize.** Write `research/thesis.md` from
   `references/synthesis-template.md`. Co-write the prose from the team's
   answers — polish wording, never add a pillar they did not argue. Tag every
   number. New version: bump `Version`, add a `History` line, keep the old
   pillars in History if they changed.
7. **Close** with one next step (usually: the evidence gap that matters most).

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Pillar selection:** which 2-3 survive. Push to cut the weakest one.
- **Variant perception:** what exactly the market misses. "Good company" is not
  a thesis; a gap versus consensus is.
- **Kill criteria:** the fact that would change their mind.
- **Direction:** Buy/Hold/Sell stays provisional until valuation — say so.

## Writes

- `research/thesis.md` (versioned in-file; history kept).
- Appends to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — thesis — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`: one line per session, e.g.
  `YYYY-MM-DD | <member> | thesis | research/thesis.md | coached pillars; co-wrote prose from team answers`
- `docs/context/memory.md`: `# decision: pillar <n> = <title>` when a pillar is locked.
- `docs/context/todo.md`: one item per evidence gap, with owner if known.
