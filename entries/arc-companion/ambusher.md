+++
id = "ref/arc-companion/ambusher"
kind = "archetype"
title = "Ambusher"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ambusher", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "186"

[fields]
kind = "archetype"
features = [
  { anchor = "camouflage" },
  { anchor = "cunning-ambusher", level = 3 },
]
trades = [
  { replaces = "Share Spells", by = ["camouflage"] },
  { replaces = "Improved Evasion", by = ["camouflage"] },
  { replaces = "Evasion", by = ["cunning-ambusher"] },
  { replaces = "Devotion", by = ["cunning-ambusher"] },
  { replaces = "Multiattack", by = ["cunning-ambusher"] },
]
+++

Ambushers sneak up on unsuspecting prey, pouncing on targets when they least expect it.

## Camouflage (Ex) {#camouflage}

An ambusher gains a +4 racial bonus on Stealth checks in its natural environment (if this is
unclear, use the environment in its _Bestiary_ entry). At 15th level, an ambusher can use the
Stealth skill to hide in its natural environment, even if the environment doesn't grant
[cover](ref/rule/cover) or [concealment](ref/rule/concealment).

This replaces share spells and improved evasion.

## Cunning Ambusher (Ex) {#cunning-ambusher}

At 3rd level, an ambusher gains [uncanny dodge](ref/ability/uncanny-dodge). At 6th level, an
ambusher gains a +2 racial bonus on initiative checks, and during the surprise round, opponents are
always considered [flat-footed](ref/rule/flat-footed) against the ambusher's attacks, even if they
have already acted. At 9th level, an ambusher gains a +2 morale bonus on attack and damage rolls
during a surprise round.

This replaces evasion, devotion, and Multiattack.
