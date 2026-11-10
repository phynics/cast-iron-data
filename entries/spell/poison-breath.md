+++
id = "ref/spell/poison-breath"
kind = "spell"
title = "Poison Breath"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poison_breath", path = "json/spells7.json" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "28"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["poison"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a spider's mandible)"
range = "15 ft."
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
Level: 6: Druid, Hunter\
7: Cleric, Oracle, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a spider's mandible)
Range: 15 ft.
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Area: cone-shaped burst
Descriptors: poison
:::

You expel a cone-shaped burst of toxic mist from your mouth, subjecting everyone caught in the area
to a deadly poison, as per the poison spell.
