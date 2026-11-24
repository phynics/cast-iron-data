+++
id = "ref/arc-druid/jungle-druid"
kind = "archetype"
title = "Jungle Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Jungle%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jungle_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "100"

[fields]
kind = "archetype"
features = [
  { anchor = "jungle-guardian", level = 2 },
  { anchor = "woodland-stride" },
  { anchor = "torrid-endurance", level = 4 },
  { anchor = "wild-shape" },
  { anchor = "verdant-sentinel", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["jungle-guardian"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["woodland-stride"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["torrid-endurance"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["verdant-sentinel"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

The fecund jungles of the equatorial regions are rich in life and ancient tradition; druidical
guardians of sacred pools, elder trees, and trembling volcanoes watch over crumbling temples and the
inevitable reclamation of lost civilizations by the beating heart of nature untamed.

## Jungle Guardian (Ex) {#jungle-guardian}

At 2nd level, a jungle druid gains a bonus on Initiative checks and Climb, Knowledge (geography),
Perception, Stealth, and Survival checks equal to 1/2 her druid level in jungle terrain, and she
cannot be tracked in such environments. This ability replaces woodland stride.

## Woodland Stride (Ex) {#woodland-stride}

A jungle druid gains this ability at 3rd level. This ability replaces trackless step.

## Torrid Endurance (Ex) {#torrid-endurance}

At 4th level, a jungle druid ignores the effects of a hot climate as if under the effects of
_[endure elements](ref/spell/endure-elements)_. She also gains a +4 bonus on saves against disease
and the exceptional abilities of animals and magical beasts. This ability replaces resist nature's
lure.

## Wild Shape (Su) {#wild-shape}

A jungle druid gains this ability at 6th level, except that her effective druid level for the
ability is equal to her druid level - 2.

## Verdant Sentinel (Ex) {#verdant-sentinel}

At 13th level, a jungle druid can cast _[tree shape](ref/spell/tree-shape)_ at will. This ability
replaces a thousand faces.
