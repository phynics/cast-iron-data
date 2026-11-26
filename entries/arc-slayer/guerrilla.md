+++
id = "ref/arc-slayer/guerrilla"
kind = "archetype"
title = "Guerrilla"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Guerrilla"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guerrilla", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "87"

[fields]
kind = "archetype"
features = [
  { anchor = "strike-first-strike-last", level = 1 },
  { anchor = "quick-start", level = 6 },
  { anchor = "astonishing-strike", level = 14 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["strike-first-strike-last"] },
  { replaces = "swift tracker", feature = "swift-tracker", by = ["strike-first-strike-last"] },
  { replaces = "6th-level slayer talent", feature = "slayer-talents", levels = [6], by = ["quick-start"] },
  { replaces = "Quarry", feature = "quarry", by = ["astonishing-strike"] },
  { replaces = "improved quarry", feature = "improved-quarry", by = ["astonishing-strike"] },
]
+++

Slayers characterized by cunning and patience, guerrillas specialize in ambush and harassment of
enemies.

## Strike First, Strike Last (Ex) {#strike-first-strike-last}

A guerrilla adds half his level on Stealth checks when remaining motionless and reduces the penalty
on Stealth checks when sniping by an equal amount. He also gains this bonus on his initiative checks
in surprise rounds whenever he is aware of the surprise round and at least one enemy is unaware.

This replaces track and swift tracker.

## Quick Start (Ex) {#quick-start}

At 6th level, the guerrilla can take a normal [charge](ref/rule/charge) action during the surprise
round, rather than a charge with half the usual distance.

This replaces the 6th-level slayer talent.

## Astonishing Strike (Ex) {#astonishing-strike}

At 14th level, when the guerrilla deals sneak attack damage to a target of his studied target
ability during the surprise round, that target is denied its Dexterity bonus to AC against attacks
from the same guerrilla until the end of the guerrilla's next turn. When the guerrilla reaches 19th
level, this ability works any time he deals sneak attack damage to a target of his studied target
ability during the first round of combat, whether or not it's a surprise round.

This replaces quarry and improved quarry.
