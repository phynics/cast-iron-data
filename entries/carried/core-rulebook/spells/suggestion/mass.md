+++
id = "ref/carried/core-rulebook/spells/suggestion/mass"
kind = "spell"
title = "Suggestion, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Suggestion"]
tags = ["enchantment", "compulsion", "language-dependent", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Suggestion/Mass", path = "core_rulebook/spell/suggestion_mass.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["language-dependent", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, M (a snake's tongue and a honeycomb)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level or until completed"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
School: enchantment (compulsion) \[language-dependent, mind-affecting\]
Level: 5: Bard, Skald\
6: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, M (a snake's tongue and a honeycomb)
Range: medium (100 ft. + 10 ft./level)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 hour/level or until completed
Saving Throw: Will negates
Spell Resistance: yes
:::

_As suggestion, affects 1 subject/level._

This spell functions like _[suggestion](ref/spell/suggestion)_, except that it can affect more
creatures. The same _[suggestion](ref/spell/suggestion)_ applies to all these creatures.
