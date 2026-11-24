+++
id = "ref/arc-rogue/scout"
kind = "archetype"
title = "Scout"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Scout"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scout", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "134"

[fields]
kind = "archetype"
features = [
  { anchor = "scout-s-charge", level = 4 },
  { anchor = "skirmisher", level = 8 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["scout-s-charge", "skirmisher"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["skirmisher"] },
]
+++

Not all rogues live in the city. Scouts frequently roam the wilderness, often banding together as
bandits, but sometimes serving as guides, as trailblazers, or as companions to a ranger or barbarian
warrior. More comfortable with sneaking and hiding outdoors, the scout is still effective in the
city and the dungeon.

## Scout's Charge (Ex) {#scout-s-charge}

At 4th level, whenever a scout makes a [charge](ref/rule/charge), her attack deals sneak attack
damage as if the target were [flat-footed](ref/rule/flat-footed). Foes with uncanny dodge are immune
to this ability. This ability replaces uncanny dodge.

## Skirmisher (Ex) {#skirmisher}

At 8th level, whenever a scout moves more than 10 feet in a round and makes an attack action, the
attack deals sneak attack damage as if the target was flat-footed. If the scout makes more than one
attack this turn, this ability only applies to the first attack. Foes with uncanny dodge are immune
to this ability. This ability replaces improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the scout archetype: assault leader, camouflage, cunning
trigger, survivalist, and trap spotter\*.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the scout archetype: hunter's surprise, skill
mastery\*, and stealthy sniper.
