+++
id = "ref/arc-alchemist/reanimator"
kind = "archetype"
title = "Reanimator"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reanimator", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["7th-level bomb damage increase", "13th-level bomb damage increase", "15th-level bomb damage increase"]
alters = ["Bombs"]
+++

**Sources:** Ultimate Magic pg 20\
A reanimator is an alchemist who has discovered how to infuse a corpse with a semblance of life.
Many work in tandem with necromancers to explore the fine border between the worlds of the living
and the dead. A reanimator has the following class features.

**Bomb**

**Ability:** A reanimator's bombs deal damage [one die step](ref/misc/damage-die-adjustments) lower
than normal (regular bombs deal d4s, [concussive bombs](ref/discovery/concussive-bomb) deal 1d3s,
and so on). This ability otherwise functions as and replaces the standard alchemist bomb class
feature.

**Alters:** Bombs

**Gained:** At 1st Level

**Simple Reanimation**

**Ability:** A reanimator adds [lesser animate dead](ref/spell/animate-dead-lesser) to his formula
book as a 3rd-level extract. When he uses that extract, rather than drinking it, he injects it into
the corpse he intends to animate, which rises as an undead creature under his control 1 hour later.
The extract can only create [zombies](ref/template/zombie) (including variant zombies).

**Gained:** At 7th Level

**Replaces:** 7th-level bomb damage increase

**Create Undead**

**Ability:** A reanimator adds [create undead](ref/spell/create-undead) to his formula book as a
4th-level extract. When he uses that extract, rather than drinking it, he injects it into the corpse
he intends to animate, which rises as an uncontrolled undead 1 hour later. The extract can only
create corporeal undead.

**Gained:** At 13th Level

**Replaces:** 13th-level bomb damage increase

**Create Greater Undead**

**Ability:** A reanimator adds [create greater undead](ref/spell/create-greater-undead) to his
formula book as a 5th-level extract. This otherwise acts similarly to a
_[create undead](ref/spell/create-undead)_ extract.

**Gained:** At 15th Level

**Replaces:** 15th-level bomb damage increase

**Discoveries:** The following discoveries complement the reanimator archetype:
[alchemical zombie](ref/discovery/alchemical-zombie),
[elixir of life](ref/discovery/elixir-of-life), [eternal potion](ref/discovery/eternal-potion),
[mummification](ref/discovery/mummification), and [preserve organs](ref/discovery/preserve-organs).
