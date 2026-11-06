+++
id = "ref/carried/ultimate-combat/spells/resist-energy/communal"
kind = "spell"
title = "Resist Energy, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Resist Energy"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Resist Energy/Communal", path = "ultimate_combat/spell/resist_energy_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 min./level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 3: Alchemist, Arcanist, Cleric, Druid, Hunter, Hunter, Hunter, Hunter, Hunter, Hunter, Inquisitor, Investigator, Oracle, Paladin, Ranger, Sorcerer, Summoner, Warpriest, Wizard
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 min./level
Saving Throw: Fortitude negates (harmless)
Spell Resistance: yes (harmless)
:::

_As resist energy, but you may divide the duration among creatures touched._

This spell functions like _[resist energy](ref/spell/resist-energy)_, except you divide the duration
in 10-minute intervals among the creatures touched.
