+++
id = "ref/arc-paladin/banishing-warden"
kind = "archetype"
title = "Banishing Warden"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "banishing_warden", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "18"

[fields]
kind = "archetype"
replaces = ["3rd-level mercy"]
alters = ["Smite evil", "Aura of justice"]
+++

The banishing warden is an expert at fighting all types of evil outsiders and sending them back to
their native planes.

**Gained class skills:** kp

**Lost class skills:** kno

**Smite Evil (Su)**

**Alters:** Smite evil

**Info:** A banishing warden's _smite evil_ deals its bonus damage only on the first attack against
outsiders (but not dragons or undead). However, it damages any evil outsider, not only those with
the evil subtype (including [native](ref/subtype/native) outsiders).

**Banishing Smite (Su)**

**Ability:** When the banishing warden confirms a critical hit against a target of her _smite evil_
effect, she can attempt to forcibly [banish](ref/spell/banishment) the target to its home plane. The
creature struck must succeed at a Will save (DC = 10 + half the banishing warden's level + the
banishing warden's Charisma modifier) or be sent back to its home plane as per
[dismissal](ref/spell/dismissal).

**At 10th Level:** A creature dismissed in this manner takes an amount of damage equal to 2 points
per paladin level at the start of its next turn.

**Gained:** At 3rd Level

**Replaces:** 3rd-level mercy

**Special:** A banishing warden still receives the benefits of the _mercy_ class ability starting at
6th level and onward.

**Usage:** 1 time/day + 1 per 6 paladin levels beyond 3rd

**Smiting Aura (Su)**

**Ability:** When an ally of the banishing warden is affected by her _aura of justice,_ that ally
can use _banishing smite._ This counts toward the banishing warden's number of uses per day and
cannot be activated if the banishing warden has no uses of _banishing smite_ remaining.

**Alters:** Aura of justice

**Gained:** At 11th Level
