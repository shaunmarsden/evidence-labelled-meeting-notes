# Fictional Transcript: Project Atlas Weekly Status

Fernbridge Digital, an entirely fictional software company. Weekly status call for Project Atlas, an internal platform migration. Participants: Priya Nair (Project Manager), Dan Okafor (Engineering Lead), Sam Whitfield (QA Lead), Liz Chen (Product).

---

**Priya:** Morning all. Let's do a quick run through where Atlas stands before we all scatter for the day. Dan, where are we on the migration itself?

**Dan:** Core migration's basically done. We moved the last two services over on Tuesday. Auth flow's the one still in progress, but QA signed off on that yesterday, so I think we're in good shape there.

**Sam:** Sorry, hang on, that's not right. We haven't finished testing the auth flow yet. We found an edge case with expired session tokens on Monday and we're still working through it. Nothing's been signed off from our side.

**Dan:** Oh. I might be thinking of the payments flow then, not auth. My mistake.

**Priya:** Okay, let's flag that as still open then, not signed off. Sam, any sense of timing on the auth testing?

**Sam:** Hard to say exactly. Probably another two days, maybe less if the fix is as simple as it looks, but I don't want to promise that.

**Priya:** Understood, we'll treat that as a rough estimate for now, not a date. Liz, anything from the product side?

**Liz:** Just one thing, the support team mentioned to me that users have been complaining about login timeouts on the current system. I haven't looked into it myself, just passing it along from what they told me.

**Priya:** Good to know, we should get someone to actually look into that properly rather than going on secondhand reports. Okay, on timing then, given where the auth flow is, should we say the 15th for launch?

**Dan:** Yeah, I guess that could work, assuming Sam's estimate holds.

**Sam:** I mean, maybe, but I'd rather not commit to a date until the auth testing's actually done. There could be more edge cases like the one we found.

**Priya:** Fair, let's not lock in the 15th then, just keep it as a working target. One more thing before we go, someone needs to update the rollback plan doc, it's still referencing the old service names from before the migration.

**Dan:** Yeah, that needs doing.

**Priya:** Great, let's pick that up next time. Last thing, are we doing a gradual rollout with feature flags or flipping it all at once?

**Liz:** I'd lean gradual, safer given what Sam's finding.

**Dan:** Could go either way honestly, depends how the auth testing lands.

**Priya:** Let's leave that open and revisit once auth's actually done. Thanks everyone, same time next week.
