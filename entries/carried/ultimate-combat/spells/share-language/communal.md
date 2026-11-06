+++
id = "ref/carried/ultimate-combat/spells/share-language/communal"
kind = "spell"
title = "Share Language, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Share Language"]
tags = ["divination"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Share Language/Communal", path = "ultimate_combat/spell/share_language_communal.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a page from a dictionary)"
range = "touch"
effects = [
  { label = "Targets", value = "creatures touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: divination
Level: 2: Bard, Skald\
3: Arcanist, Cleric, Druid, Hunter, Hunter, Oracle, Sorcerer, Warpriest, Wizard
Casting Time: 1 standard action
Components: V, S, M (a page from a dictionary)
Range: touch
Targets: creatures touched
Duration: 24 hours
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As share language, but you may divide the duration among creatures touched._

This spell functions like _[share language](ref/spell/share-language)_ , except you divide the
duration in 1-hour increments among the creatures touched.
