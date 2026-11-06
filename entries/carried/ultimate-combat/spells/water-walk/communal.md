+++
id = "ref/carried/ultimate-combat/spells/water-walk/communal"
kind = "spell"
title = "Water Walk, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Water Walk"]
tags = ["transmutation", "water"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Water Walk/Communal", path = "ultimate_combat/spell/water_walk_communal.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["water"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 min./level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: transmutation \[water\]
Level: 4: Cleric, Hunter, Oracle, Ranger, Warpriest
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 min./level (D)
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As water walk, but you may divide the duration among creatures touched._

This spell functions like _[water walk](ref/spell/water-walk)_, except you divide the duration in
10-minute intervals among the creatures touched.
