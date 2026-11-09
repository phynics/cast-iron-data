+++
id = "ref/carried/core-rulebook/spells/spell-immunity/greater"
kind = "spell"
title = "Spell Immunity, Greater"
aon = "SpellDisplay.aspx?ItemName=Spell%20Immunity%2C%20Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Spell Immunity"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Spell Immunity/Greater", path = "core_rulebook/spell/spell_immunity_greater.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Warpriest", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 min./level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 8: Cleric, Oracle, Warpriest
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creature touched
Duration: 10 min./level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As spell immunity, but up to 8th-level spells._

This spell functions like _[spell immunity](ref/spell/spell-immunity)_, except the immunity applies
to spells of 8th level or lower. A creature can have only one
_[spell immunity](ref/spell/spell-immunity)_ or
_[greater spell immunity](ref/spell/spell-immunity-greater)_ spell in effect on it at a time.
