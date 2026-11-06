+++
id = "ref/carried/ultimate-combat/spells/tongues/communal"
kind = "spell"
title = "Tongues, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Tongues"]
tags = ["divination"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Tongues/Communal", path = "ultimate_combat/spell/tongues_communal.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 5 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, M/DF (a clay model of a ziggurat)"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 min./level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
School: divination
Level: 3: Bard, Skald\
4: Alchemist, Arcanist, Investigator, Sorcerer, Summoner, Witch, Wizard\
5: Cleric, Oracle, Warpriest
Casting Time: 1 standard action
Components: V, M/DF (a clay model of a ziggurat)
Range: touch
Target: creatures touched
Duration: 10 min./level
Saving Throw: Will negates (harmless)
Spell Resistance: no
:::

_As tongues, but you may divide the duration among creatures touched._

This spell functions like _[tongues](ref/spell/tongues)_, except you divide the duration in
10-minute intervals among the creatures touched.
