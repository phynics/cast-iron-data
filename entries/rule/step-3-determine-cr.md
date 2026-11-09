+++
id = "ref/rule/step-3-determine-cr"
kind = "rule"
title = "Step 3: Determine CR"
source_ids = ["bestiary"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "step_3_determine_cr", path = "json/rules_gm07.json" },
]
[[sources]]
publication = "bestiary"
page = "297"

[fields]
kind = "none"
+++

Determining the final CR for a creature with class levels requires careful consideration. While
adding a class level to a monster that stacks with its existing abilities and role generally adds 1
to its CR for each level taken, adding classes that do not stack is more complicated.

Table 2-4 gives general guidelines regarding which core classes add directly to a monster's
abilities based on its role. Classes that are marked "key" generally add 1 to a creature's CR for
each level added. Classes marked with a --- increase a creature's CR by 1 for every 2 class levels
added until the number of levels added are equal to (or exceed) the creature's original CR, at which
point they are treated as "key" levels (adding 1 to the creature's CR for each level added).
Creatures that fall into multiple roles treat a class as key if either of its roles treat the class
as key. Note that levels in NPC classes are never considered key.

### Table 2-4: Monsters with Class Levels

|Monster Role|Barbarian, Fighter, Ranger|Cleric, Druid, Sorcerer, Wizard|Bard, Rogue|Monk, Paladin|
| --- | --- | --- | --- | --- |
|Combat|Key|-|-|-|
|Spell|-|Key\*|-|-|
|Skill|Key|-|Key|-|
|Special|-|-|-|-|

\* This class is only key if its spellcasting levels stack with those possessed by the creature.
