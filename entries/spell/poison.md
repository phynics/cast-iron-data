+++
id = "ref/spell/poison"
kind = "spell"
title = "Poison"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poison", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous; see text"
saving_throw = "Fortitude negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Druid, Hunter\
4: Antipaladin, Cleric, Mesmerist, Occultist, Oracle, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: instantaneous; see text
Saving throw: Fortitude negates; see text
Spell resistance: yes
Target: living creature touched
Descriptors: poison
:::

**Sources:** PRPG Core Rulebook pg 323

Calling upon the venomous powers of natural predators, you infect the subject with a horrible poison
by making a successful melee touch attack. This poison deals 1d3 Constitution damage per round for 6
rounds. Poisoned creatures can make a Fortitude save each round to negate the damage and end the
affliction.
