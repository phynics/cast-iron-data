+++
id = "ref/spell/atavism-mass"
kind = "spell"
title = "Mass Atavism"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "atavism_mass", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/atavism" },
]
[[sources]]
publication = "ultimate-magic"
page = "207"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one animal/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Druid
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one animal/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: yes
:::

### Mass Atavism

This spell functions as [atavism](ref/spell/atavism), except that it affects multiple creatures.
