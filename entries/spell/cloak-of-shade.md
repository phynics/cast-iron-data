+++
id = "ref/spell/cloak-of-shade"
kind = "spell"
title = "Cloak of Shade"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloak_of_shade", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a leaf from a shade tree)"
range = "touch"
effects = [
  { label = "Target", value = "one creature per level" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Druid, Hunter, Ranger
Casting time: 1 standard action
Components: V, S, M (a leaf from a shade tree)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature per level
:::

**Sources:** Advanced Player's Guide pg 211

This spell provides the subject with some degree of protection from the harmful effects of the sun.
The cloaked subject treats environmental heat due to sun exposure as one level less: severe heat is
considered very hot conditions, while very hot is considered average temperature (see
[heat dangers](ref/rule/heat-dangers)). The cloak of shade also reduces any penalties from sunlight
by 1. The spell does not, however, eliminate the effects of direct sunlight on creatures vulnerable
to sunlight. Cloak of shade has no effect on environmental heat from sources other than the sun.
