+++
id = "ref/arc-ranger/wild-hunter"
kind = "archetype"
title = "Wild Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Wild%20Hunter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_hunter", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-class-guide"
page = "108"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-focus", level = 1 },
  { anchor = "shared-focus", level = 7 },
]
trades = [
  { replaces = "All instances of the favored enemy class ability", feature = "favored-enemy", by = ["animal-focus"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["shared-focus"] },
  { replaces = "swift tracker", feature = "swift-tracker", by = ["shared-focus"] },
]
+++

A wild hunter seeks to emulate the animals around him to keep him safe while he tracks his prey.
Instead of studying the traits and behaviors of a _favored enemy,_ a wild hunter studies those of
various animals, incorporating those attributes into his hunting strategy.

## Animal Focus (Su) {#animal-focus}

At 1st level, as a swift action a wild hunter can take on the
[aspect of an animal](ref/ability/animal-foci), gaining a bonus or special ability based on the type
of animal emulated. This functions as the hunter's animal focus class feature (see page 27), though
this only applies to the wild hunter and not an animal companion (see shared focus, below). The wild
hunter can use this ability for 1 minute per day per ranger level. This duration does not need to be
consecutive, but it must be spent in 1-minute increments. He can only emulate one animal at a time.
This ability replaces all instances of the favored enemy class ability.

## Shared Focus (Su) {#shared-focus}

At 7th level, a wild hunter can share his current animal focus with one creature appropriate to his
hunter's bond. If the wild hunter's bond is with an animal companion, the companion automatically
gains the benefits of the wild hunter's current animal focus. If the wild hunter's bond is with his
companions, as a swift action he can select one bonded ally to gain the benefits of the hunter's
current animal focus; this lasts until the hunter's bond ends, the animal focus ends for the wild
hunter, or the wild hunter selects a different companion. This ability replaces woodland stride and
swift tracker.
