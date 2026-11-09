+++
id = "ref/carried/core-rulebook/spells/magic-fang/greater"
kind = "spell"
title = "Magic Fang, Greater"
aon = "SpellDisplay.aspx?ItemName=Magic%20Fang%2C%20Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Magic Fang"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Magic Fang/Greater", path = "core_rulebook/spell/magic_fang_greater.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Summoner", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: transmutation
Level: 3: Druid, Hunter, Hunter, Ranger, Summoner
Casting Time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature
Duration: 1 hour/level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_One natural weapon gets + 1/four levels (max. +5)._

This spell functions like _[magic fang](ref/spell/magic-fang)_, except that the enhancement bonus on
attack and damage rolls is +1 per four caster levels (maximum +5). This bonus does not allow a
natural weapon or unarmed strike to bypass [damage reduction](ref/rule/damage-reduction) aside from
magic.

Alternatively, you may imbue all of the creature's natural weapons with a +1 enhancement bonus
(regardless of your caster level).

_[Greater magic fang](ref/spell/magic-fang-greater)_ can be made permanent with a
_[permanency](ref/spell/permanency)_ spell.
