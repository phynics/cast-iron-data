+++
id = "ref/spell/cure-moderate-wounds-mass"
kind = "spell"
title = "Mass Cure Moderate Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_moderate_wounds_mass", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/cure-light-wounds-mass" },
]
[[sources]]
publication = "core-rulebook"
page = "263"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 7 },
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
Level: 6: Bard, Cleric, Inquisitor, Occultist, Oracle, Shaman, Skald, Warpriest\
7: Druid, Witch
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
cures 2d8 points of damage + 1 point per caster level (maximum +30).
