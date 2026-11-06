+++
id = "ref/carried/core-rulebook/spells/arcane-sight/greater"
kind = "spell"
title = "Arcane Sight, Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Arcane Sight"]
tags = ["divination"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Arcane Sight/Greater", path = "core_rulebook/spell/arcane_sight_greater.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 min./level (D)"
+++

::: statblock
School: divination
Level: 7: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 1 min./level (D)
:::

_As arcane sight, but also reveals magic effects on creatures and objects._

This spell functions like _[arcane sight](ref/spell/arcane-sight)_, except that you automatically
know which spells or magical effects are active upon any individual or object you see.

Unlike _[arcane sight](ref/spell/arcane-sight)_, this spell cannot be made permanent with a
_[permanency](ref/spell/permanency)_ spell.
