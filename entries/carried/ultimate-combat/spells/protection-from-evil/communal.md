+++
id = "ref/carried/ultimate-combat/spells/protection-from-evil/communal"
kind = "spell"
title = "Protection From Evil, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Protection From Evil"]
tags = ["abjuration", "good"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Protection From Evil/Communal", path = "ultimate_combat/spell/protection_from_evil_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "1 min./level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no; see text"
+++

::: statblock
School: abjuration \[good\]
Level: 2: Arcanist, Cleric, Inquisitor, Oracle, Paladin, Sorcerer, Summoner, Warpriest, Wizard
Casting Time: 1 standard action
Components: V, S, M/DF
Range: touch
Target: creatures touched
Duration: 1 min./level (D)
Saving Throw: Will negates (harmless)
Spell Resistance: no; see text
:::

_As protection from evil, but you may divide the duration among creatures touched._

This spell functions like _[protection from evil](ref/spell/protection-from-evil)_, except you
divide the duration in 1-minute intervals among the creatures touched.
