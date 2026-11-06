+++
id = "ref/ragepower/savage-dirty-trick"
kind = "rule"
title = "Savage Dirty Trick"
source_ids = ["champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "savage_dirty_trick", path = "json/class_ability_rage_powers.json" },
]

[fields]
kind = "none"
+++

**&L&Savage Dirty Trick (Ex)&FN&**

**Action:** Ability

**Prereq:** 6th-level barbarian

**Provokes attack of opportunity:** No

**Usage:** Once per opponent per _rage_

**Usage:** Once per opponent per _rage_

Once per round while _raging,_ the barbarian can attempt a [dirty trick](ref/rule/dirty-trick)
combat maneuver in place of a melee attack. If successful, the target takes an amount of damage
equal to the barbarian's Strength modifier and must succeed at a Fortitude save (DC 10 + 1/2 the
barbarian's level + the barbarian's Strength modifier) or take an additional penalty from the dirty
trick based on the type of dirty trick performed and the following table.

|Initial Penalty|Additional Penalty|
| --- | --- |
|[Blinded](ref/misc/blinded)|[Staggered](ref/misc/staggered)|
|[Dazzled](ref/misc/dazzled)|[Dazed](ref/misc/dazed)|
|[Deafened](ref/misc/deafened)|Staggered|
|[Entangled](ref/rule/entangled)|Anchored in place and unable to move from that square|
|[Sickened](ref/misc/sickened)|[Nauseated](ref/misc/nauseated)|

On a failed Fortitude save, the opponent takes this additional penalty on top of the dirty trick's
original effect. The additional penalty lasts for 1 round (though the initial penalty lasts as long
as normal), and can be removed with a move action. The initial effect cannot be removed via mundane
means until the additional penalty is removed (though magical effects like
[remove blindness/deafness](ref/spell/remove-blindness-deafness) work). Removing the initial effect
also removes the additional penalty. If the target is immune to the initial penalty, then it is
unaffected by the additional penalty.

For example, a barbarian using this rage power attempts a dirty trick combat maneuver against her
opponent to blind him. She succeeds and her opponent fails his Fortitude save, so he becomes
staggered as well as blinded. Regardless of whether he had succeeded at his saving throw, the
opponent still takes an amount of damage from the barbarian's combat maneuver equal to the
barbarian's Strength modifier (unless he has [damage reduction](ref/rule/damage-reduction) or would
otherwise be able to prevent this damage). Likewise, if her opponent were immune to blinding
effects, he would not suffer from the blindness or the staggering effect, regardless of his saving
throw.
