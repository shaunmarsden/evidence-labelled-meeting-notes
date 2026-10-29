# Does the Review Checklist Need to Be Inside the Skill? A 12-Run Test

The [template test](template-in-skill-test.md) found that a pasted skill can't open a link, and fixed it for the output template. It also found a second link with the same problem. SKILL.md ends "Use [the review checklist](../checks/checklist.md) before treating any write-up as the record", and 13 of the 18 replies in that test said they hadn't opened it or it wasn't included. This test asks whether writing the checklist into the skill fixes that without making anything else worse.

## What I Tested

Two versions of the skill, both in [checklist-in-skill](checklist-in-skill/):

- **Current.** SKILL.md as it is.
- **Inline.** The same, with the link sentence replaced by "After those points, give the reader this checklist to go through before treating the write-up as the record:" and the six items from [the checklist](../checks/checklist.md), word for word.

In both, as in the template test, I removed the sentence that points to the worked examples, so a reply can't take a hint from it. The shipped file keeps it.

Each prompt is the skill, a line, the task line from the template test ("Here is the transcript of a meeting. The company and the people are fictional. Please write it up."), and one transcript: the Atlas status call from [the first example](../example/transcript.md), the Overton hiring debrief from [the second](../example-two/transcript.md), or the Ridgeway renewal call written for the template test ([copied here](checklist-in-skill/ridgeway-transcript.md)).

3 transcripts x 2 versions x 2 model settings (the larger and smaller ones the template test used) = 12 replies, 6 per version. Each run reads one file and writes one reply under a random name. I score blind, then unblind.

> **Re-running this yourself?** Copy everything above this line and stop here. The section below says what each reply is scored on.

## What I Decided in Advance

Written on 29 October 2026, before any run.

Two new measures:

- **A. Says the checklist is missing.** The reply says it couldn't open the review checklist, or that it wasn't included. This is the problem the template test found.
- **B. Gives the reader the checklist.** The reply ends with at least five of the checklist's six points for the reader, in any wording.

The five measures from the template test, unchanged, as guards: 1 closing check, 2 shape, 3 traps, 4 no overstatement, 5 no invention. They are defined in [that test](template-in-skill-test.md#what-i-decided-in-advance).

I will put the checklist into the skill if all of these hold:

- Inline says the checklist is missing in at most 1 of 6 replies, and in fewer than Current.
- Shape and the closing check each pass in at least 5 of 6 Inline replies.
- None of traps, no overstatement and no invention falls by 2 or more from Current to Inline.

If any fails, I leave the skill as it is and say so. I will add no runs.

I can't fully hide which version a reply came from, because measure B shows it. I'll score the guards before B.
