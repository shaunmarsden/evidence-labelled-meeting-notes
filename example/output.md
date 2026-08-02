# Evidence-Labelled Notes: Project Atlas Weekly Status

Source: [transcript.md](transcript.md), Fernbridge Digital, fictional.

## Confirmed Facts

- Core platform migration is complete; the last two services moved over on Tuesday. `confirmed` (Dan)
- The auth flow is not signed off. QA found an edge case with expired session tokens on Monday and testing is still in progress. `confirmed` (Sam, correcting an earlier misstatement from Dan, who confirmed he had been thinking of the payments flow, not auth)

## Estimates

- Auth testing may take roughly two more days, possibly less if the fix is as simple as it currently looks. `estimate` (Sam, explicitly hedged, not a committed date)

## Second-Hand Reports

- Users have reportedly been complaining about login timeouts on the current system. `second_hand`, relayed by Liz from the support team; not confirmed first-hand by anyone in this meeting. Liz herself flagged this as something to look into properly rather than act on as-is.

## Flagged Non-Decisions

- **The 15th as a launch date was discussed, not agreed.** Priya proposed it; Dan gave a conditional, hedged yes ("I guess that could work, assuming Sam's estimate holds"); Sam explicitly declined to commit to any date until auth testing is finished. Priya then confirmed it stays a working target, not a locked date. Treat this as unresolved, not as a decision.
- **Rollout approach (gradual vs. all at once) was discussed, not decided.** Liz leaned gradual; Dan said it could go either way. Priya explicitly left it open pending the auth testing outcome.

## Actions

| Action | Owner | Timing | Status |
| --- | --- | --- | --- |
| Finish auth flow testing | Sam (QA) | `estimate`, roughly two days | In progress |
| Look into the login timeout reports properly | `unknown`, not assigned in this meeting | `unknown` | Not yet started |
| Update the rollback plan doc (still references old service names) | `unknown`, Dan acknowledged it needs doing but was not explicitly assigned it | `unknown` | Not yet started |

## Open Questions

- Launch date: still open, pending auth testing.
- Rollout approach: still open, pending auth testing.
- Who is actually looking into the login timeout reports: not assigned.
- Who owns the rollback plan doc update: acknowledged as needed, not assigned to a specific person.

## Summary

Migration itself is complete. The one blocking item is auth flow testing, currently in progress with no confirmed completion date, only a hedged two-day estimate. Both the launch date and rollout approach were discussed but explicitly left open pending that testing. Two actions (the login timeout follow-up and the rollback plan update) were raised but not assigned to anyone; both need an owner before next week's call, not just a general acknowledgement that they need doing.
