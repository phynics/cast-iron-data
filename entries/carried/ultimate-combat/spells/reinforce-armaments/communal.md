+++
id = "ref/carried/ultimate-combat/spells/reinforce-armaments/communal"
kind = "spell"
title = "Reinforce Armaments, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Reinforce Armaments"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Reinforce Armaments/Communal", path = "ultimate_combat/spell/reinforce_armaments_communal.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a metal pin)"
range = "touch"
effects = [
  { label = "Target", value = "armor suits or weapons touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless, object)"
spell_resistance = "yes (harmless, object)"
+++

::: statblock
School: transmutation
Level: 2: Arcanist, Cleric, Magus, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting Time: 1 standard action
Components: V, S, M/DF (a metal pin)
Range: touch
Target: armor suits or weapons touched
Duration: 10 minutes/level
Saving Throw: Will negates (harmless, object)
Spell Resistance: yes (harmless, object)
:::

_As reinforce armaments, but you may divide the spell's duration among objects touched._

This spell functions like _[reinforce armaments](ref/spell/reinforce-armaments)_, except you divide
the duration in 10-minute intervals among the objects touched.
