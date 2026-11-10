+++
id = "ref/spell/violent-misfire-greater"
kind = "spell"
title = "Greater Violent Misfire"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "violent_misfire_greater", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/violent-misfire" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "29"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a small piece of flint)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one early or advanced firearm/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a small piece of flint)
Range: medium (100 ft. + 10 ft./level)
Target: one early or advanced firearm/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
:::

### Greater Violent Misfire

This spell functions as [violent misfire](ref/spell/violent-misfire) except as noted above.
