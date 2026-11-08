+++
id = "ref/spell/inflict-serious-wounds-mass"
kind = "spell"
title = "Mass Inflict Serious Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_serious_wounds_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/inflict-light-wounds-mass" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Witch", level = 8 },
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
Level: 7: Cleric, Oracle, Shaman\
8: Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
:::

### Mass Inflict Serious Wounds

**Sources:** PRPG Core Rulebook pg 301

This spell functions like [mass inflict light wounds](ref/spell/inflict-light-wounds-mass), except
that it deals 3d8 points of damage + 1 point per caster level (maximum +35).
