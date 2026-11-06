+++
id = "ref/spell/decompose-corpse"
kind = "spell"
title = "Decompose Corpse"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "decompose_corpse", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of dried toadstool)"
range = "touch"
effects = [
  { label = "Target", value = "one corpse or corporeal undead" },
]
duration = "instantaneous or 1 minute; see text"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Cleric, Druid, Hunter, Medium, Occultist, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of dried toadstool)
Range: touch
Duration: instantaneous or 1 minute; see text
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: one corpse or corporeal undead
:::

**Sources:** Ultimate Magic pg 216

Using this spell, the caster rapidly decomposes the flesh from a single corpse of size Huge or
smaller, leaving behind a perfectly cleaned skeleton. If it is cast on a non-skeletal corporeal
undead, the creature takes a -2 penalty on all rolls and to its Armor Class and CMD for 1 minute.
