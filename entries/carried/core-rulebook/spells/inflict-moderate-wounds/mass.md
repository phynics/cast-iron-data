+++
id = "ref/carried/core-rulebook/spells/inflict-moderate-wounds/mass"
kind = "spell"
title = "Inflict Moderate Wounds, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Inflict Moderate Wounds"]
tags = ["necromancy"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Inflict Moderate Wounds/Mass", path = "core_rulebook/spell/inflict_moderate_wounds_mass.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 7 },
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
Level: 6: Cleric, Inquisitor, Oracle, Shaman, Warpriest\
7: Witch
Casting Time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving Throw: Will half
Spell Resistance: yes
:::

_Deals 2d8 damage + 1/level, affects 1 subject/level._

This spell functions like _[mass inflict light wounds](ref/spell/inflict-light-wounds-mass)_, except
that it deals 2d8 points of damage + 1 point per caster level (maximum +30).
