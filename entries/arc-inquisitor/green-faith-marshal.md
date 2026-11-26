+++
id = "ref/arc-inquisitor/green-faith-marshal"
kind = "archetype"
title = "Green Faith Marshal"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Green%20Faith%20Marshal"
source_ids = ["ultimate-wilderness", "heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "green_faith_marshal", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "141"
[[sources]]
publication = "heroes-of-the-wild"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "power-of-nature", level = 1 },
  { anchor = "wild-lore", level = 1 },
  { anchor = "nature-s-ally", level = 5 },
  { anchor = "wild-step", level = 11 },
]
trades = [
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["power-of-nature"] },
  { replaces = "Monster lore", feature = "monster-lore", by = ["wild-lore"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["nature-s-ally"] },
  { replaces = "Stalwart", feature = "stalwart", by = ["wild-step"] },
  { alters = "Domain", feature = "domain", by = ["power-of-nature"] },
]
+++

The [Green Faith](ref/faith/green-faith) marshal serves as a literal force of nature, hunting down
and punishing those who have committed sins against nature through enslavement and mistreatment of
animals or destruction of wild places.

## Power of Nature {#power-of-nature}

A Green Faith marshal gains one domain selected from the
[animal and terrain domains](ref/ability/druid-domains). The 1st-though 6th-level bonus spells from
this domain are added to the Green Faith marshal's spell list.

This alters the inquisitor's domain ability and replaces stern gaze.

## Wild Lore (Ex) {#wild-lore}

A Green Faith marshal adds her Wisdom modifier to her Knowledge (nature) skill checks, in addition
to her Intelligence modifier.

This replaces monster lore.

## Nature's Ally (Sp) {#nature-s-ally}

At 5th level, a Green Faith marshal gains the ability to cast
_[commune with nature](ref/spell/commune-with-nature)_ once per week.

This replaces discern lies.

## Wild Step (Ex) {#wild-step}

At 11th level, a Green Faith marshal can move through any sort of naturally occurring
[difficult terrain](ref/rule/terrain-and-obstacles) (such as natural thorns, briars, overgrown
areas, and similar terrain) at her normal speed without taking damage or suffering any other
impairment. Terrain that is enchanted or magically manipulated to impede motion still affects her.

This replaces stalwart.
