+++
id = "ref/arc-ranger/darklands-sailor"
kind = "archetype"
title = "Darklands Sailor"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Darklands%20Sailor"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darklands_sailor", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "skilled-pilot", level = 1 },
  { anchor = "keen-ear", level = 3 },
  { anchor = "quick-swim", level = 7 },
  { anchor = "subsonic-warning", level = 8 },
  { anchor = "hidden-depths", level = 12 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["skilled-pilot"] },
  { replaces = "Favored terrain", feature = "favored-terrain", by = ["keen-ear"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["quick-swim"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["subsonic-warning"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["hidden-depths"] },
  { replaces = "hide in plain sight", feature = "hide-in-plain-sight", by = ["hidden-depths"] },
]
+++

Those plying the lightless waters of the Darklands learn to use sound to augment their compromised
vision, providing insight into the hazards lurking below the surface. A Darklands sailor has the
following class features.

## Skilled Pilot (Ex) {#skilled-pilot}

A Darklands sailor adds half his level (minimum 1) to Profession (sailor) and Survival checks to
navigate or avoid natural hazards in subterranean waterways.

This ability replaces track.

## Keen Ear (Ex) {#keen-ear}

At 3rd level, a Darklands sailor learns how to use sound to compensate for poor visibility when
facing threats above and below the water. He gains the [uncanny dodge](ref/ability/uncanny-dodge)
rogue ability when underground and either swimming or aboard a boat. At 8th level, he gains
[improved uncanny dodge](ref/ability/improved-uncanny-dodge) under these conditions, treating his
Darklands sailor level as his effective rogue level for the purpose of denying an enemy's sneak
attacks. At 13th level, he gains blind sense with a range of 30 feet against creatures touching
water. At 18th level, his blind sense range increases to 60 feet or equal to the range of his
[darkvision](ref/rule/darkvision), whichever is greater. If the Darklands sailor becomes
[deafened](ref/misc/deafened), he loses all benefits of this ability until his hearing is restored.

This replaces favored terrain.

## Quick Swim (Ex) {#quick-swim}

At 7th level, a Darklands sailor can swim at his full speed as a move action without penalty.

This ability replaces woodland stride.

## Subsonic Warning (Ex) {#subsonic-warning}

At 8th level as a swift action, a Darklands sailor can provide the benefits of his keen ear ability
to the subjects of his hunter's bond. This effect lasts for a number of rounds per day equal to the
Darklands sailor's Wisdom modifier. These rounds need not be consecutive. A deafened creature can't
benefit from a Darklands sailor's subsonic warning.

This ability replaces swift tracker.

## Hidden Depths (Ex) {#hidden-depths}

At 12th level, a Darklands sailor can use the Stealth skill to hide while underground or underwater,
even if he doesn't have cover or concealment. At 17th level, he can use the Stealth skill even while
being observed when underground or underwater.

This ability replaces camouflage and hide in plain sight.
