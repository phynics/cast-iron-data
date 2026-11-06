+++
id = "ref/carried/ultimate-combat/spells/air-walk/communal"
kind = "spell"
title = "Air Walk, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Air Walk"]
tags = ["transmutation", "air"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Air Walk/Communal", path = "ultimate_combat/spell/air_walk_communal.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 min./level"
saving_throw = "none"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: transmutation \[air\]
Level: 5: Alchemist, Cleric, Druid, Hunter, Investigator, Oracle, Warpriest
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 min./level
Saving Throw: none
Spell Resistance: yes (harmless)
:::

_As air walk, but you may divide the duration among creatures touched._

This spell functions like _[air walk](ref/spell/air-walk)_, except divide the duration in 10-minute
intervals among the creatures touched.
