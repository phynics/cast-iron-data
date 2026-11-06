+++
id = "ref/spell/alter-winds"
kind = "spell"
title = "Alter Winds"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alter_winds", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 minute"
components = "V, S"
range = "touch"
effects = [
  { label = "Area", value = "immobile 10-ft.-radius emanation" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Druid, Hunter, Occultist, Red Mantis Assassin, Sorcerer, Spiritualist, Wizard
Casting time: 1 minute
Components: V, S
Range: touch
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Area: immobile 10-ft.-radius emanation
Descriptors: air
:::

**Sources:** Advanced Player's Guide pg 201

You subtly enhance or diminish the effects of natural winds within the spell's area, which is an
immobile emanation around a point touched by you as the spell is cast. Within the area, natural (but
not magical) wind effects are either increased or decreased by one step in intensity. The maximum
wind force you can affect with this spell is based on your caster level, as shown on the table
below. Alter winds has no effect on magical wind effects.

|Caster Level|Wind Force|
| --- | --- |
|1st-3rd|Light|
|4th-9th|Moderate|
|10th-15th|Strong|
|16th or higher|Severe|
