+++
id = "ref/arc-bard/averaka-arbiter"
kind = "archetype"
title = "Averaka Arbiter"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Averaka%20Arbiter"
source_ids = ["bastards-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "averaka_arbiter", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "bastards-of-golarion"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "inspire-teamwork", level = 3 },
  { anchor = "ritual-of-reconciliation", level = 8 },
  { anchor = "versatile-teamwork", level = 2 },
]
trades = [
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["inspire-teamwork"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["ritual-of-reconciliation"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["versatile-teamwork"] },
  { replaces = "well-versed", feature = "well-versed", by = ["versatile-teamwork"] },
]
+++

Some Averakan bards make it their mission to unify their fellow half-ores, and are equally skilled
at helping allies defeat common enemies and at building a new civilization that reflects their
unique identity.

## Bardic Performance {#bardic-performance}

An Averaka arbiter gains the following types of bardic performance.

## Inspire Teamwork (Ex) {#inspire-teamwork}

A 3rd-level Averaka arbiter can use his performance to treat his allies as if they possessed the
same teamwork feats as the bard for the purpose of determining whether the bard receives a bonus
from his teamwork feats. His allies do not receive any bonuses from these feats unless they actually
possess the feats themselves. The allies' positioning and actions must still meet the prerequisites
listed in the teamwork feat for the bard to receive the listed bonus. This performance replaces
inspire competence.

## Ritual of Reconciliation (Su) {#ritual-of-reconciliation}

An Averaka arbiter of 8th level or higher can use his performance to
[improve the attitudes](ref/skill/diplomacy) of nearby creatures by two steps. To be affected, a
creature must be within 30 feet and able to hear the bard. Creatures whose attitude toward the bard
becomes indifferent or better immediately cease attacking the bard and his allies, but may otherwise
act as they please. The effect persists for as long as the creature is within 30 feet and the bard
continues his performance. The effect ends if one of the bard's allies attacks the creature. A
successful Will saving throw (DC 10 + 1/2 the bard's level + the bard's Charisma modifier) negates
the effect. Ritual of reconciliation relies on audible components. This performance replaces dirge
of doom.

## Versatile Teamwork (Ex) {#versatile-teamwork}

At 2nd level, an Averaka arbiter gains a bonus teamwork feat. He gains an additional bonus teamwork
feat at 6th level and every 4 levels thereafter. This ability replaces versatile performance and
well-versed.
