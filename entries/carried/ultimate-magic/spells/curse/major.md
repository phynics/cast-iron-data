+++
id = "ref/carried/ultimate-magic/spells/curse/major"
kind = "spell"
title = "Curse, Major"
source_ids = ["ultimate-magic"]
section = ["Spells", "Curse"]
tags = ["necromancy", "curse"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Curse/Major", path = "ultimate_magic/spell/curse_major.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
School: necromancy \[curse\]
Level: 5: Cleric, Oracle, Shaman, Warpriest, Witch\
6: Arcanist, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature
Duration: permanent
Saving Throw: Will negates
Spell Resistance: yes
:::

_As bestow curse, but harder to remove._

This spell functions as _[bestow curse](ref/spell/bestow-curse)_, except the DC to remove the curse
is equal to the save DC + 5.
