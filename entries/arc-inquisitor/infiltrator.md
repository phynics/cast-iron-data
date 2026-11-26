+++
id = "ref/arc-inquisitor/infiltrator"
kind = "archetype"
title = "Infiltrator"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Infiltrator"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infiltrator", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-magic"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "misdirection", level = 1 },
  { anchor = "guileful-lore", level = 1 },
  { anchor = "forbidden-lore" },
  { anchor = "necessary-lies" },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["guileful-lore"] },
  { replaces = "Track", feature = "track", by = ["forbidden-lore"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["necessary-lies"] },
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["misdirection"] },
]
+++

This inquisitor uses guile and deception to blend in among the enemies of the faith rather than
confronting them head-on.

## Misdirection (Sp) {#misdirection}

At 1st level, each day when the infiltrator prepares spells, she may choose an alignment. She
detects as that alignment as if she had used _[misdirection](ref/spell/misdirection)_ on a creature
with that alignment (this does not change any divination results about her other than her
alignment). This power replaces stern gaze.

## Guileful Lore (Ex) {#guileful-lore}

At 1st level, the infiltrator's will is bent toward subterfuge and deception. She adds her Wisdom
modifier on Bluff and Diplomacy skill checks in addition to the normal ability score modifiers. This
ability replaces monster lore.

## Forbidden Lore (Ex) {#forbidden-lore}

While other inquisitors learned to track unbelievers, an infiltrator learns how to cast their
spells. An infiltrator can cast spells of an alignment opposed to her or her deity (ignoring the
restriction in the Chaotic, Evil, Good, and Lawful Spells class ability). This ability replaces
track.

## Necessary Lies (Su) {#necessary-lies}

An infiltrator adds her class level on saving throws against abilities that detect lies or reveal or
force the truth, such as _detect lies_ and _[zone of truth](ref/spell/zone-of-truth)_. This power
replaces [discern lies](ref/spell/discern-lies).
