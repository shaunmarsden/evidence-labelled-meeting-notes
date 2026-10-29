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

## Method

Twelve runs on 29 October 2026, each in a fresh conversation, on settings that report themselves as `claude-opus-5-5` and `claude-haiku-5-5`. Both names are self-reported. Each run read one prompt file and wrote its reply to a file named by a random code. A mapping of codes to versions stayed hidden until I had scored every reply and committed [the blind scores](checklist-in-skill/blind-scores.md). The [prompts](checklist-in-skill/prompts/), [replies](checklist-in-skill/replies/), [mapping](checklist-in-skill/mapping.json) and [a script that counts the scores](checklist-in-skill/analyse.py) are all in the folder.

## Result

| Passes, of 6 | Current | Inline |
| --- | ---: | ---: |
| A. Says the checklist is missing | 4 | 0 |
| B. Gives the reader the checklist | 0 | 6 |
| 1. Closing check | 5 | 5 |
| 2. Shape | 6 | 6 |
| 3. Traps | 6 | 6 |
| 4. No overstatement | 5 | 6 |
| 5. No invention | 5 | 6 |
| Mean words a reply | 910 | 942 |

Every line held. Inline said the checklist was missing in none of its 6 replies, against 4 of 6 for Current. Shape passed in 6 and the closing check in 5. No guard fell. I've written the checklist into the skill.

## What the Result Shows

**Writing the checklist in fixed the link problem.** Every Inline reply ended with the checklist for the reader, and none said anything was missing. Four of the 6 Current replies told the reader the checklist wasn't included or hadn't been used. The other 2 said nothing about it, so a reader wouldn't know there was a checklist at all.

**It made nothing else worse.** The guards came out the same or one better for Inline. A difference of one reply in six is too small to read anything into.

**Both models followed it.** The larger and smaller model each gave the checklist on all three transcripts. Three replies reworded some points to fit the meeting, for example naming the decision the reader should check. That still counts as giving the checklist.

## What Went Wrong, and What I Can't Tell

- **Measure B gives the version away.** I scored the guards before B, but a reply that ends with the checklist is plainly Inline, so the guards weren't fully blind either.
- **Two closing checks failed on a strict reading.** One reply in each version left out that Saskia's usage report has no time. On a reading that only asks for unowned actions, both pass. The readings I fixed while scoring are in [the blind scores](checklist-in-skill/blind-scores.md).
- **The two guard failures were both in Current.** One reply called the migration "complete" when Dan said "basically done". Another named Hester as owner of an action nobody took on. Neither is to do with the checklist.
- **Small slips I didn't score.** Four replies gave Sam or Casey a pronoun the transcript doesn't. One said "no one in the meeting" had spoken to anyone senior, when only Saskia said that about herself.
- **The checklist now lives in two places,** SKILL.md and [checks/checklist.md](../checks/checklist.md), like the template.
- **Six replies a version, three transcripts,** two of them the repo's own examples, all written by me. I scored by reading. The replies came from two model settings, run inside a coding tool with my project notes.

## What I'd Do Next

Run the skill on a transcript from a real meeting I didn't write. That is still the test it hasn't had.
