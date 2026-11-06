+++
id = "ref/carried/ultimate-combat/spells/spider-climb/communal"
kind = "spell"
title = "Spider Climb, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Spider Climb"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Spider Climb/Communal", path = "ultimate_combat/spell/spider_climb_communal.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a live spider)"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 min./level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: transmutation
Level: 3: Alchemist, Arcanist, Druid, Hunter, Hunter, Hunter, Investigator, Sorcerer, Summoner, Wizard
Casting Time: 1 standard action
Components: V, S, M (a live spider)
Range: touch
Target: creatures touched
Duration: 10 min./level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As spider climb, but you may divide the duration among creatures touched._

This spell functions like _[spider climb](ref/spell/spider-climb)_, except you divide the duration
in 10-minute intervals among the creatures touched.
