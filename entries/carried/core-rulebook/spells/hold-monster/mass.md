+++
id = "ref/carried/core-rulebook/spells/hold-monster/mass"
kind = "spell"
title = "Hold Monster, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Hold Monster"]
tags = ["enchantment", "compulsion", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Hold Monster/Mass", path = "core_rulebook/spell/hold_monster_mass.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
components = ": V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)"
effects = [
  { label = "Targets", value = "one or more creatures, no two of which can be more than 30 ft. apart" },
]
+++

::: statblock
School: enchantment (compulsion) \[mind-affecting\]
Level: 9: Arcanist, Sorcerer, Witch, Wizard
Components: : V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)
Targets: one or more creatures, no two of which can be more than 30 ft. apart
:::

_As hold monster, but all within 30 ft._

This spell functions like _[hold person](ref/spell/hold-person)_, except that it affects multiple
creatures and holds any living creature that fails its Will save.
