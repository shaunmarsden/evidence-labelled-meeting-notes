---
name: evidence-labelled-meeting-notes
description: Turn a meeting transcript or clear notes into a write-up that keeps confirmed facts, estimates and assumptions visibly separate, so nothing invented gets treated as agreed. Use for any meeting, a status update, a planning session, a hiring debrief, a stakeholder review, where what was actually said needs to stay distinct from what is being assumed. Do not use this to write a finished summary email on its own; it produces the evidence pack a summary should be built from.
---

# Evidence-Labelled Meeting Notes

You do not need to install anything to try this once: copy this whole file, paste it as your first message in any AI chat tool, then follow it with your actual inputs.

Turn a meeting transcript or notes into a reliable record for human review. Preserve uncertainty and avoid turning a plausible interpretation into a fact, or a discussed idea into a decision.

## Gather the Inputs

List the material supplied before analysing it. Inputs may include:

- The current meeting's transcript or notes
- Relevant earlier notes or correspondence, if available
- Who was actually in the meeting and what they said, versus what is being reported second-hand

Use only the information needed for this write-up. Exclude unrelated personal information.

## Classify the Evidence

Use these labels consistently:

- `confirmed`: directly and explicitly stated in the meeting
- `estimate`: a number or view explicitly presented as approximate
- `second_hand`: reported by someone who was not the original source
- `inference`: a reasonable interpretation that still needs checking
- `unknown`: important information the meeting did not establish
- `conflict`: two things said in the meeting disagree with each other

Do not upgrade an estimate, a second-hand comment or an inference into a confirmed fact.

## Extract the Findings

1. Identify confirmed facts and estimates, kept clearly labelled as which.
2. State plainly when the meeting actually reached a genuine decision, do not hedge a real, explicit agreement just to be cautious; treating a real yes as ambiguous is its own failure, not a safe default.
3. Record each action with its owner and timing, only where the meeting actually assigned both; mark either as unknown, or as a soft estimate, if it did not.
4. Flag anything that sounds like a decision but was never actually confirmed as one, a proposal floated and never voted on, an idea that got nodded at rather than agreed.
5. Note open questions and genuine unknowns the meeting did not resolve.
6. Surface any conflict between two things said in the same meeting, rather than silently picking the more convenient one.
7. Prepare a short summary that a reader could act on, with facts, decisions, estimates and assumptions still visibly distinct within it.

Use [the output template](templates/output-template.md) for the shape of the final write-up.

## Apply the Guardrails

- Never invent an owner, a date, or a commitment the meeting did not actually establish.
- Preserve conditional language exactly: "I think", "probably", "we should check", "subject to budget approval".
- Do not treat a discussed option as a decision unless the meeting shows it was actually decided.
- Equally, do not hedge a genuine, unambiguous agreement into looking uncertain just to seem cautious; call a real decision a decision.
- State plainly when the meeting did not resolve something, rather than filling the gap with a plausible guess.
- Recommend a next step if one is obvious, but do not treat this write-up as authorisation to act on it.

## Stop When the Task Is Unsafe

Do not manufacture a complete write-up when:

- No usable transcript or notes are actually supplied
- The material is too thin or garbled to support confident labelling
- The request is to present an unsupported interpretation as a confirmed fact or a settled decision
- The output would expose personal or confidential information not needed for the write-up

Explain the limitation and ask only for the minimum missing information.

## Require Human Review

End with the points a reader must check before treating this write-up as the record: any action with an unknown owner or date, any flagged non-decision, and any conflict that was surfaced rather than resolved.

For fictional tests, read [the first worked example](example/), built to check the skill does not mistake a floated idea for a real decision, and [the second](example-two/), built to check the opposite: that it still recognises a genuine decision when one actually happens.
