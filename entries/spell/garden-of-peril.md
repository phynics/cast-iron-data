+++
id = "ref/spell/garden-of-peril"
kind = "spell"
title = "Garden of Peril"
aon = "SpellDisplay.aspx?ItemName=Garden%20of%20Peril"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "garden_of_peril", path = "json/spells13.json" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "28"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of spores)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one poisonous mushroom/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Druid, Hunter, Ranger, Sorcerer, Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of spores)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: no
Effect: one poisonous mushroom/level, no two of which can be more than 30 ft. apart
Subschool: Creation
Descriptors: poison
:::

Vividly colored poisonous mushrooms instantly spring into existence in squares you select. The
mushrooms can appear on any solid surface, even growing horizontally from walls or upside down from
the ceiling.

Once per round as a move action, starting the round after you cast this spell, you can command the
mushrooms to release poisonous spores. Each creature adjacent to a mushroom or in a mushroom's
square must then succeed at a Fortitude save or become sickened for 1d4 rounds. The condition of
creatures that fail multiple saving throws does not worsen, but each additional failed saving throw
adds 1d4 rounds to the duration the creature is sickened.

The mushrooms are Tiny and cannot provide cover, but they are fairly sturdy (AC 7, hp 30, break DC
20). Creatures can move through squares containing mushrooms as normal. When destroyed, a mushroom
evaporates and releases one last cloud of spores.
