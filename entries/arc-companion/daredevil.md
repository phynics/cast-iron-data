+++
id = "ref/arc-companion/daredevil"
kind = "archetype"
title = "Daredevil"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daredevil", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "187"

[fields]
kind = "archetype"
features = [
  { anchor = "artful-acrobat" },
  { anchor = "uncanny-dodge", level = 6 },
  { anchor = "devil-may-care", level = 9 },
]
trades = [
  { replaces = "Share Spells", by = ["artful-acrobat"] },
  { replaces = "Devotion", by = ["uncanny-dodge"] },
  { replaces = "Multiattack", by = ["devil-may-care"] },
]
+++

Daredevil companions join the fray with graceful leaps or swooping dives, heedless of the danger.

## Artful Acrobat (Ex) {#artful-acrobat}

A daredevil gains a competence bonus on Acrobatics checks equal to
[half](ref/misc/fractions-and-rounding) its Hit Dice.

This replaces share spells.

## Uncanny Dodge (Ex) {#uncanny-dodge}

At 6th level, a daredevil gains [Mobility](ref/feat/mobility) as a bonus feat without needing to
meet the prerequisites. If it already has Mobility, it gains [Spring Attack](ref/feat/spring-attack)
instead.

This replaces devotion.

## Devil May Care (Ex) {#devil-may-care}

At 9th level, a daredevil can't be flanked.

This replaces Multiattack.
