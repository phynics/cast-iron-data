+++
id = "ref/skill/heal"
kind = "rule"
title = "Heal"
source_ids = ["core-rulebook", "occult-adventures", "technology-guide", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heal", path = "json/skills.json" },
]
[[sources]]
publication = "core-rulebook"
page = "98"

[fields]
kind = "none"
+++

**Associated Skill**

**Details:** Wisdom

**Trained Only**

**Details:** No

**Armor Check Penalty**

**Details:** No

**Optional Unchained Skill**

**Details:** No

**Optional Background Skill**

**Details:** No

### Check

The DC and effect of a Heal check depend on the task you attempt.

|Task|DC|
| --- | --- |
|First aid|15|
|Long-term care|15|
|Treat wounds from caltrops, spike growth, or spike stones|15|
|Treat deadly wounds|20|
|Treat poison|Poison's save DC|
|Treat disease|Disease's save DC|

### Action

Varies

### Try Again

Varies. Generally speaking, you can't try a Heal check again without witnessing proof of the
original check's failure.

### Special

A character with the [Self-Sufficient](ref/feat/self-sufficient) feat gets a bonus on Heal checks.

A [healer's kit](ref/eq-misc/healers-kit) gives you a +2 circumstance bonus on Heal checks.

Heal is also used in the [harvesting poison](ref/rule/harvesting-poisons) rules in the creation of
antivenoms.

### First Aid and Poison

You usually use first aid to save a [dying](ref/misc/dying) character. If a character has negative
hit points and is losing hit points (at the rate of 1 per round, 1 per hour, or 1 per day), you can
make him [stable](ref/misc/stable). A stable character regains no hit points but stops losing them.
First aid also stops a character from losing hit points due to effects that cause
[bleed](ref/rule/bleed).

To treat poison means to tend to a single character who has been poisoned and who is going to take
more damage from the poison (or suffer some other effect). Every time the poisoned character makes a
saving throw against the [poison](ref/rule/poisons), you make a Heal check. If your Heal check
exceeds the DC of the poison, the character receives a +4 competence bonus on his saving throw
against the poison.

### Action

Providing first aid, treating a wound, or treating poison is a **standard action**.

### Try Again

Generally speaking, you can't try a Heal check again without witnessing proof of the original
check's failure. You can always retry a check to provide first aid, assuming the target of the
previous attempt is still alive.

### Long-Term Care

Providing long-term care means treating a wounded person for a day or more. If your Heal check is
successful, the patient recovers hit points or ability score points lost to ability damage at twice
the normal rate: 2 hit points per level for a full 8 hours of rest in a day, or 4 hit points per
level for each full day of complete rest; 2 ability score points for a full 8 hours of rest in a
day, or 4 ability score points for each full day of complete rest.

You can tend to as many as six patients at a time. You need a few items and supplies (bandages,
salves, and so on) that are easy to come by in settled lands. Giving long-term care counts as light
activity for the healer. You cannot give long-term care to yourself.

### Action

Providing long-term care requires 8 hours of light activity.

### Treat Mobility Wounds

A creature wounded by stepping on a caltrop moves at half normal speed. A successful Heal check
removes this movement penalty.

A creature wounded by a [spike growth](ref/spell/spike-growth) or
[spike stones](ref/spell/spike-stones) spell must succeed on a Reflex save or take injuries that
reduce his speed by one-third. Another character can remove this penalty by taking 10 minutes to
dress the victim's injuries and succeeding on a Heal check against the spell's save DC.

### Action

Tending a creature wounded by [caltrops](ref/eq-misc/caltrops) or a
_[spike growth](ref/spell/spike-growth)_ or _[spike stones](ref/spell/spike-stones)_ spell takes 10
minutes of work.

### Treat Deadly Wounds

When treating deadly wounds, you can restore hit points to a damaged creature. Treating deadly
wounds restores 1 hit point per level of the creature. If you exceed the DC by 5 or more, add your
Wisdom modifier (if positive) to this amount. A creature can only benefit from its deadly wounds
being treated within 24 hours of being injured and never more than once per day. You must expend two
uses from a healer's kit to perform this task. You take a -2 penalty on your Heal skill check for
each use from the healer's kit that you lack.

### Action

Treating deadly wounds takes 1 hour of work.

### Treat Disease

To treat a disease means to tend to a single diseased character. Every time the diseased character
makes a saving throw against disease effects, you make a Heal check. If your Heal check exceeds the
DC of the [disease](ref/rule/diseases), the character receives a +4 competence bonus on his saving
throw against the disease.

### Action

Treating a disease takes 10 minutes of work.

### Occult Skill Unlocks

[Occult skill unlocks](ref/rule/occult-skill-unlocks) are available to those using the occult rules
and meet certain requirements.

#### Faith Healing

**Sources:** Occult Adventures pg 195\
You apply esoteric principles to temporarily suspend or remove curses, diseases, and ability damage.

##### Check

You can use faith healing once per day. The DC and effect of the Heal check depend on the task you
attempt. You can't use faith healing on yourself.

###### Restore Vitality

You suppress [ability damage](ref/rule/ability-damage-drain). You perform a 1-hour ceremony, after
which you attempt a Heal check against the DC of the effect that caused the ability damage. If you
succeed at the check, you temporarily suppress 1 point of ability damage for 1 hour, plus 1
additional point and hour for every 5 by which the check result exceeds the DC. A creature can
benefit from this treatment no more than once per day.

###### Suspend Affliction

You treat one curse, disease, or poison affecting a creature. You enter into a deep trance for 1
hour while you treat the subject, after which you attempt your Heal check. If the check is
successful, you suspend the effects of the [affliction](ref/rule/afflictions) by 1 hour, plus 1 hour
for every 5 by which you exceed the DC. This time doesn't count against the effect's duration (if
any). The affliction can still be cured by other means while it's suspended.

###### Remove Affliction

You can attempt to permanently remove an affliction in an 8-hour ceremony, after which you attempt a
Heal check. If the result of the check is at least double the DC of the original affliction, the
sufferer can attempt another saving throw using the original DC to permanently cast off the effect.

|Task|DC|
| --- | --- |
|Restore vitality|Effect's save DC|
|Suspend affliction|Affliction's save DC|
|Remove affliction|Double the affliction's save DC|

##### Action

Restoring vitality and suspending afflictions each require 1 hour in a quiet environment. Permanent
removal of afflictions requires 8 hours of heavy activity.

##### Try Again

Varies. A creature can't be the subject of faith healing more than once per day. You can't try to
permanently remove an affliction again.

### Researching Technology

**Sources:** Technology Guide pg 5\
When using the [technological equipment](ref/rule/technological-equipment) rules, a character can
use Heal to identify and understand pharmaceuticals.

### Unchained Rogue Skill Unlocks

**Sources:** Pathfinder Unchained pg 84\
If using [skill unlocks](ref/rule/skill-unlocks), with sufficient ranks in Heal, you earn the
following.

**5 Ranks**

**Details:** When you treat deadly wounds, the target recovers hit points and ability damage as if
it had rested for a full day.

**10 Ranks**

**Details:** When you treat deadly wounds, the target recovers hit points as if it had rested for a
full day with long-term care.

**15 Ranks**

**Details:** When you treat deadly wounds, the creature recovers hit point and ability damage as if
it had rested for 3 days.

**20 Ranks**

**Details:** When you treat deadly wounds, the target recovers hit point and ability damage as if it
had rested for 3 days with long-term care.
