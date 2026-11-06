+++
id = "ref/carried/ultimate-combat/spells/endure-elements/communal"
kind = "spell"
title = "Endure Elements, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Endure Elements"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Endure Elements/Communal", path = "ultimate_combat/spell/endure_elements_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 2: Arcanist, Cleric, Druid, Hunter, Hunter, Hunter, Hunter, Oracle, Paladin, Ranger, Sorcerer, Warpriest, Wizard\
3: Alchemist, Investigator
Casting Time: 1 standard action
Components: V, S
Range: touch
Target: creatures touched
Duration: 24 hours
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As endure elements, but you may divide the duration among creatures touched._

This spell functions like _[endure elements](ref/spell/endure-elements)_, except you divide the
duration in 1-hour increments among the creatures touched.
