# Does the Template Need to Be Inside the Skill? An 18-Run Test

The skill tells an AI to use [the output template](../templates/output-template.md) for the shape of its write-up, and it linked to the template by a relative path. When you paste SKILL.md into a chat, as the README says to, that link doesn't open. I wanted to know what that costs, and whether writing the template into the skill fixes it. It costs the shape. With the link, none of 6 replies used the template's headings. With the template written in, all 6 did, and nothing else got worse. I made that change, and this page records the two tests behind it.

## What I Tested

I gave an AI the skill text, then one meeting transcript, and asked it to write the meeting up. The task line was the same every time: "Here is the transcript of a meeting. The company and the people are fictional. Please write it up." Three transcripts, each used with a larger and a smaller model:

- **The Atlas status call** from [the first example](../example/transcript.md).
- **The Overton hiring debrief** from [the second example](../example-two/transcript.md).
- **A renewal planning call I wrote for this test**, below.

```text
# Fictional Transcript: Ridgeway Renewal Planning

Ridgeway Logistics, an entirely fictional customer of an invented software company. Internal renewal planning call. Participants: Maren Pryce (Account Director), Tobias Quill (Finance Partner), Saskia Sorrel (Customer Success).

---

**Maren:** Let's start with the basics. Ridgeway's renewal date is the 30th of November, right?

**Tobias:** Yes, 30 November. That's in the contract.

**Maren:** Good. Tobias, where are we on the current contract value?

**Tobias:** It's £84,000 a year.

**Saskia:** Hang on, I had it as £48,000 in my notes from the last review.

**Tobias:** I'm fairly sure it's £84,000, but I'm going from memory.

**Maren:** Okay, we'll sort that out. How's the relationship, Saskia?

**Saskia:** I think their sponsor is fine with us. And I heard from someone on their ops team that they might be looking at a competitor, but that's secondhand, I haven't spoken to anyone senior about it.

**Maren:** Noted. Tobias, how long do you think the renewal will take once we send the paperwork?

**Tobias:** Probably around six weeks, give or take. Procurement there is slow.

**Maren:** So now, pricing. I'd like to offer them flat pricing on renewal, no uplift. Any objection?

**Tobias:** None from finance.

**Saskia:** Yes, flat is the right call.

**Maren:** Good, that's decided then, flat pricing. And what about offering a discount if they sign for three years instead of one?

**Tobias:** We could look at it.

**Saskia:** Depends what they want, really.

**Maren:** Okay, let's park that for now.

**Saskia:** I'll send round the usage report for the account.

**Maren:** Great. And someone should probably call the sponsor before the paperwork goes out.

**Saskia:** Yes, that makes sense.

**Maren:** Okay, thanks both.
```

I tested three versions of the skill:

- **Current.** SKILL.md as it was, with the template linked by a relative path.
- **Template and closing section.** The template written into SKILL.md where the link was, and a new closing section on the template called "Check Before Relying On This".
- **Template only.** The same, without the new section.

In every version I removed the sentence at the end that points to the worked examples, so a reply couldn't take a hint from it. The shipped file keeps that sentence.

> **Re-running this yourself?** Copy everything above this line and stop here. The section below says what each reply was scored on, so including it turns the test into an open-book exam and the result will look better than it should.

## What I Decided in Advance

I wrote five pass-or-fail measures before any run, and scored each reply by reading it.

1. **Closing check.** The reply ends with a section saying what a reader must check, and names every unowned or untimed action, every non-decision and every open conflict that exists in that transcript.
2. **Shape.** The reply uses the template's headings: Confirmed Facts, Estimates, Second-Hand Reports, Flagged Non-Decisions, Actions as a table with owner, timing and status, Open Questions and Summary, plus Confirmed Decisions where the transcript has a real decision.
3. **Traps.** Every planted trap is handled as I'd decided. For the Atlas call: auth is not signed off, the 15th and the rollout approach are not decisions, two actions have no owner, the two-day figure is an estimate, and the login-timeout report is second-hand. For the Overton debrief: the offer is a real decision, waiting for a second interview is a real decision, take-home tests are not, Casey owns both actions, "aim for early next week" is soft and "by Friday" is firm. For the renewal call: 30 November is confirmed, flat pricing is a real decision, the three-year discount is not, the contract value is shown as a conflict and not settled either way, the competitor report is second-hand, the sponsor's view is an inference, six weeks is an estimate, Saskia owns the usage report with no timing, and nobody owns the sponsor call.
4. **No overstatement.** Nothing a speaker hedged is stated as settled.
5. **No invention.** No owner or date that isn't in the transcript.

For the first test I said I'd change the skill only if the closing check passed in at least 5 of 6 replies with the change and at least 3 more than without, shape was at least as good, and no other measure fell by 2 or more. For the second test I said I'd change it if shape and the closing check each passed in at least 5 of 6 and none of the other three measures fell below 5 of 6. I added no runs.

## Method

Eighteen runs on 20 October 2026 in fresh conversations, on settings that report themselves as `claude-opus-5-5` and `claude-haiku-5-5`. Both names are self-reported. Each run read its input from a file and wrote its reply to another. In the first test, six replies used the current skill and six used the template and closing section. In the second, six used the template alone. For the second test I reused the six current-skill replies from the first as the baseline. I ran them earlier the same day, on the same transcripts and settings, and didn't rerun them. I scored by reading and could usually tell which setup a reply came from. After the runs I gave two of the three people in the renewal call different names, because the first ones appeared elsewhere in my repos. Nothing else in it changed. I also changed five names in the two example transcripts afterwards, because they matched characters in other repos. The first test's runs used the earlier names.

## Result

| Passes, of 6 | Current | Template and closing section | Template only |
| --- | ---: | ---: | ---: |
| 1. Closing check | 6 | 6 | 6 |
| 2. Shape | 0 | 6 | 6 |
| 3. Traps | 6 | 6 | 6 |
| 4. No overstatement | 6 | 6 | 6 |
| 5. No invention | 6 | 5 | 6 |
| Mean words a reply | 833 | 871 | 903 |

The first test missed my line, because the closing check was already 6 of 6 without the new section, so the change was no better on the one thing I'd set it to improve. I changed nothing. The second test met its line, so I wrote the template into the skill and changed nothing else.

## What the Result Shows

**The shape was the problem, not the closing section.** I'd thought the closing section was missing, because neither of my two example outputs had one. The skill asks for it in one sentence, and all 18 replies had one, with or without the template. The two example outputs just came from a run that left it out.

**A pasted skill can't use a link.** Of the 6 replies to the current skill, 3 told the reader the template wasn't included, and 3 built their own layout and said nothing. Their headings ran from "Evidence" and "Decisions and non-decisions" to "Facts and estimates". They were readable and mostly right, but a reader who had the template in mind would not have got it.

**Writing the template in worked with both models.** The larger and smaller model each used the template's headings on all three transcripts.

**The new closing section added nothing.** It made no difference to any measure.

**The traps held in every setup.** None of the 18 replies treated the 15th as an agreed launch date, or the rollout approach, the three-year discount or the take-home tests as decided. None named a person as owner of an action nobody took on without saying it hadn't been assigned, and none settled the renewal call's contract value in either direction.

## What Went Wrong, and What I Can't Tell

- **Measure 4 is a judgement.** I fixed the reading while scoring, the same for every setup: stating "Dan said it's basically done" as his view with the hedge kept passes, and calling the migration complete fails. On a stricter reading that counts any `confirmed` label on a hedged statement, replies in all three setups would fail, so the measure doesn't separate them.
- **One invented date.** One reply with the template and closing section wrote "Today is 20 October", which isn't in the transcript. Four replies to the renewal call worked out a send deadline of about 19 October from the six-week estimate and said it was their own arithmetic. I didn't count those.
- **Small slips I didn't score.** One reply gave the QA lead a pronoun the transcript doesn't give. Several wrote "not started" against actions nobody described. One listed the unsettled contract value under Estimates as well as under Conflicts. Two labelled the 15th target an `estimate`.
- **The checklist still doesn't open.** SKILL.md ends by pointing to [the review checklist](../checks/checklist.md) by a relative link, and 13 of the 18 replies said they hadn't opened it or it wasn't included: 3 of the 6 to the current skill, 4 of the 6 to the template and closing section, and all 6 to the template alone. I haven't changed or tested that.
- **The template now lives in two places,** SKILL.md and the template file.
- **One stray.** One smaller-model run started a background task and then dismissed it, which I've seen before. It didn't change the reply.
- **Six runs a setup, three transcripts,** two of them the repo's own examples. The baseline wasn't run alongside the retest. I wrote the renewal call knowing what I was looking for. I scored by reading, not blind. The replies came from two model settings, run inside a coding tool with my project notes.

## What I'd Do Next

I'd test writing the review checklist into the skill the same way, since the same link problem applies and 13 of 18 replies noticed it. I'd also run the skill on a transcript from a real meeting, which I haven't. These transcripts are ones I wrote, and the skill's real test is a meeting I didn't plan.
