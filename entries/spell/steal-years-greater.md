+++
id = "ref/spell/steal-years-greater"
kind = "spell"
title = "Greater Steal Years"
source_ids = ["blood-of-the-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steal_years_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/steal-years" },
]
[[sources]]
publication = "blood-of-the-night"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of ash)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 day/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a handful of ash)
Range: touch
Target: creature touched
Duration: 1 day/level
Saving throw: Fortitude negates
Spell resistance: yes
:::

### Greater Steal Years

This spell functions like [steal years](ref/spell/steal-years), except you drain 1d6 years per two
caster levels (maximum 10d6).
