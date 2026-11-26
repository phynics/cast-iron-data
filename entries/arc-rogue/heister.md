+++
id = "ref/arc-rogue/heister"
kind = "archetype"
title = "Heister"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Heister"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heister", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "rum-dubber", level = 2 },
  { anchor = "ferret-s-grace", level = 4 },
  { anchor = "unseen", level = 8 },
]
trades = [
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["rum-dubber"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["ferret-s-grace"] },
  { replaces = "rogue talent gained at 4th level", feature = "rogue-talents", levels = [4], by = ["ferret-s-grace"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["unseen"] },
  { replaces = "rogue talent gained at 8th level", feature = "rogue-talents", levels = [8], by = ["unseen"] },
]
+++

Notorious for their stealth, imagination, and elaborately planned thefts and capers, heisters
specialize in breaking into secure locations, stealing items of value, and escaping undetected.
Heisters often work as members of or independent operatives contracted to criminal organizations,
crime families, or wealthy individuals inclined to unlawful activity.

## Rum Dubber (Ex) {#rum-dubber}

At 2nd level, whenever a heister attempts to open a lock without a set of
[thieves' tools](ref/eq-misc/thieves-tools), the DC increases by 2, instead of 10.

This ability replaces the rogue talent gained at 2nd level.

## Ferret's Grace (Ex) {#ferret-s-grace}

At 4th level, a heister gains [Stealthy](ref/feat/stealthy) as a bonus feat.

Additionally, a heister counts as a creature one size category smaller than she actually is when
determining whether or not she is [squeezing](ref/misc/squeezing) into an enclosed space. Finally,
when a heister uses the [Escape Artist](ref/skill/escape-artist) skill to move through a tight space
where her head fits but her shoulders do not, the DC is 20, instead of 30.

This ability replaces uncanny dodge and the rogue talent gained at 4th level.

## Unseen (Ex) {#unseen}

At 8th level, a heister masters hiding in underground and urban terrain. She can use the Stealth
skill to hide in underground and urban terrain, even while being observed. She also gains the
[terrain mastery](ref/talent/terrain-mastery) rogue talent twice, once each for underground and
urban terrain.

This ability replaces improved uncanny dodge and the rogue talent gained at 8th level.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the heister archetype: expert leaper, fast getaway, fast
picks, fast stealth, getaway artist, ledge walker, and quick disable (as well as certainty for an
unchained rogue).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the heister archetype: fast tumble, getaway master,
hidden mind, and skill mastery (as well as cutting edge for an unchained rogue).
