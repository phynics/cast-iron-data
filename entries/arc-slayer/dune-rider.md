+++
id = "ref/arc-slayer/dune-rider"
kind = "archetype"
title = "Dune Rider"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Dune%20Rider"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dune_rider", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "86"

[fields]
kind = "archetype"
features = [
  { anchor = "sand-foot", level = 1 },
  { anchor = "desert-skirmisher", level = 1 },
  { anchor = "galloping-fire", level = 4 },
  { anchor = "dust-vision", level = 8 },
  { anchor = "dunes-of-death", level = 20 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["sand-foot"] },
  { replaces = "fast tracker", feature = "swift-tracker", by = ["sand-foot"] },
  { replaces = "Studied target", feature = "studied-target", by = ["desert-skirmisher"] },
  { replaces = "Stalker", feature = "stalker", by = ["galloping-fire"] },
  { replaces = "slayer talent gained at 4th level", feature = "slayer-talents", levels = [4], by = ["galloping-fire"] },
  { replaces = "Slayer talent gained at 8th level", feature = "slayer-talents", levels = [8], by = ["dust-vision"] },
  { replaces = "Master slayer", feature = "master-slayer", by = ["dunes-of-death"] },
]
+++

Mounted harriers, saboteurs, and skirmishers, dune riders can disrupt even the most organized
opposition.

## Sand Foot (Ex) {#sand-foot}

The dune rider adds half his level as a bonus on Ride checks in warm deserts, hills, and mountains.
At 11th level, the dune rider and his mount no longer treat sand or rocky ground as
[difficult terrain](ref/rule/terrain-and-obstacles), and they gain a +10-foot enhancement bonus to
their base speed in warm deserts, hills, and mountains.

This replaces track and fast tracker.

## Desert Skirmisher (Ex) {#desert-skirmisher}

The dune rider excels in combat in warm deserts, hills, and mountains. While in such terrain, he
gains a +2 bonus on initiative, Perception, and Stealth checks, and a +1 bonus on attack and damage
rolls. At 5th level and every 5 levels thereafter, the bonus on initiative, Perception, and Stealth
checks increases by 2 (maximum +10) and the bonus on attack and damage rolls increases by 1 (maximum
+5).

This replaces studied target.

## Galloping Fire (Ex) {#galloping-fire}

At 4th level, the penalties for the dune rider's ranged attacks while mounted decrease by 2. These
penalties decrease by an additional 2 at 7th level.

This replaces stalker and the slayer talent normally gained at 4th level.

## Dust Vision (Ex) {#dust-vision}

At 8th level, the dune rider is at home in the desert. He exists comfortably in hot conditions up to
140º Fahrenheit without having to attempt Fortitude saves. His equipment is likewise protected. He
takes no penalties on Perception checks from blowing sand, dust, or heat shimmers, nor do these
effects grant [concealment](ref/rule/concealment) to the dune rider's enemies within 30 feet.
Effects that would grant total concealment work normally.

This replaces the slayer talent normally gained at 8th level.

## Dunes of Death (Su) {#dunes-of-death}

At 20th level, a dune rider can use the desert's heat to finish off his foes. As a standard action,
he can make a single attack at his full base attack bonus while in warm desert, hills, or mountains,
choosing one of the following effects: kill, knock unconscious for 1d4 hours, or paralyze for 2d6
rounds. If the attack hits, the target takes damage normally and must succeed at a Fortitude save or
suffer the additional effect. The DC of this save is 20 + the dune rider's Intelligence modifier.
Whether or not the target succeeds, it can't be targeted by this ability again for 24 hours.

This replaces master slayer.
