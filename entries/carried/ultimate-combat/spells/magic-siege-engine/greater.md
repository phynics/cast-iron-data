+++
id = "ref/carried/ultimate-combat/spells/magic-siege-engine/greater"
kind = "spell"
title = "Magic Siege Engine, Greater"
source_ids = ["ultimate-combat"]
section = ["Spells", "Magic Siege Engine"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Magic Siege Engine/Greater", path = "ultimate_combat/spell/magic_siege_engine_greater.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (black powder)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one siege engine touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless, object)"
spell_resistance = "yes (harmless, object)"
+++

::: statblock
School: transmutation
Level: 4: Antipaladin, Arcanist, Inquisitor, Paladin, Sorcerer, Wizard\
5: Cleric, Oracle, Warpriest
Casting Time: 1 standard action
Components: V, S, M/DF (black powder)
Range: close (25 ft. + 5 ft./2 levels)
Target: one siege engine touched
Duration: 1 hour/level
Saving Throw: Will negates (harmless, object)
Spell Resistance: yes (harmless, object)
:::

_Siege engine gains +1 on targeting and damage rolls for every four caster levels._

This spell functions like _magic siege weapon_, except it gives an indirect fire siege weapon an
enhancement bonus on targeting and damage rolls of +1 per four caster levels (maximum +5). If used
on a direct-fire siege weapon, this spell functions as
_[greater magic weapon](ref/spell/magic-weapon-greater)_.
