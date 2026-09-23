# Phase 1 manual evals

Run in a fresh empty folder after installing the plugin from a local path
(`/plugin marketplace add <repo path>`, `/plugin install research-challenge@cfa-research`).
Mark each expected behavior pass/fail.

## init-skills

1. Prompt: `/research-challenge:init-skills` in an empty folder.
   - [ ] Prints the audit table before asking anything.
   - [ ] Asks one question at a time, each with a default.
   - [ ] Proposes IFRS + MXN + Mexico City for a BMV company and asks to confirm.
   - [ ] Creates all files and 7 folders; `company-profile.yaml` has no `{{`.
   - [ ] `todo.md` milestones are dated backwards from the deadline.
   - [ ] Appends a line to `ai-use-log.md`.
2. Prompt: `/research-challenge:init-skills` again in the same folder.
   - [ ] Says "Project already set up. Nothing changed." and asks nothing.
3. Setup: delete `docs/context/lessons.md`, edit `CLAUDE.md` to remove `@AGENTS.md`. Run again.
   - [ ] Recreates only `lessons.md`; asks `[k]/[o]/[m]` for `CLAUDE.md`; no interview.

## thesis

1. Prompt: "We think Cemex is a buy because infrastructure spending is going up."
   - [ ] Restates the idea and asks to confirm before challenging.
   - [ ] Asks at most 3 questions; ends with one next step.
   - [ ] Does not propose pillars the student did not raise.
2. Prompt: "roast our thesis" with an existing `research/thesis.md`.
   - [ ] Summarizes the current version first; uses L2/L3 questions.
3. Prompt: "ok, write it up" after a full session.
   - [ ] Writes `research/thesis.md` in template layout; every number tagged; History line added.
   - [ ] Appends to `thesis-journal.md` and `ai-use-log.md`.

## industry

1. Prompt: "analyze the industry for our company" (profile present, one annual report in `filings/`).
   - [ ] Drafts sections 1-6 with sources; unsourced market share tagged `[unverified]` + todo.
   - [ ] Stops for the market-definition coach moment before finalizing.
2. Prompt: "who should be our comparables?"
   - [ ] Proposes 5-8 peers mixing local/regional/global, flags IFRS vs US GAAP.
   - [ ] Asks the team to defend each peer.

## wrap-up

1. Prompt: `/research-challenge:wrap-up` after a thesis session.
   - [ ] Updates todo/session-log; ai-use-log has lines for the session's work.
   - [ ] Reports in five lines or fewer with one next step.
