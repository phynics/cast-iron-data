+++
id = "ref/spell/cure-critical-wounds"
kind = "spell"
title = "Cure Critical Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_critical_wounds", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "262"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 4 },
  { class = "Alchemist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will half (harmless)"
spell_resistance = "yes (harmless); see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Adept, Alchemist, Bard, Cleric, Inquisitor, Investigator, Occultist, Oracle, Shaman, Skald, Spiritualist, Warpriest\
5: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half (harmless)
Spell resistance: yes (harmless); see text
Target: creature touched
Subschool: Healing
:::

This spell functions like cure light wounds, except that it cures 4d8 points of damage +1 point per
caster level (maximum +20).
