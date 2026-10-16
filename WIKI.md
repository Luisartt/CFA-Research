# WIKI.md — Knowledge Wiki Operating Manual (BIMBOA)

Read this before touching the vault.

## CFA Research Challenge team — Grupo Bimbo (BIMBOA)
university team covering Grupo Bimbo, S.A.B. de C.V.

Voice: standard. Clear, complete sentences. No filler, no hedging. Direct. English only.

## Structure
- `raw/` — inbox for non-filing sources: broker notes, transcripts, press, papers, decks. `filings/` is a second inbox (annual/quarterly reports, releases) and follows the same read-only rules. You read, never write. The team may delete a source once it is compiled; that is expected, not a problem.
- `wiki/` — compiled knowledge base. You own it. Flat: files live directly under domain folders (`Company`, `Industry`, `Financials`, `Valuation`, `Macro`, `Risks-ESG`, `Thesis`, `CFA-Process`). No subfolders, no per-folder `_index.md`.
- `wiki/_master-index.md` — the one and only index.
- `wiki/_log.md` — append-only ops journal. Written only by `compile`, `audit`, and `refresh-index`. Never edited by hand.
- `notes/` — The team's human-authored notes. SACRED. Read-only.
- `notes/private/` — The team's private synthesis. Never persisted anywhere; see Private Notes Rules.
- `output/` — artifacts The team explicitly asks for. Never dump compile logs here.

## Directionality
`raw/ → wiki/ → output/`. `notes/` is a reference side-channel: cite and backlink from wiki articles, never generate from.

## Wiki Conventions
- Frontmatter: `Writer`, `Link` (if applicable), `Source`, `tags` (exactly two). Nothing else.
- `Source` — list of the `raw/` paths the article was compiled from, as plain text (e.g. `raw/q3-report.pdf`), never `[[wikilinks]]`. Append a path when a new source updates the article; never remove one. It is the provenance record and how `compile` knows which sources are done, so it stays valid after the file leaves `raw/`.
  - Domain tags: `Company`, `Industry`, `Financials`, `Valuation`, `Macro`, `Risks-ESG`, `Thesis`, `CFA-Process`.
  - Default: one domain tag + one topic tag (e.g. `Industry` + `pricing-power`).
  - Every number in an article carries a data tag from `AGENTS.md` (`[sourced]`, `[guidance]`, `[assumption]`, `[calc]`, `[unverified]`) with document and page/URL.
- Dense bullets, tables, `==highlights==`, `[[wikilinks]]`. End every article with `## Key Takeaways` (3–7 bullets).
- Match the voice of existing articles. No padding phrases.
- Never create subfolders inside a domain folder.
- **Contradictions and staleness.** When a new claim conflicts with or supersedes one in an existing article, never silently overwrite. Insert a `> [!warning] Superseded` callout in the older article, linking the newer article with a `[[wikilink]]`, and keep the original claim beneath it. Time-bound claims carry their source date inline (e.g., "as of 2026-03").

Citations: `[[wikilinks]]` to other vault articles, plus inline source paths (e.g., `filings/BIMBOA-4Q25.pdf`, `raw/call-transcript.pdf`) when citing sources directly.

## Log
`wiki/_log.md` is the vault's memory of what was done. Append one entry at the end of every completed `compile`, `audit`, and `refresh-index` run:
```
## [YYYY-MM-DD] <op> | <one-line summary>
- wrote: `slug-a`, `slug-b`
- updated: `slug-c`
- flagged: `slug-c` superseded by `slug-a`
```
- `<op>` is one of `compile`, `audit`, `audit deep`, `refresh-index`, mirroring the slash command names. Omit empty bullets. `flagged:` means a Superseded callout was written, not merely reported.
- Name articles by file stem in backticks, never `[[wikilinks]]`, so the log stays out of Obsidian's graph and is never rewritten by link updates on rename.
- Record file-level actions on `wiki/` only. Never log query content, answers, or any path under `notes/private/`.
- Append only. Never rewrite or delete past entries. If the file is missing, create it with a `# Log` header first. Read the last few entries at the start of `compile` and `audit` to know what happened recently.

## notes/ — Sacred Rules
- Never edit, restructure, or paraphrase notes. Never copy their content into the wiki.
- Notes never trigger wiki generation on their own. Wiki articles are born from `raw/`.
- When a raw source overlaps a note, backlink to the note with a `[[wikilink]]`.
- **Exception — `refine`:** editor role only. Fix typos silently. Preserve voice, headers, `==highlights==`, `[[links]]`, analogies. Flag unclear spots with `> [!question]` callouts — never invent. Always show a diff before applying.

## notes/private/ — Private Notes Rules
- `notes/private/` is completely invisible to `compile` and `audit`.
- During a query, read it only if The team explicitly references it (e.g., "how does my idea in private/X connect to wiki/Y"). Answers stay in chat — never written to `wiki/` or `output/` unless The team asks.
- In scope for `refine` only when The team names the file explicitly.

## Commands
Step-by-step procedures live in `.claude/commands/`. When The team asks for one of these operations, even in plain words, run the matching command instead of improvising.

| Command | Does | Writes |
|---|---|---|
| `/compile` | Process `raw/` into `wiki/` | Wiki articles, `_master-index.md`, `_log.md` |
| `/audit [deep]` | Review `wiki/`; `deep` adds content checks (monthly) | `_log.md` entry only |
| `/refresh-index` | Rebuild `_master-index.md` | `_master-index.md`, `_log.md` |
| `/refine <path>` | Voice-preserving editor pass on one `notes/` file | That file |
| `/teach <topic>` | Multi-session tutor grounded in `wiki/` | `output/teach/<topic-slug>/` only |
| `/vault-init [force]` | Re-run the interview that renders this file | `CLAUDE.md` |

Questions about vault content go through the `vault-query` skill: wiki first, then notes, then raw; answer in chat.

## Approval Gates
These hold whether or not a command file is loaded.
- `compile`: present the plan in chat and get explicit approval ("go" / "proceed" / "ok" / "yes") before writing any file. A rejected plan writes nothing, including `_log.md`.
- `audit`: never modifies a wiki article. Fixes are a separate pass with their own plan and approval, and their own `_log.md` entry.
- `refresh-index` and `refine`: show the diff in chat; write only on approval.
- `teach`: invoking it counts as The team's explicit ask to write in `output/teach/<topic-slug>/`, and nowhere else.
- Plans and reports live in chat, never in files. `_log.md` is the only file-based record of vault operations.

## Hard Don'ts
- Don't edit `notes/` outside of `refine`.
- Don't move or delete files in `raw/` or `filings/`.
- Don't write to `output/` unless The team explicitly asks.
- Don't invent citations. If no wiki article, `raw/` file, or note backs a claim, say so.
- Don't create subfolders in `wiki/`.
- Don't write to `_log.md` except to append an entry at the end of `compile`, `audit`, `refresh-index`, or an approved audit fix pass.
- Don't rewrite articles in generic LLM voice during compile.

## Project integration (CFA Research Challenge)
`AGENTS.md` rules win on conflict. This wiki is the team's compiled reference layer; it feeds the `research-challenge` skills but never replaces their outputs.

| Wiki domain | Feeds skill | Typical content |
|---|---|---|
| `Company` | thesis, financials | Business model, segments, geographies, brands, management, governance, capital allocation |
| `Industry` | industry | Bakery/packaged-food structure, competitors, peers, channels, regulation, input costs |
| `Financials` | financials, forecast, model | Statement notes, KPIs, accounting adjustments, guidance, call takeaways |
| `Valuation` | valuation | WACC inputs, comps, precedent deals, market data, consensus |
| `Macro` | forecast | FX (MXN/USD/BRL), inflation, wheat/commodity inputs, rates, regional demand |
| `Risks-ESG` | risks-esg | Risk drivers, ESG disclosures, controversies, ratings |
| `Thesis` | thesis, report | Compiled external views (bull/bear, consensus, catalysts). The team's own thesis lives in `notes/` and `research/thesis.md`, never here |
| `CFA-Process` | report, pitch, deck | Rules, grading rubric, templates, deadlines, judge expectations |

- Data tags: every number in a wiki article carries `[sourced]`, `[guidance]`, `[assumption]`, `[calc]` or `[unverified]`. Wiki articles are mostly `[sourced]`/`[guidance]`; team judgment goes in `notes/`, not the wiki.
- Public information only (CFA Standard II(A)). Material non-public information is never compiled; stop and flag it.
- AI-use log: after every `/compile` that writes articles, append `YYYY-MM-DD | member | wiki-compile | wiki/<Domain>/<slug> | compiled from <source>` to `docs/context/ai-use-log.md`.
- `notes/` = the team's handwritten thinking (story, doubts, assumptions). `notes/private/` = work-in-progress views the team does not want persisted.
- `/wrap-up` should mention the last `wiki/_log.md` entry in `docs/context/session-log.md`.
