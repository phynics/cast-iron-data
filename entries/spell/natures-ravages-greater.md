+++
id = "ref/spell/natures-ravages-greater"
kind = "spell"
title = "Greater Nature's Ravages"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "natures_ravages_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/natures-ravages" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "31"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Witch", level = 7 },
]
casting_time = "10 minute/HD of target"
components = "V, S, M/DF (dried maggots)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "corpse of creature whose total number of HD does not exceed your caster level" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Witch\
8: Cleric, Oracle
Casting time: 10 minute/HD of target
Components: V, S, M/DF (dried maggots)
Range: close (25 ft. + 5 ft./2 levels)
Target: corpse of creature whose total number of HD does not exceed your caster level
Duration: instantaneous
Saving throw: none
Spell resistance: no
:::

### Greater Nature's Ravages

This spell functions like [nature's ravages](ref/spell/natures-ravages), except the target corpse
ages a number of years equal to up to 1 year per caster level (maximum 20 years at 20th level).
