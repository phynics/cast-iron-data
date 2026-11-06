+++
id = "ref/carried/core-rulebook/spells/command/greater"
kind = "spell"
title = "Command, Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Command"]
tags = ["enchantment", "compulsion", "language-dependent", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Command/Greater", path = "core_rulebook/spell/command_greater.json" },
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
range = "close (25 ft. + 5 ft./2 levels)"
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
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving Throw: Will negates
Spell Resistance: yes
:::

_As command, but affects one subject/level._

This spell functions like _[command](ref/spell/command)_, except that up to one creature per level
may be affected, and the activities continue beyond 1 round. At the start of each commanded
creature's action after the first, it gets another Will save to attempt to break free from the
spell. Each creature must receive the same command.
