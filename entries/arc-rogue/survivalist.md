+++
id = "ref/arc-rogue/survivalist"
kind = "archetype"
title = "Survivalist"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Survivalist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "survivalist", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-combat"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "hardy", level = 1 },
  { anchor = "endure-elements", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["hardy"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["endure-elements"] },
]
+++

The survivalist focuses her talents on surviving harsh and unforgiving conditions that would kill a
lesser rogue. Whether in blazing deserts or frigid arctic wastes - or simply the cold, hard reality
of the streets - the survivalist uses her training to both ensure her own success and provide for
the safety of her allies.

## Hardy (Ex) {#hardy}

At 1st level, a survivalist is already prepared to endure extreme hardships and environmental
conditions. She can go twice the normal number of days without water and triple the normal number of
days without food before feeling the effects of either thirst or starvation. This ability replaces
trapfinding.

## Endure Elements (Sp) {#endure-elements}

At 3rd level, a survivalist rogue can use _[endure elements](ref/spell/endure-elements)_ once per
day as a [spell-like ability](ref/umr/spell-like-abilities). The survivalist's caster level is the
same as her rogue level. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the survivalist archetype: hold breath, iron guts,
resiliency, strong stroke, survivalist, terrain mastery, and wall scramble.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the survivalist archetype: another day, defensive
roll, feat, and skill mastery.
