+++
id = "ref/carried/ultimate-magic/spells/forbid-action/greater"
kind = "spell"
title = "Forbid Action, Greater"
source_ids = ["ultimate-magic"]
section = ["Spells", "Forbid Action"]
tags = ["enchantment", "compulsion", "language-dependent", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Forbid Action/Greater", path = "ultimate_magic/spell/forbid_action_greater.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["language-dependent", "mind-affecting"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. +5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
School: enchantment (compulsion) \[language-dependent, mind-affecting\]
Level: 5: Cleric, Inquisitor, Oracle, Warpriest
Casting Time: 1 standard action
Components: V
Range: close (25 ft. +5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving Throw: Will negates
Spell Resistance: yes
:::

_As forbid action, but 1 creature/level._

This spell functions as _[forbid action](ref/spell/forbid-action)_, except up to one creature per
level may be affected. Each creature must receive the same forbidden action.
