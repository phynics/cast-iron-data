+++
id = "ref/spell/inflict-critical-wounds-mass"
kind = "spell"
title = "Mass Inflict Critical Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_critical_wounds_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/inflict-light-wounds-mass" },
]
[[sources]]
publication = "core-rulebook"
page = "300"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Witch", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Cleric, Oracle, Shaman\
9: Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
:::

### Mass Inflict Critical Wounds

This spell functions like [mass inflict light wounds](ref/spell/inflict-light-wounds-mass), except
that it deals 4d8 points of damage + 1 point per caster level (maximum +40).
