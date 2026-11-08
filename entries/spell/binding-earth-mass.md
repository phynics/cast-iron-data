+++
id = "ref/spell/binding-earth-mass"
kind = "spell"
title = "Mass Binding Earth"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "binding_earth_mass", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/binding-earth" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or object/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature or object/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Descriptors: earth
:::

### Mass Binding Earth

**Sources:** Advanced Race Guide pg 149

> _[Oreads](ref/race/oread) have access to the following spell._

This spell functions as [binding earth](ref/spell/binding-earth), except as noted above.
