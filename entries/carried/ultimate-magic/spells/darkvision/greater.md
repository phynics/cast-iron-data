+++
id = "ref/carried/ultimate-magic/spells/darkvision/greater"
kind = "spell"
title = "Darkvision, Greater"
source_ids = ["ultimate-magic"]
section = ["Spells", "Darkvision"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Darkvision/Greater", path = "ultimate_magic/spell/darkvision_greater.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (either a pinch of dried carrot or an agate)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: transmutation
Level: 4: Alchemist, Antipaladin, Arcanist, Hunter, Hunter, Investigator, Ranger, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S, M (either a pinch of dried carrot or an agate)
Range: touch
Target: creature touched
Duration: 1 hour/level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_See 120 ft. in total darkness._

This spell functions as _[darkvision](ref/spell/darkvision)_, except the target's
[darkvision](ref/rule/darkvision) has a range of 120 feet.
