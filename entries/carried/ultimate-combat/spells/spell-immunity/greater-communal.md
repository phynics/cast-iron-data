+++
id = "ref/carried/ultimate-combat/spells/spell-immunity/greater-communal"
kind = "spell"
title = "Spell Immunity, Greater Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Spell Immunity"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Spell Immunity/Greater Communal", path = "ultimate_combat/spell/spell_immunity_greater_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Warpriest", level = 9 },
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
Level: 9: Cleric, Oracle, Warpriest
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 min./level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As greater spell immunity, but you may divide the duration among creatures touched._

This spell functions like _[greater spell immunity](ref/spell/spell-immunity-greater)_, except you
divide the duration among the creatures in 10-minute intervals among the creatures touched.
