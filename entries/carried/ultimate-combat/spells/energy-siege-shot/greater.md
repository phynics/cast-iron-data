+++
id = "ref/carried/ultimate-combat/spells/energy-siege-shot/greater"
kind = "spell"
title = "Energy Siege Shot, Greater"
source_ids = ["ultimate-combat"]
section = ["Spells", "Energy Siege Shot"]
tags = ["transmutation", "variable"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Energy Siege Shot/Greater", path = "ultimate_combat/spell/energy_siege_shot_greater.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["variable"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (a ball of pitch)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one siege engine of any size" },
]
duration = "10 minute/level"
saving_throw = "Fortitude negates (harmless, object)"
spell_resistance = "yes (harmless/object)"
+++

::: statblock
School: transmutation \[variable\]
Level: 6: Arcanist, Sorcerer, Summoner, Wizard
Casting Time: 10 minutes
Components: V, S, M (a ball of pitch)
Range: close (25 ft. + 5 ft./2 levels)
Target: one siege engine of any size
Duration: 10 minute/level
Saving Throw: Fortitude negates (harmless, object)
Spell Resistance: yes (harmless/object)
:::

_As energy siege shot, but you can affect any size siege engine._

This spell functions like energy shot, except it can target siege engines of any size, not just
Large siege engines.
