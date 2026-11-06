+++
id = "ref/carried/ultimate-magic/spells/daze/mass"
kind = "spell"
title = "Daze, Mass"
source_ids = ["ultimate-magic"]
section = ["Spells", "Daze"]
tags = ["enchantment", "compulsion", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Daze/Mass", path = "ultimate_magic/spell/daze_mass.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one or more humanoid creatures, no two of which may be more than 30 ft. apart" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
School: enchantment (compulsion) \[mind-affecting\]
Level: 4: Arcanist, Bard, Inquisitor, Skald, Sorcerer, Summoner, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Targets: one or more humanoid creatures, no two of which may be more than 30 ft. apart
Duration: 1 round
Saving Throw: Will negates
Spell Resistance: yes
:::

_As daze, but affecting multiple creatures._

This spell functions as _[daze](ref/spell/daze)_, except as noted above.
