+++
id = "ref/carried/ultimate-combat/spells/mind-blank/communal"
kind = "spell"
title = "Mind Blank, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Mind Blank"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Mind Blank/Communal", path = "ultimate_combat/spell/mind_blank_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 9: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: creatures touched
Duration: 24 hours
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As mind blank, but you may divide the duration among creatures touched._

This spell functions like _[mind blank](ref/spell/mind-blank)_, except you divide the duration in
1-hour increments among the creatures touched.
