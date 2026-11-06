+++
id = "ref/carried/ultimate-combat/spells/protection-from-good/communal"
kind = "spell"
title = "Protection From Good, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Protection From Good"]
tags = ["abjuration", "evil"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Protection From Good/Communal", path = "ultimate_combat/spell/protection_from_good_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
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
School: abjuration \[evil\]
Level: 2: Antipaladin, Arcanist, Cleric, Inquisitor, Oracle, Sorcerer, Summoner, Warpriest, Wizard
Target: creatures touched
:::

_As protection from good, but you may divide the duration among creatures touched._

This spell functions like _[protection from good](ref/spell/protection-from-good)_, except you
divide the duration in 1-minute intervals among the creatures touched.
