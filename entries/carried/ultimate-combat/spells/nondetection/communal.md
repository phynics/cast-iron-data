+++
id = "ref/carried/ultimate-combat/spells/nondetection/communal"
kind = "spell"
title = "Nondetection, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Nondetection"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Nondetection/Communal", path = "ultimate_combat/spell/nondetection_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (diamond dust worth 25 gp per target)"
range = "touch"
effects = [
  { label = "Target", value = "creatures or objects touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless, object)"
spell_resistance = "yes (harmless, object)"
+++

::: statblock
School: abjuration
Level: 4: Antipaladin, Arcanist, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S, M (diamond dust worth 25 gp per target)
Range: touch
Target: creatures or objects touched
Duration: 1 hour/level
Saving Throw: Will negates (harmless, object)
Spell Resistance: yes (harmless, object)
:::

_As nondetection, but you may divide the duration among creatures touched._

This spell functions like _[nondetection](ref/spell/nondetection)_, except you divide the duration
in 1-hour increments among the creatures or objects touched.
