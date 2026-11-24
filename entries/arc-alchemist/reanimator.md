+++
id = "ref/arc-alchemist/reanimator"
kind = "archetype"
title = "Reanimator"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Reanimator"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reanimator", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-magic"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "bomb", level = 1 },
  { anchor = "simple-reanimation", level = 7 },
  { anchor = "create-undead", level = 13 },
  { anchor = "create-greater-undead", level = 15 },
]
trades = [
  { replaces = "Increase to bomb damage at this level", by = ["simple-reanimation", "create-undead", "create-greater-undead"] },
  { replaces = "Bombs", feature = "bomb", by = ["bomb"] },
]
+++

A reanimator is an alchemist who has discovered how to infuse a corpse with a semblance of life.
Many work in tandem with necromancers to explore the fine border between the worlds of the living
and the dead. A reanimator has the following class features.

## Bomb {#bomb}

A reanimator's bombs deal damage [one die step](ref/misc/damage-die-adjustments) lower than normal
(regular bombs deal d4s, [concussive bombs](ref/discovery/concussive-bomb) deal 1d3s, and so on).
This ability otherwise functions as and replaces the standard alchemist bomb class feature.

## Simple Reanimation {#simple-reanimation}

At 7th level, a reanimator adds _[lesser animate dead](ref/spell/animate-dead-lesser)_ to his
formula book as a 3rd-level extract. When he uses that extract, rather than drinking it, he injects
it into the corpse he intends to animate, which rises as an undead creature under his control 1 hour
later. The extract can only create [zombies](ref/template/zombie) (including variant zombies). This
ability replaces the increase to bomb damage at this level.

## Create Undead {#create-undead}

At 13th level, a reanimator adds _[create undead](ref/spell/create-undead)_ to his formula book as a
4th-level extract. When he uses that extract, rather than drinking it, he injects it into the corpse
he intends to animate, which rises as an uncontrolled undead 1 hour later. The extract can only
create corporeal undead. This ability replaces the increase to bomb damage at this level.

## Create Greater Undead {#create-greater-undead}

At 15th level, a reanimator adds _[create greater undead](ref/spell/create-greater-undead)_ to his
formula book as a 5th-level extract. This otherwise acts similarly to a
_[create undead](ref/spell/create-undead)_ extract. This ability replaces the increase to bomb
damage at this level.

## Discoveries {#discoveries}

The following discoveries complement the reanimator archetype:
[alchemical zombie](ref/discovery/alchemical-zombie),
[elixir of life](ref/discovery/elixir-of-life), [eternal potion](ref/discovery/eternal-potion),
[mummification](ref/discovery/mummification), and [preserve organs](ref/discovery/preserve-organs).
