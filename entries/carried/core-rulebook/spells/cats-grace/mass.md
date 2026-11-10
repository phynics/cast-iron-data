+++
id = "ref/carried/core-rulebook/spells/cats-grace/mass"
kind = "spell"
title = "Cat's Grace, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Cats Grace"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Cats Grace/Mass", path = "core_rulebook/spell/cats_grace_mass.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 4 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (pinch of cat fur)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 min./level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
School: transmutation
Level: 4: Summoner\
6: Arcanist, Bard, Druid, Hunter, Hunter, Magus, Skald, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S, M (pinch of cat fur)
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 min./level
Saving Throw: Will negates (harmless)
Spell Resistance: yes
:::

_As cat's grace, affects 1 subject/level._

This spell functions like _[cat's grace](ref/spell/cats-grace)_, except that it affects multiple
creatures.
