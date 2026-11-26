+++
id = "ref/arc-rogue/waylayer"
kind = "archetype"
title = "Waylayer"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Waylayer"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "waylayer", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "staggering-reflexes", level = 1 },
  { anchor = "ambuscading-sneak-attack", level = 4 },
  { anchor = "danger-awareness", level = 8 },
  { anchor = "exceptional-reflexes", level = 12 },
  { anchor = "masterful-reflexes", level = 20 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["staggering-reflexes"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["ambuscading-sneak-attack"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["danger-awareness"] },
  { replaces = "Rogue talent gained at 12th level", feature = "rogue-talents", levels = [12], by = ["exceptional-reflexes"] },
  { replaces = "Rogue talent gained at 20th level", feature = "rogue-talents", levels = [20], by = ["masterful-reflexes"] },
]
+++

A clever rogue knows the easiest battle to win is the one that's over before your foe knows it has
begun. Some rogues thus specialize in setting up ambushes to catch their opponents off guard.

## Staggering Reflexes (Ex) {#staggering-reflexes}

At 1st level, a waylayer gains a bonus on initiative checks equal to 1/2 her level (minimum +1) if
she acts in a surprise round, and is never [flat-footed](ref/rule/flat-footed) at the start of
combat (even if she fails to act during the surprise round). This ability replaces trapfinding.

## Ambuscading Sneak Attack (Ex) {#ambuscading-sneak-attack}

At 4th level, a waylayer becomes especially skilled at attacking unaware foes. When she makes a
sneak attack during a surprise round, she uses d8s to roll sneak attack damage instead of d6s. This
ability replaces uncanny dodge.

## Danger Awareness (Ex) {#danger-awareness}

At 8th level, a waylayer is never considered an unaware combatant and is always able to act in the
surprise round. This replaces improved uncanny dodge.

## Exceptional Reflexes (Ex) {#exceptional-reflexes}

At 12th level, a waylayer can move up to her speed before taking her action in a surprise round.
This replaces the rogue talent gained at 12th level.

## Masterful Reflexes (Ex) {#masterful-reflexes}

At 20th level, a waylayer's initiative roll is automatically a natural 20. This ability replaces the
rogue talent gained at 20th level.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the waylayer archetype: camouflage, cunning trigger, quick
trapsmith, slow reactions, surprise attack, and underhanded.

## Advanced Talents {#advanced-talents}

The following advanced talents complement the waylayer archetype: entanglement of blades, hide in
plain sight, knock-out blow, and weapon snatcher.
