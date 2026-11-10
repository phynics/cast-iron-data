+++
id = "ref/carried/core-rulebook/spells/inflict-critical-wounds/mass"
kind = "spell"
title = "Inflict Critical Wounds, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Inflict Critical Wounds"]
tags = ["necromancy"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Inflict Critical Wounds/Mass", path = "core_rulebook/spell/inflict_critical_wounds_mass.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Warpriest", level = 8 },
  { class = "Witch", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
School: necromancy
Level: 8: Cleric, Oracle, Shaman, Warpriest\
9: Witch
Casting Time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving Throw: Will half
Spell Resistance: yes
:::

_Deals 4d8 damage + 1/level, affects 1 subject/level._

This spell functions like _[mass inflict light wounds](ref/spell/inflict-light-wounds-mass)_, except
that it deals 4d8 points of damage + 1 point per caster level (maximum +40).
