+++
id = "ref/arc-brawler/turfer"
kind = "archetype"
title = "Turfer"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Turfer"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "turfer", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "42"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-turf", level = 3 },
  { anchor = "terrain-mastery", level = 4 },
]
trades = [
  { replaces = "Maneuver training", feature = "maneuver-training", by = ["favored-turf"] },
  { replaces = "Knockout", feature = "knockout", by = ["terrain-mastery"] },
]
+++

A turfer has a mastery over particular types of terrain.

## Favored Turf (Ex) {#favored-turf}

At 3rd level, a turfer chooses a type of terrain from the ranger's
[favored terrain](ref/ability/favored-terrain) list. When in that type of terrain, she gains a +2
bonus on initiative checks and a +1 bonus on combat maneuver checks and to CMD.

At 7th level and every 4 brawler levels thereafter, the turfer chooses an additional terrain in
which to gain these bonuses. Each time, in one selected terrain (including the one just chosen), her
bonus on initiative checks increases by 2, and her bonus on combat maneuver checks and to CMD
increases by 1.

This replaces maneuver training.

## Terrain Mastery (Su) {#terrain-mastery}

At 4th level, a turfer gains the benefits of _[endure elements](ref/spell/endure-elements)_ and a
+10-foot enhancement bonus to her base speed, but only in her favored terrains. In addition, she can
move through [difficult terrain](ref/rule/terrain-and-obstacles) in her favored terrains at her
normal speed without taking damage or suffering any other impairment, but she can't do so through
difficult terrain that has been magically manipulated. At 10th and 16th levels, her enhancement
bonus to her base speed increases by 10 feet within her favored terrains. The turfer loses this
ability if she wears medium or heavy armor or carries a medium or heavy load.

This replaces knockout.
