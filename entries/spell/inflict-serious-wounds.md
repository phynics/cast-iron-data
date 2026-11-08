+++
id = "ref/spell/inflict-serious-wounds"
kind = "spell"
title = "Inflict Serious Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_serious_wounds", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
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
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Cleric, Inquisitor, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
4: Antipaladin, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 301

This spell functions like [inflict light wounds](ref/spell/inflict-light-wounds), except that it
deals 3d8 + 1 point per caster level (maximum +15).
