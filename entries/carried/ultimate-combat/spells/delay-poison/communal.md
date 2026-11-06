+++
id = "ref/carried/ultimate-combat/spells/delay-poison/communal"
kind = "spell"
title = "Delay Poison, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Delay Poison"]
tags = ["conjuration", "healing"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Delay Poison/Communal", path = "ultimate_combat/spell/delay_poison_communal.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
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
  { class = "Skald", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: conjuration (healing)
Level: 3: Alchemist, Bard, Cleric, Druid, Hunter, Hunter, Hunter, Hunter, Hunter, Inquisitor, Investigator, Oracle, Paladin, Ranger, Skald, Warpriest, Witch
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 1 hour/level
Saving Throw: Fortitude negates (harmless)
Spell Resistance: yes (harmless)
:::

_As delay poison, but you may divide the duration among creatures touched._

This spell functions like _[delay poison](ref/spell/delay-poison)_, except you divide the duration
in 1-hour intervals among the creatures touched.
