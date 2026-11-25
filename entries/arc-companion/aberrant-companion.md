+++
id = "ref/arc-companion/aberrant-companion"
kind = "archetype"
title = "Aberrant Companion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aberrant_companion", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "186"

[fields]
kind = "archetype"
features = [
  { anchor = "not-quite-animal" },
  { anchor = "aberrant-sight" },
  { anchor = "alien-mind", level = 6 },
  { anchor = "fluid-bones", level = 9 },
]
trades = [
  { replaces = "Share Spells", by = ["aberrant-sight"] },
  { replaces = "Devotion", by = ["alien-mind"] },
  { replaces = "Multiattack", by = ["fluid-bones"] },
  { replaces = "The +2 natural armor increase at 9th level", by = ["fluid-bones"] },
]
+++

There's something oddly wrong about aberrant companions. Yet though they're touched by eldritch
magic or mutated by strange influences, they are still loyal, if unnatural, allies.

## Aberrant Skills {#aberrant-skills}

Aberrant companions treat Escape Artist and Intimidate as class skills.

## Not Quite Animal {#not-quite-animal}

The DC to use Handle Animal on an aberrant companion is 5 higher, as if it were a nonanimal with an
Intelligence score of 1 or 2.

## Aberrant Sight (Ex) {#aberrant-sight}

An aberrant companion gains [darkvision](ref/rule/darkvision) with a range of 60 feet.

This replaces share spells.

## Alien Mind (Ex) {#alien-mind}

At 6th level, an aberrant companion is immune to mind-affecting effects that specifically target
animals, such as _[charm animal](ref/spell/charm-animal)_. Anyone who attempts to use such an effect
against it takes 1d4 points of [Wisdom damage](ref/rule/ability-damage-drain) (Will DC 20 half).

This replaces devotion.

## Fluid Bones (Ex) {#fluid-bones}

At 9th level, an aberrant companion gains [compression](ref/umr/compression) as per the universal
monster rule, though it can use the ability while carrying a rider only if the rider has
compression.

This replaces Multiattack and the +2 natural armor increase at 9th level.
