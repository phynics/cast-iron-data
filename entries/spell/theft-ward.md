+++
id = "ref/spell/theft-ward"
kind = "spell"
title = "Theft Ward"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "theft_ward", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one object" },
]
duration = "1 day"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Arcanist, Cleric, Inquisitor, Mesmerist, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 day
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one object
:::

**Sources:** Advanced Race Guide pg 167

> _[Tengus](ref/race/tengu) have access to the following spell._

You ward a single object in your possession against theft. You gain a +10 bonus on Perception checks
to notice someone trying to take the object from you.
