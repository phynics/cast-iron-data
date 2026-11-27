+++
id = "ref/arc-paladin/banishing-warden"
kind = "archetype"
title = "Banishing Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Banishing%20Warden"
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
features = [
  { anchor = "smite-evil", level = 1 },
  { anchor = "banishing-smite", level = 3 },
  { anchor = "smiting-aura", level = 11 },
]
trades = [
  { replaces = "Mercy gained at 3rd level", feature = "mercy", levels = [3], by = ["banishing-smite"] },
  { alters = "Smite evil", feature = "smite-evil", by = ["smite-evil"] },
  { alters = "Aura of justice", feature = "aura-of-justice", by = ["smiting-aura"] },
]
+++

The banishing warden is an expert at fighting all types of evil outsiders and sending them back to
their native planes.

## Class Skills {#class-skills}

A banishing warden gains Knowledge (planes) as a class skill but does not gain Knowledge (nobility)
as a class skill.

## Smite Evil (Su) {#smite-evil}

A banishing warden's smite evil deals its bonus damage only on the first attack against outsiders
(but not dragons or undead). However, it damages any evil outsider, not only those with the evil
subtype (including [native](ref/subtype/native) outsiders).

This modifies smite evil.

## Banishing Smite (Su) {#banishing-smite}

At 3rd level, once per day when the banishing warden confirms a critical hit against a target of her
smite evil effect, she can attempt to forcibly [banish](ref/spell/banishment) the target to its home
plane. The creature struck must succeed at a Will save (DC = 10 + half the banishing warden's
level + the banishing warden's Charisma modifier) or be sent back to its home plane as per
_[dismissal](ref/spell/dismissal)_. At 10th level, a creature dismissed in this manner takes an
amount of damage equal to 2 points per paladin level at the start of its next turn. The banishing
warden gains an additional daily use of this ability at 9th and 15th level.

This ability replaces the mercy gained at 3rd level. A banishing warden still receives the benefits
of the mercy class ability starting at 6th level and onward.

## Smiting Aura (Su) {#smiting-aura}

At 11th level, when an ally of the banishing warden is affected by her aura of justice, that ally
can use banishing smite. This counts toward the banishing warden's number of uses per day and cannot
be activated if the banishing warden has no uses of banishing smite remaining.

This ability modifies aura of justice.
