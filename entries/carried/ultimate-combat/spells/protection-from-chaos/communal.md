+++
id = "ref/carried/ultimate-combat/spells/protection-from-chaos/communal"
kind = "spell"
title = "Protection From Chaos, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Protection From Chaos"]
tags = ["abjuration", "lawful"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Protection From Chaos/Communal", path = "ultimate_combat/spell/protection_from_chaos_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["lawful"]
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
effects = [
  { label = "Target", value = "creatures touched" },
]
+++

::: statblock
School: abjuration \[lawful\]
Level: 2: Arcanist, Cleric, Inquisitor, Oracle, Paladin, Sorcerer, Summoner, Warpriest, Wizard
Target: creatures touched
:::

_As protection from chaos, but you may divide the duration among creatures touched._

This spell functions like _[protection from chaos](ref/spell/protection-from-chaos)_, except you
divide the duration in 1-minute intervals among the creatures touched.
