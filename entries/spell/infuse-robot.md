+++
id = "ref/spell/infuse-robot"
kind = "spell"
title = "Infuse Robot"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infuse_robot", path = "json/spells14.json" },
]
[[sources]]
publication = "technology-guide"
page = "9"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one robot" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Cleric, Druid, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one robot
:::

If the targeted robot fails its Will saving throw, it transforms into a magical construct made of
wood, stone, flesh, or bone. The robot's statistics and abilities do not change, although it is now
a magical construct rather than a technological one. It loses the robot subtype, but does not lose
its Intelligence score (if any). You can issue mental commands to the infused robot as long as it
stays within range of the spell; issuing commands in this manner is a free action for you. When the
spell's duration runs out, the robot transforms back to normal but is staggered for 1d4 rounds.
