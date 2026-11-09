+++
id = "ref/spell/cure-critical-wounds-mass"
kind = "spell"
title = "Mass Cure Critical Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_critical_wounds_mass", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/cure-light-wounds-mass" },
]
[[sources]]
publication = "core-rulebook"
page = "262"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 9 },
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
saving_throw = "Will half (harmless) or Will half; see text"
spell_resistance = "yes (harmless) or yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 8: Cleric, Oracle, Shaman\
9: Druid, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half (harmless) or Will half; see text
Spell resistance: yes (harmless) or yes; see text
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Healing
:::

This spell functions like [mass cure light wounds](ref/spell/cure-light-wounds-mass), except that it
cures 4d8 points of damage +1 point per caster level (maximum +40).
