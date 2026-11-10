+++
id = "ref/spell/inflict-critical-wounds"
kind = "spell"
title = "Inflict Critical Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_critical_wounds", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "300"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
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
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Inquisitor, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
5: Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: creature touched
:::

This spell functions like [inflict light wounds](ref/spell/inflict-light-wounds), except that you
deal 4d8 points of damage + 1 point per caster level (maximum +20).
