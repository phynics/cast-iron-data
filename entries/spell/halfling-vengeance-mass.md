+++
id = "ref/spell/halfling-vengeance-mass"
kind = "spell"
title = "Mass Halfling Vengeance"
source_ids = ["pathfinder-131-the-reapers-right-hand"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "halfling_vengeance_mass", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/halfling-vengeance" },
]
[[sources]]
publication = "pathfinder-131-the-reapers-right-hand"
page = "72"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one Small or smaller creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Antipaladin\
6: Inquisitor\
7: Cleric, Oracle
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one Small or smaller creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Mass Halfling Vengeance

This spell functions like [halfling vengeance](ref/spell/halfling-vengeance), except that it affects
multiple creatures.
