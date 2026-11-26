+++
id = "ref/arc-kineticist/arakineticist"
kind = "archetype"
title = "Arakineticist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Arakineticist"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arakineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "living-curse" },
  { anchor = "accursed-shadow", level = 4 },
  { anchor = "curse-spinner", level = 6 },
  { anchor = "accursed-infusion", level = 13 },
]
trades = [
  { replaces = "Utility wild talent gained at 4th level", feature = "wild-talents", levels = [4], by = ["accursed-shadow"] },
  { replaces = "Utility wild talents gained at 6th and 8th levels", feature = "wild-talents", levels = [6, 8], by = ["curse-spinner"] },
  { replaces = "Utility wild talent gained at 13th level", feature = "wild-talents", levels = [13], by = ["accursed-infusion"] },
]
+++

Those of strong will who live under a dark curse long enough might learn to control and channel the
corrupt energy afflicting them. [Changelings](ref/race/changeling) who resist the call of their hag
mothers are especially given to the arts of the arakineticist.

## Living Curse {#living-curse}

An arakineticist's curse lives within her, granting her dark powers. She must choose void as her
primary [element](ref/ability/elements) (see _Pathfinder Player Companion:_

_Occult Origins_) and [negative blast](ref/kinetic/negative-blast) as her first simple blast.

## Accursed Shadow (Sp) {#accursed-shadow}

At 4th level, an arakineticist's curse casts a dark shadow over her soul, shielding her from death
magic. She gains a +2 bonus on saving throws against necromancy spells and death effects.

This bonus increases by 1 every 4 levels beyond 4th, to a maximum of +6 at 20th level.

This replaces the utility wild talent gained at 4th level.

## Curse Spinner (Sp) {#curse-spinner}

An arakineticist learns to wield her living curse like a needle to weave and unravel curses. At 6th
level, an arakineticist can accept 1 point of burn to cast _[remove curse](ref/spell/remove-curse)_
as a [spell-like ability](ref/umr/spell-like-abilities). At 8th level, she can accept 1 point of
burn to curse a target as _[bestow curse](ref/spell/bestow-curse)_ as
[spell-like ability](ref/umr/spell-like-abilities). Both of these abilities count as 4th-level
utility wild talents.

This replaces the utility wild talents gained at 6th and 8th levels.

## Accursed Infusion (Su) {#accursed-infusion}

At 13th level, an arakineticist's blasts can temporarily curse and bedevil her foe. On a failed Will
save, the target takes a -4 penalty on ability checks, attack rolls, saving throws, and skills
checks for 1 round as if it were affected by _[bestow curse](ref/spell/bestow-curse)_. A single
creature can't be affected by more than one curse from this infusion at a time. This is a 6th-level
substance infusion that costs 4 points of burn and can be used with negative and void blasts.

This replaces the utility wild talent gained at 13th level.
