+++
id = "ref/arc-ranger/deep-walker"
kind = "archetype"
title = "Deep Walker"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Deep%20Walker"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deep_walker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-combat"
page = "66"

[fields]
kind = "archetype"
features = [
  { anchor = "deep-knowledge", level = 3 },
  { anchor = "rock-hopper", level = 7 },
  { anchor = "deep-walker-camouflage", level = 12 },
  { anchor = "one-with-the-stone", level = 17 },
]
trades = [
  { replaces = "Favored terrain", feature = "favored-terrain", by = ["deep-knowledge"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["rock-hopper"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["deep-walker-camouflage"] },
  { replaces = "Hide in plain sight", feature = "hide-in-plain-sight", by = ["one-with-the-stone"] },
]
+++

Some rangers devote their lives to the woods, becoming hunters, protectors, and wilderness guides
among its diverse terrain types. The deep walker is instead a master of the strange terrain of the
deep earth, exploring its caverns and caves, becoming a master of the dark corridors most surface
dwellers fear to explore—and perhaps the reason they fear to explore them.

## Deep Knowledge (Ex) {#deep-knowledge}

At 3rd level, a deep walker gains a +2 bonus on initiative checks and Knowledge (dungeoneering),
Perception, Stealth, and Survival skill checks while underground (in caves and dungeons). Every 5
levels thereafter, the deep walker gains an additional +3 on each of those checks while underground
(to a maximum of +11 at 18th level). This ability replaces favored terrain.

## Rock Hopper (Ex) {#rock-hopper}

At 7th level, a deep walker instinctively grasps for the most stable surfaces and holds on tighter
while moving over underground rock and stone. The deep walker gains a +5 bonus on all Acrobatics and
Climb checks made to traverse underground terrain. Furthermore, the deep walker ignores
[difficult terrain](ref/rule/terrain-and-obstacles) created by underground terrain and subterranean
flora. This ability replaces woodland stride.

## Deep Walker Camouflage (Ex) {#deep-walker-camouflage}

At 12th level, a deep walker can use the Stealth skill to hide in underground environments, even if
the terrain does not grant cover or concealment. This ability replaces camouflage.

## One with the Stone (Ex) {#one-with-the-stone}

At 17th level, a deep walker can use the Stealth skill while he is underground, even when being
observed. This ability replaces hide in plain sight.
