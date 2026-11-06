+++
id = "ref/spell/cure-serious-wounds-mass"
kind = "spell"
title = "Mass Cure Serious Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_serious_wounds_mass", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 8 },
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
saving_throw = "Will half (harmless) or Will half; see text"
spell_resistance = "yes (harmless) or yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Cleric, Oracle, Shaman\
8: Druid, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half (harmless) or Will half; see text
Spell resistance: yes (harmless) or yes; see text
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Healing
:::

**Sources:** PRPG Core Rulebook pg 263

This spell functions like mass cure light wounds, except that it cures 3d8 points of damage + 1
point per caster level (maximum +35).
