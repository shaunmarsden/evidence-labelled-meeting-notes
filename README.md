# Evidence-Labelled Meeting Notes

<p>
  <img alt="Status: Working tool" src="https://img.shields.io/badge/status-working%20tool-2563eb">
  <a href="LICENSE"><img alt="Licence: MIT" src="https://img.shields.io/badge/licence-MIT-lightgrey"></a>
</p>

Turn a meeting transcript or your notes into a write-up that keeps confirmed facts, estimates and assumptions apart, so nobody mistakes something invented for something agreed.

## Why

A meeting write-up usually reads as one flat block of "what happened," so a proposal nobody agreed reads the same as a real decision. An action nobody was given reads as if someone owns it. This keeps them apart: what was confirmed, what's an estimate, what's second-hand, and what only sounds like a decision but was left open.

[![Meeting notes before and after evidence labels are applied.](assets/diagrams/07-evidence-labelled-meeting-notes.svg)](SKILL.md)

**Not what you need?** This turns a meeting into a written record. If you're checking the status fields in a tracker against the evidence for each item, you probably want [Claims vs. Evidence Checker](https://github.com/shaunmarsden/claims-vs-evidence-checker).

## Use It

Copy [SKILL.md](SKILL.md) and paste it into your AI tool (ChatGPT, Claude, Gemini or similar). Then paste in the meeting's transcript or your notes. You get:

- Confirmed facts, kept apart from estimates and second-hand reports
- Flagged non-decisions: anything that sounded like an agreement but wasn't confirmed as one
- An action list, with owner and timing marked unknown, not guessed, wherever the meeting didn't set them
- Open questions: what the meeting left unsettled

<details>
<summary><strong>See exactly what it produces</strong></summary>

1. A labelled list of confirmed facts, estimates, second-hand reports, inferences, unknowns and conflicts
2. Real decisions stated plainly as decisions, next to anything flagged as a non-decision
3. An action list with owner and timing marked unknown wherever the meeting didn't set them
4. Open questions the meeting left unsettled, with the points a reader must check before relying on the write-up

</details>

[The output template](templates/output-template.md) shows the exact shape with no made-up content. The worked examples show it run on full transcripts. [The first](example/) is a project status call with traps that shouldn't be mistaken for decisions: a proposal nobody agreed, an action someone mentioned but nobody was given, and a fact one speaker got wrong and then corrected. [The second](example-two/) tests the opposite risk. It's a hiring debrief with real, confirmed decisions, which the skill has to recognise rather than hedge out of too much caution.

Use [the review checklist](checks/checklist.md) before you treat any write-up as the record.

You don't need to install anything or write any code to try it once.

## Before You Use It

Don't paste in anything confidential that you're not allowed to use outside your organisation's approved tools. The write-up is for your own use. Treat any suggested next step as something to check and do yourself. The write-up hasn't approved it.

## Feedback

Tried it on a real meeting? [Start a discussion](https://github.com/shaunmarsden/evidence-labelled-meeting-notes/discussions) if something didn't work the way you expected.

## Part of a Family

This is one of a family of free tools that take patterns from [practical-ai-sales-workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows) and use them outside sales. The rest are in [sibling-projects](https://github.com/shaunmarsden/sibling-projects). Not sure which one fits? Try [the interactive picker](https://shaunmarsden.github.io/sibling-projects/), or paste a description of your problem into an AI chat with [the router](https://github.com/shaunmarsden/sibling-projects/blob/main/ROUTER.md).
