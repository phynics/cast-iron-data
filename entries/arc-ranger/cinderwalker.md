+++
id = "ref/arc-ranger/cinderwalker"
kind = "archetype"
title = "Cinderwalker"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Cinderwalker"
source_ids = ["pathfinder-95-anvil-of-fire"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cinderwalker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "pathfinder-95-anvil-of-fire"
page = "72"

[fields]
kind = "archetype"
features = [
  { anchor = "born-to-the-fire", level = 3 },
  { anchor = "inured", level = 4 },
  { anchor = "cinderwalk", level = 7 },
]
trades = [
  { replaces = "1st favored terrain", feature = "favored-terrain", levels = [3], by = ["born-to-the-fire"] },
  { replaces = "wild empathy", feature = "wild-empathy", by = ["born-to-the-fire"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["inured"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["cinderwalk"] },
]
+++

Cinderwalkers traverse burning wastelands and restless mountains, thriving in lands most creatures
avoid.

## Born to the Fire (Ex) {#born-to-the-fire}

At 3rd level, a cinderwalker gains a +2 bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks when in volcanic or geothermally active areas. Such areas
include calderas, hot springs, lava plains, and volcanically formed hills or mountains. In addition,
the cinderwalker adds this bonus on any ability checks, saving throws, or skill checks to avoid
geothermal or volcanic hazards. The cinderwalker can choose to improve this bonus in place of
improving a favored terrain bonus. A cinderwalker traveling through volcanic or geothermally active
areas leaves no trail and cannot be tracked (though he can leave a trail if he chooses). This
ability replaces the cinderwalker's first favored terrain and wild empathy.

## Inured (Ex) {#inured}

At 4th level, a cinderwalker gains the benefits of _[endure elements](ref/spell/endure-elements)_
against hot environments. At 8th level, the cinderwalker gains fire resistance 10, which improves to
fire resistance 20 at 12th level, fire resistance 30 at 16th level, and immunity to fire at 20th
level. This ability replaces hunter's bond.

## Cinderwalk (Ex) {#cinderwalk}

At 7th level, a cinderwalker can move through any sort of solid volcanic terrain (such as ash,
cooled lava, or volcanic rock) at his normal speed and without taking damage or suffering any other
impairment. The cinderwalker ignores fire damage from being near heat sources and touching heated
surfaces (but not from immersion). This ability replaces woodland stride.
