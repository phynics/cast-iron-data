+++
id = "ref/arc-arcanist/elemental-master"
kind = "archetype"
title = "Elemental Master"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20Elemental%20Master"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_master", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "78"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-focus", level = 1 },
  { anchor = "elemental-attack", level = 3 },
  { anchor = "powerful-exploit", level = 9 },
  { anchor = "greater-elemental-attack", level = 11 },
  { anchor = "elemental-movement", level = 15 },
]
trades = [
  { replaces = "The arcanist exploit gained at 1st level", feature = "arcanist-exploits", levels = [1], by = ["elemental-focus"] },
  { replaces = "The arcanist exploit gained at 3rd level", feature = "arcanist-exploits", levels = [3], by = ["elemental-attack"] },
  { replaces = "The arcanist exploit gained at 9th level", feature = "arcanist-exploits", levels = [9], by = ["powerful-exploit"] },
  { replaces = "The arcanist exploit gained at 11th level", feature = "arcanist-exploits", levels = [11], by = ["greater-elemental-attack"] },
  { replaces = "The arcanist exploit gained at 15th level", feature = "arcanist-exploits", levels = [15], by = ["elemental-movement"] },
]
+++

Arcanists with an affinity for elemental forces sometimes focus on one and display its power in
everything they do.

## Elemental Focus (Su) {#elemental-focus}

At 1st level, the elemental master must select one element: air, earth, fire, or water. The arcanist
can prepare one additional spell per day of each level she can cast, but it must have the elemental
descriptor of her chosen element. In addition, any spell she prepares from the opposite elemental
school (air opposes earth, fire opposes water) takes up two of her prepared spell slots. This
ability replaces the arcanist exploit gained at 1st level.

## Elemental Attack (Su) {#elemental-attack}

At 3rd level, the elemental master gains an arcanist exploit tied to her element. If she selected
air, she gains the [lightning lance](ref/exploit/lightning-lance) arcanist exploit. If she selected
earth, she gains the [acid jet](ref/exploit/acid-jet) arcanist exploit. If she selected fire, she
gains the [flame arc](ref/exploit/flame-arc) arcanist exploit. If she selected water, she gains the
[ice missile](ref/exploit/ice-missile) arcanist exploit. This ability replaces the arcanist exploit
gained at 3rd level.

## Powerful Exploit (Su) {#powerful-exploit}

At 9th level, an elemental master increases the damage done by her elemental attack to 1d8 points of
energy damage plus 1d8 points of damage per two arcanist levels she possesses. The type of damage is
determined by the elemental attack. In addition, the range for the elemental attack ability
increases to 60 feet (in the case of flame arc, a 60-foot line). This ability replaces the arcanist
exploit gained at 9th level.

## Greater Elemental Attack (Su) {#greater-elemental-attack}

At 11th level, the elemental master gains a greater arcanist exploit tied to her element. If she
selected air, she gains the [dancing electricity](ref/exploit/dancing-electricity) arcanist exploit.
If she selected earth, she gains the [lingering acid](ref/exploit/lingering-acid) arcanist exploit.
If she selected fire, she gains the [burning flame](ref/exploit/burning-flame) arcanist exploit. If
she selected water, she gains the [icy tomb](ref/exploit/icy-tomb) arcanist exploit. This ability
replaces the arcanist exploit gained at 11th level.

## Elemental Movement (Su) {#elemental-movement}

At 15th level, an elemental master gains an elemental movement. This enhancement is based on her
chosen element type. Air grants a fly speed of 90 feet (average maneuverability), earth grants a
burrow speed of 30 feet, fire grants a increase of 30 feet to base land speed, and water grants a
swim speed of 60 feet. This ability replaces the arcanist exploit gained at 15th level.
