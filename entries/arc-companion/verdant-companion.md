+++
id = "ref/arc-companion/verdant-companion"
kind = "archetype"
title = "Verdant Companion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "verdant_companion", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "189"

[fields]
kind = "archetype"
features = [
  { anchor = "not-quite-animal" },
  { anchor = "photosynthesis" },
  { anchor = "verdant-resistance" },
]
trades = [
  { replaces = "Share Spells", by = ["verdant-resistance"] },
  { replaces = "Evasion", by = ["verdant-resistance"] },
  { replaces = "Devotion", by = ["verdant-resistance"] },
  { replaces = "Improved Evasion", by = ["verdant-resistance"] },
]
+++

Favorites of druids who balance their responsibilities between flora and fauna, verdant companions
are animals with some of the abilities and physical aspects of plants.

## Not Quite Animal {#not-quite-animal}

The DC to use Handle Animal on a verdant companion is 5 higher, as if it were a nonanimal with an
Intelligence score of 1 or 2.

## Photosynthesis (Ex) {#photosynthesis}

As long as it stays in the sunlight for at least 8 hours per day, a verdant companion doesn't need
to eat. Otherwise, it eats normally for an animal of its kind.

## Verdant Resistance (Ex) {#verdant-resistance}

A verdant companion gains a +1 racial bonus on saving throws against mind-affecting effects,
paralysis, poison, polymorph, sleep effects, and stunning. This bonus increases to +2 at 3rd level,
+3 at 6th level, and +4 at 15th level. At 6th level, a verdant companion gains roots it can plant or
retract as a swift action. With its roots planted, it can't move, but it gains a +4 bonus to its CMD
against bull rush, pull, push, reposition, trip, and other combat maneuvers that would knock it over
or move it.

This replaces share spells, evasion, devotion, and improved evasion.
