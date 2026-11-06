+++
id = "ref/rule/mythic-subtype"
kind = "rule"
title = "Mythic Subtype"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mythic_subtype", path = "json/rules_campaign_types06.json" },
]

[fields]
kind = "none"
+++

**Sources:** Mythic Adventures pg 226

A creature with this subtype is infused with mythic power and is capable of terrible and
awe-inspiring feats. Creatures with the mythic subtype gain the following abilities.

**Mythic Rank:** A creature with the mythic subtype gains 1 to 10 mythic ranks, representing its
overall mythic power. Its rank is generally equal to 1/2 its original CR.

**Natural Armor Bonus:** Add the creature's mythic rank to its natural armor bonus. A creature
without natural armor has an effective natural armor bonus of +0.

**Bonus Hit Points:** A creature with d6 Hit Dice gains 6 hit points per mythic rank, a creature
with d8 Hit Dice gains 8 hit points per rank, and a creature with d10 or d12 Hit Dice gains 10 hit
points per rank. Note that this is the same number of bonus hit points the creature would gain if it
had a [mythic simple template](ref/rule/mythic-simple-templates).

**Damage Reduction:** A creature with 5 to 10 Hit Dice gains DR 5/epic. A creature with 11 or more
Hit Dice gains DR 10/epic.

If the creature already has [damage reduction](ref/rule/damage-reduction), it adds epic to the
qualities needed to bypass that reduction. If the damage reduction granted from this subtype has a
larger numerical value than the creature's original damage reduction, increase the creature's
original damage reduction to the amount of the epic DR. For example, a monster with DR 5/bludgeoning
that gains DR 10/epic from the mythic subtype gains DR 10/bludgeoning and epic.

**Spell Resistance:** If the creature has [spell resistance](ref/rule/spell-resistance), add its
mythic rank to its spell resistance.

**Mythic Power:** The creature gains the [mythic power](ref/umr/mythic-power) and
[surge](ref/umr/surge) universal monster abilities. The monster's surge die depends on its rank, as
summarized in Table 6-5: Mythic Subtype Abilities.

**Ability Bonus:** At 2nd rank and every 2 ranks thereafter, the monster gains a permanent +2 bonus
to an ability score. If it has multiple bonuses, it can apply them to the same ability score or to
different ability scores.

**Mythic Feats:** At 1st rank and every 2 ranks thereafter, the monster gains a mythic feat. It must
meet all of the prerequisites for this feat.

**Additional Mythic Abilities:** The monster gains a number of mythic abilities equal to its MR + 1.
Such abilities can be drawn from the regular [mythic path](ref/rule/mythic-paths) abilities or the
mythic abilities listed with the monsters, or it can be a new ability you create by taking
inspiration from those abilities. These abilities should be thematically appropriate for the
creature.

Some new monster abilities are especially powerful; at the GM's discretion, they can count as two
abilities toward this total. For example, the
[mythic fire giant's](ref/monster/giant-fire-giant-mythic) fire vortex ability could count as two
mythic abilities. In place of a mythic ability, the monster may gain a universal monster ability,
such as [rend](ref/umr/rend) or [pounce](ref/umr/pounce).

**CR:** When you're finished adding abilities to the monster, add 1/2 the monster's mythic rank to
its CR to determine its new CR. Evaluate the monster at its new CR using
[Table 6-8: Monster Statistics by CR](ref/rule/evaluating-monster-statistics) to make sure it falls
within the expected values for its new CR.

**XP:** Change the creature's [XP award to match its new CR](ref/rule/awarding-experience).

### Table 6-5: Mythic Subtype Abilities

|Mythic Rank|Ability Bonus|Mythic Feat|Surge Die Type|
| --- | --- | --- | --- |
|1st|-|1st|1d6|
|2nd|1st|-|1d6|
|3rd|-|2nd|1d6|
|4th|2nd|-|1d8|
|5th|-|3rd|1d8|
|6th|3rd|-|1d8|
|7th|-|4th|1d10|
|8th|4th|-|1d10|
|9th|-|5th|1d10|
|10th|5th|-|1d12|
