+++
id = "ref/spell/cure-moderate-wounds"
kind = "spell"
title = "Cure Moderate Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_moderate_wounds", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "263"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
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
Level: 2: Adept, Alchemist, Bard, Cleric, Inquisitor, Investigator, Occultist, Oracle, Shaman, Skald, Spiritualist, Warpriest, Witch\
3: Druid, Hunter, Paladin, Ranger
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half (harmless)
Spell resistance: yes (harmless); see text
Target: creature touched
Subschool: Healing
:::

This spell functions like cure light wounds, except that it cures 2d8 points of damage + 1 point per
caster level (maximum +10).
