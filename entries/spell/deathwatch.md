+++
id = "ref/spell/deathwatch"
kind = "spell"
title = "Deathwatch"
aon = "SpellDisplay.aspx?ItemName=Deathwatch"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deathwatch", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "265"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Cleric, Medium, Oracle, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

Using the powers of necromancy, you can determine the condition of creatures near death within the
spell's range. You instantly know whether each creature within the area is dead, fragile (alive and
wounded, with 3 or fewer hit points left), fighting off death (alive with 4 or more hit points),
healthy, undead, or neither alive nor dead (such as a construct). Deathwatch sees through any spell
or ability that allows creatures to feign death.
