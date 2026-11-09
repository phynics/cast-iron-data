+++
id = "ref/carried/core-rulebook/spells/enlarge-person/mass"
kind = "spell"
title = "Enlarge Person, Mass"
aon = "SpellDisplay.aspx?ItemName=Enlarge%20Person%2C%20Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Enlarge Person"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Enlarge Person/Mass", path = "core_rulebook/spell/enlarge_person_mass.json" },
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
components = "V, S, M (powdered iron)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "One humanoid creature/level, no two of which can be more than 30 ft. apart" },
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
Components: V, S, M (powdered iron)
Range: close (25 ft. + 5 ft./2 levels)
Target: One humanoid creature/level, no two of which can be more than 30 ft. apart
Duration: 1 min./level (D)
Saving Throw: Fortitude negates
Spell Resistance: yes
:::

_1 humanoid creature/level doubles in size._

This spell functions like _[enlarge person](ref/spell/enlarge-person)_, except that it affects
multiple creatures.
