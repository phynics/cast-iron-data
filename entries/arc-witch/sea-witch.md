+++
id = "ref/arc-witch/sea-witch"
kind = "archetype"
title = "Sea Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Sea%20Witch"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sea_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "ultimate-magic"
page = "85"

[fields]
kind = "archetype"
features = [
  { anchor = "patron" },
  { anchor = "spells" },
  { anchor = "know-direction" },
  { anchor = "sea-creature-empathy", level = 1 },
]
trades = [
  { replaces = "1st-level hex", feature = "hex", levels = [1], by = ["sea-creature-empathy"] },
]
+++

A sea witch's affinities are tied to the vast oceans and the rolling waves. Her magic concerns the
moon, tides, water, and winds, and she is most at peace when she is upon or near the sea.

## Patron {#patron}

A sea witch cannot choose a patron whose interests or theme opposes that of water (for example,
earth or fire).

## Spells {#spells}

A sea witch replaces some of her patron spells with the following: 2nd—_touch of sea_, 4th—_gust of
wind_, 6th—_water breathing_, 8th—_control water_, 10th—_cloudkill_, 12th—_control wind_,
14th—_control weather_, 16th—_vortex_, 18th—_tsunami_.

## Know Direction (Sp) {#know-direction}

So long as she near a sizable body of water (at least a lake with a diameter of 1 mile or more), a
sea witch may cast _[know direction](ref/spell/know-direction)_ at will as a
[spell-like ability](ref/umr/spell-like-abilities).

## Sea Creature Empathy (Ex) {#sea-creature-empathy}

A sea witch can influence the attitude of water-dwelling animals and animals that live along coasts
and shores, including birds, as if using [wild empathy](ref/ability/wild-empathy). The sea witch
uses her witch level as her [druid](ref/class/druid) level for this ability. If the sea witch has
wild empathy from another class, her witch levels stack with the other class's levels to determine
her wild empathy bonus for these kinds of creatures. This ability replaces the witch's 1st-level
hex.

## Hexes {#hexes}

The following witch hexes complement the sea witch archetype: charm, flight, water lung.

## Major Hexes {#major-hexes}

The following major hexes complement the sea witch archetype: hag eye, hidden home, weather control.

## Grand Hexes {#grand-hexes}

The following grand hex complements the sea witch archetype: natural disaster.
