+++
id = "ref/skill/appraise"
kind = "rule"
title = "Appraise"
source_ids = ["core-rulebook", "occult-adventures", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "appraise", path = "json/skills.json" },
]
[[sources]]
publication = "core-rulebook"
page = "90"

[fields]
kind = "none"
+++

**Associated Skill**

**Details:** Intelligence

**Trained Only**

**Details:** No

**Armor Check Penalty**

**Details:** No

**Optional Unchained Skill**

**Details:** No

**Optional Background Skill**

**Details:** Yes

### Check

A DC 20 Appraise check determines the value of a common item. If you succeed by 5 or more, you also
determine if the item has magic properties, although this success does not grant knowledge of the
magic item's abilities. If your fail the check by less than 5, you determine the price of that item
to within 20% of its actual value. If you fail this check by 5 or more, the price is wildly
inaccurate, subject to GM discretion. Particularly rare or exotic items might increase the DC of
this check by 5 or more.

You can also use this check to determine the most valuable item visible in a treasure hoard. The DC
of this check is generally 20 but can increase to as high as 30 for a particularly large hoard.

### Action

Appraising an item takes 1 **standard action**. Determining the most valuable object in a treasure
hoard takes 1 **full-round action**.

### Try Again

Additional attempts to Appraise an item reveal the same result.

### Special

A spellcaster with a [raven](ref/monster/familiar-raven) familiar gains a +3 bonus on Appraise
checks.

### Occult Skill Unlocks

[Occult skill unlocks](ref/rule/occult-skill-unlocks) are available to those using the occult rules
and meet certain requirements.

#### Psychometry

**Sources:** Occult Adventures pg 196

You can read the psychic impressions left on objects or in places by previous owners and events.

##### Check

Once per day, you can concentrate for 1 minute while in physical contact with an item or location,
during which you receive flashes of insight regarding the subject's nature and ownership. After 1
minute, you attempt a DC 15 Appraise check to decipher the visions. You gain one piece of
information about the historical significance or the last previous owner - such as a glimpse of the
last owner's appearance or its emotional state when it last used the item - determined by the GM.

You learn one more piece of information for every 10 by which your check result exceeds the DC, as
long as you concentrate for 1 additional minute for each piece of information.

If you fail the check by less than 5 or the item has no significant psychic imprint, you don't learn
any information. If you fail this check by 5 or more, the item appears to be psychically significant
even if it's not, and the information you gain is wildly inaccurate.

If you attempt to use psychometry on an item affected by [charge object](ref/spell/charge-object) or
[implant false reading](ref/spell/implant-false-reading), you automatically learn all information
imprinted by the spell. You must also attempt a Will save. If the item is affected by an
_[implant false reading](ref/spell/implant-false-reading)_ spell, on a success, you realize the
information was false, and can determine the true information as well. On a failure, or if the item
is affected by a _[charge object](ref/spell/charge-object)_ spell, you believe the information is
true.

##### Action

Reading an object requires at least 1 minute of uninterrupted concentration.

##### Try Again

Yes. Multiple readings on an object or place always give the same results unless its circumstances
or ownership have changed, but additional checks might reach further back into an object's history.
You don't reroll the saving throw to determine if a psychic imprint is false. You can still use
psychometry only once per day.

### Unchained Rogue Skill Unlocks

**Sources:** Pathfinder Unchained pg 82\
If using [skill unlocks](ref/rule/skill-unlocks), with sufficient ranks in Appraise, you earn the
following.

**5 Ranks**

**Details:** A successful DC 20 Appraise check reveals whether an item is magical, and a second
check (DC = 25 + the item's caster level) unveils its properties. You can use Appraise to detect
non-written forgeries and counterfeits.

**10 Ranks**

**Details:** You can determine the most expensive object a creature is wearing or wielding (or in a
5-foot cube) as a **standard action** by succeeding at a DC 20 check. You never make a wildly
inaccurate appraisal of an item's value.

**15 Ranks**

**Details:** Determining the most expensive object as above is a **move action**. You can substitute
an Appraise check at a -10 penalty for a Will save to disbelieve a figment or glamer.

**20 Ranks**

**Details:** Determining the most expensive object as above is a **move action**, and if the check
succeeds, you gain a +2 circumstance bonus on combat maneuver checks to steal that object or disarm
a creature of that object for 1 minute.
