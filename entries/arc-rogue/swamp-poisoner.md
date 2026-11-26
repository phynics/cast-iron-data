+++
id = "ref/arc-rogue/swamp-poisoner"
kind = "archetype"
title = "Swamp Poisoner"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Swamp%20Poisoner"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swamp_poisoner", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "potions-and-poisons"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "mucous-membrane", level = 1 },
  { anchor = "mark-the-vein", level = 2 },
  { anchor = "poison-the-well", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["mucous-membrane"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["mark-the-vein"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["poison-the-well"] },
  { replaces = "Danger sense", by = ["poison-the-well"] },
]
+++

Swamp poisoners use their own toxins to defend their homes and level the playing field. The swamp
poisoner is an archetype available to grippli characters, and it is appropriate for rogues built
using the rules from the _Pathfinder RPG Core Rulebook_ as well as for unchained rogues (_Pathfinder
RPG Pathfinder Unchained_ 20).

## Prerequisites {#prerequisites}

A swamp poisoner must have selected the toxic skin grippli alternate racial trait.

## Mucous Membrane (Ex) {#mucous-membrane}

A swamp poisoner gains a bonus equal to half his class level on Escape Artist checks and to his CMD
when resisting grapple attempts (minimum 1).

This replaces trapfinding.

## Mark the Vein (Ex) {#mark-the-vein}

At 2nd level, when the swamp poisoner attacks a target that is currently affected by his grippli
racial poison, that target is denied its Dexterity bonus to AC. The target must be actively
poisoned, not just suffering the effects of poison, such as lingering ability damage.

This replaces the rogue talent gained at 2nd level.

## Poison the Well (Ex) {#poison-the-well}

At 3rd level as a standard action, a swamp poisoner can smear the poison generated through the use
of his toxic skin alternate racial trait onto the ground in a 5-foot area, instead of onto a weapon
or his own body. The first creature other than the swamp poisoner to enter the area is exposed to
the poison. The poison loses its potency after 1 hour. This area is considered a
[trap](ref/rule/traps), and the DCs of Perception checks to notice it and Disable Device checks to
disable it are equal to 10 + half the swamp poisoner's level + the swamp poisoner's Constitution
modifier.

The swamp poisoner also gains an extra use per day of his toxic skin alternate racial trait, plus
one additional use per day for every 3 levels beyond 3rd.

This replaces trap sense. An unchained rogue replaces danger sense instead.
