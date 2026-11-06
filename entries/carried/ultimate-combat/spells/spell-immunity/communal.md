+++
id = "ref/carried/ultimate-combat/spells/spell-immunity/communal"
kind = "spell"
title = "Spell Immunity, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Spell Immunity"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Spell Immunity/Communal", path = "ultimate_combat/spell/spell_immunity_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
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
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 5: Cleric, Inquisitor, Oracle, Warpriest
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 min./level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As spell immunity, but you may divide the duration among creatures touched._

This spell functions like _[spell immunity](ref/spell/spell-immunity)_, except you divide the
duration in 10-minute intervals among the creatures touched.
