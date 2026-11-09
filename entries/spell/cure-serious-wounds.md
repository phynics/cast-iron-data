+++
id = "ref/spell/cure-serious-wounds"
kind = "spell"
title = "Cure Serious Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_serious_wounds", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "263"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Alchemist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 4 },
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
Level: 3: Adept, Alchemist, Bard, Cleric, Inquisitor, Investigator, Occultist, Oracle, Shaman, Skald, Spiritualist, Warpriest\
4: Druid, Hunter, Paladin, Ranger, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half (harmless)
Spell resistance: yes (harmless); see text
Target: creature touched
Subschool: Healing
:::

This spell functions like cure light wounds, except that it cures 3d8 points of damage + 1 point per
caster level (maximum +15).
