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
replaces = ["Favored enemy", "Woodland stride", "swift tracker"]
replaces_features = ["favored-enemy", "woodland-stride", "swift-tracker"]
+++

A wild hunter seeks to emulate the animals around him to keep him safe while he tracks his prey.
Instead of studying the traits and behaviors of a _favored enemy,_ a wild hunter studies those of
various animals, incorporating those attributes into his hunting strategy.

**Animal Focus (Su)**

**Gained:** At 1st Level

**Replaces:** Favored enemy

**Special:** He can only emulate one animal at a time.

**Swift:** A wild hunter can take on the [aspect of an animal](ref/ability/animal-foci), gaining a
bonus or special ability based on the type of animal emulated. This functions as the hunter's
_animal focus_ class feature, though this only applies to the wild hunter and not an animal
companion (see _shared focus,_ below).

**Usage:** 1 minute/day per ranger level; these minutes need not be consecutive, but must be spent
in 1-minute increments

**Shared Focus (Su)**

**Ability:** A wild hunter can share his current animal focus with one creature appropriate to his
_hunter's bond._ If the wild _hunter's bond_ is with an animal companion, the companion
automatically gains the benefits of the wild hunter's current animal focus. If the wild _hunter's
bond_ is with his companions, as a **swift action** he can select one bonded ally to gain the
benefits of the hunter's current animal focus; this lasts until the _hunter's bond_ ends, the animal
focus ends for the wild hunter, or the wild hunter selects a different companion.

**Gained:** At 7th Level

**Replaces:** Woodland stride, swift tracker
