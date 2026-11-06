+++
id = "ref/spell/sickening-strikes"
kind = "spell"
title = "Sickening Strikes"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sickening_strikes", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["disease"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Antipaladin", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Antipaladin, Druid, Hunter, Investigator, Witch\
3: Magus\
4: Ranger
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: Fortitude negates, see text
Spell resistance: yes
Target: you
Descriptors: disease
:::

**Sources:** Advanced Race Guide pg 155

> _[Ratfolk](ref/race/ratfolk) have access to the following spell._

You are imbued with disease, and any creature you strike with a melee attack must make a Fortitude
save or be sickened for 1 minute. Creatures that are immune to disease are immune to this sickened
effect.
