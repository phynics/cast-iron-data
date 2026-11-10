+++
id = "ref/spell/inflict-moderate-wounds"
kind = "spell"
title = "Inflict Moderate Wounds"
aon = "SpellDisplay.aspx?ItemName=Inflict%20Moderate%20Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_moderate_wounds", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "300"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
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
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Inquisitor, Occultist, Oracle, Shaman, Spiritualist, Warpriest, Witch\
3: Antipaladin
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: creature touched
:::

This spell functions like [inflict light wounds](ref/spell/inflict-light-wounds), except that you
deal 2d8 points of damage + 1 point per caster level (maximum +10).
