+++
id = "ref/carried/core-rulebook/spells/reduce-person/mass"
kind = "spell"
title = "Reduce Person, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Reduce Person"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Reduce Person/Mass", path = "core_rulebook/spell/reduce_person_mass.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (a pinch of powdered iron)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 min./level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
School: transmutation
Level: 3: Summoner\
4: Arcanist, Bloodrager, Magus, Sorcerer, Wizard
Casting Time: 1 round
Components: V, S, M (a pinch of powdered iron)
Range: close (25 ft. + 5 ft./2 levels)
Target: one humanoid creature/level, no two of which can be more than 30 ft. apart
Duration: 1 min./level (D)
Saving Throw: Fortitude negates
Spell Resistance: yes
:::

_As reduce person, but affects 1 humanoid creature/level._

This spell functions like _[reduce person](ref/spell/reduce-person)_, except that it affects
multiple creatures.
