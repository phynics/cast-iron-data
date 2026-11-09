+++
id = "ref/spell/archons-trumpet"
kind = "spell"
title = "Archon's Trumpet"
source_ids = ["champions-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "archons_trumpet", path = "json/spells.json" },
]
[[sources]]
publication = "champions-of-purity"
page = "28"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good", "sonic"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Paladin", level = 4 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Paladin\
5: Bard, Skald\
7: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Area: cone-shaped burst
Descriptors: good, sonic
:::

Upon hearing a booming report, as if from a trumpet archon's mighty horn, all creatures in the area
of the burst are paralyzed for 1d4 rounds.
