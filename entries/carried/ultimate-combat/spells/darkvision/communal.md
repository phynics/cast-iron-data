+++
id = "ref/carried/ultimate-combat/spells/darkvision/communal"
kind = "spell"
title = "Darkvision, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Darkvision"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Darkvision/Communal", path = "ultimate_combat/spell/darkvision_communal.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Hunter", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (either a pinch of dried carrot or an agate)"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: transmutation
Level: 3: Alchemist, Antipaladin, Arcanist, Investigator, Sorcerer, Wizard\
4: Hunter, Hunter, Ranger
Casting Time: 1 standard action
Components: V, S, M (either a pinch of dried carrot or an agate)
Range: touch
Target: creatures touched
Duration: 1 hour/level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As darkvision, but you may divide the duration among creatures touched._

This spell functions like _[darkvision](ref/spell/darkvision)_, except you may divide the duration
in 1-hour intervals among the creatures touched.
