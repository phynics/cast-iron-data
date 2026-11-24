+++
id = "ref/arc-rogue/underground-chemist"
kind = "archetype"
title = "Underground Chemist"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Underground%20Chemist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "underground_chemist", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-class-guide"
page = "109"

[fields]
kind = "archetype"
features = [
  { anchor = "chemical-weapons", level = 2 },
  { anchor = "precise-splash-weapons", level = 4 },
  { anchor = "discovery", level = 10 },
]
trades = [
  { replaces = "Evasion", feature = "evasion", by = ["chemical-weapons"] },
  { replaces = "Rogue talent gained at 4th level", feature = "rogue-talents", levels = [4], by = ["precise-splash-weapons"] },
  { alters = "Advanced talents", feature = "advanced-talents", by = ["discovery"] },
]
+++

Underground chemists are part of the rotting, fetid underbelly of the alchemical world. While
underground chemists can't hold a candle to dedicated alchemists, they're tricky and dangerous with
alchemical substances and potions.

## Chemical Weapons (Ex) {#chemical-weapons}

At 2nd level, an underground chemist is able to retrieve an alchemical item as if
[drawing a weapon](ref/rule/draw-or-sheathe-a-weapon). She adds her Intelligence modifier to damage
dealt with [splash weapons](ref/rule/throw-splash-weapon), including any splash damage. She adds 1/2
her level to Craft (alchemy) checks. This ability replaces evasion.

## Precise Splash Weapons (Ex) {#precise-splash-weapons}

At 4th level, an underground chemist can deal [sneak attack](ref/ability/sneak-attack) damage with
splash weapons. The attack must be her first attack that round, qualify for dealing sneak attack
damage (such as against a [flat-footed](ref/rule/flat-footed) target), and be directed at a creature
rather than a square. This ability replaces the rogue talent gained at 4th level.

## Discovery (Su) {#discovery}

At 10th level, an underground chemist can select one of the following alchemist discoveries
(_Advanced Player's Guide_ 28) in place of a rogue talent:
[concentrate poison](ref/discovery/concentrate-poison), [dilution](ref/discovery/dilution),
[enhance potion](ref/discovery/enhance-potion), [extend potion](ref/discovery/extend-potion),
[mummification](ref/discovery/mummification), [nauseating flesh](ref/discovery/nauseating-flesh),
[poison conversion](ref/discovery/poison-conversion),
[preserve organs](ref/discovery/preserve-organs),
[spontaneous healing](ref/discovery/spontaneous-healing), or
[sticky poison](ref/discovery/sticky-poison). She uses her rogue level as her alchemist level for
determining the effects of her discoveries and whether she is able to select one. This ability
alters advanced talents.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the underground chemist archetype: black market connections,
fast fingers, lasting poison, sniper's eye, and swift poison.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the underground chemist archetype: deadly cocktail
and thoughtful reexamining.
