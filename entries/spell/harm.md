+++
id = "ref/spell/harm"
kind = "spell"
title = "Harm"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "harm", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "293"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 7 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will half; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Cleric, Inquisitor, Occultist, Oracle, Spiritualist, Warpriest\
7: Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half; see text
Spell resistance: yes
Target: creature touched
:::

Harm charges a subject with negative energy that deals 10 points of damage per caster level (to a
maximum of 150 points at 15th level). If the creature successfully saves, harm deals half this
amount. Harm cannot reduce the target's hit points to less than 1.

If used on an undead creature, harm acts like heal.
