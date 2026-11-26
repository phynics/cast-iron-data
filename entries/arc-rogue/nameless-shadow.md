+++
id = "ref/arc-rogue/nameless-shadow"
kind = "archetype"
title = "Nameless Shadow"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Nameless%20Shadow"
source_ids = ["merchants-manifest"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nameless_shadow", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "merchants-manifest"
page = "30"

[fields]
kind = "archetype"
features = [
  { anchor = "harmless-guise", level = 1 },
  { anchor = "face-in-the-crowd", level = 4 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["harmless-guise"] },
  { replaces = "rogue talents gained at 2nd, 6th, 10th, 14th, and 18th levels", feature = "rogue-talents", levels = [2, 6, 10, 14, 18], by = ["harmless-guise"] },
  { replaces = "Rogue talents gained at 4th and 8th levels", feature = "rogue-talents", levels = [4, 8], by = ["face-in-the-crowd"] },
]
+++

Where bandits and tyrants prey on merchants and caravans, the nameless shadow preys on bandits and
tyrants. Posing as mundane merchants or other harmless travelers, these assassins can hide both
within darkness and in the anonymity of a seemingly unimportant crowd. This archetype is appropriate
for rogues built using the rules from the _Pathfinder RPG Core Rulebook_ as well as for unchained
rogues (_Pathfinder RPG Pathfinder Unchained_ 20).

## Harmless Guise (Ex) {#harmless-guise}

A nameless shadow gains the dual identity and seamless guise [vigilante](ref/class/vigilante) class
features (_Pathfinder RPG Ultimate Intrigue_ 9–10), with the following restrictions. Her social
identity must be that of a mundane and nonthreatening member of society, such as a farmer or a
merchant. At 6th level, the nameless shadow gains the [many guises](ref/soctalent/many-guises)
vigilante social talent. At 8th level, the nameless shadow gains the
[quick change](ref/soctalent/quick-change) vigilante social talent. At 14th level, the nameless
shadow gains the [everyman](ref/soctalent/everyman) vigilante social talent. At 18th level, the
nameless shadow gains the [any guise](ref/soctalent/any-guise) vigilante social talent.

Additionally, when a nameless shadow attacks a foe while in a social or mundane identity, her target
takes a -2 penalty to AC for the purpose of resolving that attack. This use of harmless guise forces
the nameless shadow into her vigilante identity after the attack is completed, and the target (if it
survives) then becomes aware of the nameless shadow's secret. This ability cannot be used on targets
that are aware of the nameless shadow's dual identity.

This replaces trapfinding and the rogue talents gained at 2nd, 6th, 10th, 14th, and 18th levels.

## Face in the Crowd (Ex) {#face-in-the-crowd}

At 4th level, so long as there are at least 10 other nonhostile creatures within 30 feet of her, a
nameless shadow can use Bluff or Disguise in place of Stealth to hide or for sniping. At 8th level,
she can use this ability to hide within a crowd even if she is being observed.

This replaces the rogue talents gained at 4th and 8th levels.
