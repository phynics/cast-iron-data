+++
id = "ref/spell/fester-mass"
kind = "spell"
title = "Mass Fester"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fester_mass", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fester" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Inquisitor", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (rotted meat)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level or 1 round; see text"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Inquisitor, Witch
Casting time: 1 standard action
Components: V, S, M (rotted meat)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level or 1 round; see text
Saving throw: Fortitude partial
Spell resistance: yes
:::

### Mass Fester

**Sources:** Advanced Player's Guide pg 221

This spell functions as [fester](ref/spell/fester), except that it affects multiple foes.
