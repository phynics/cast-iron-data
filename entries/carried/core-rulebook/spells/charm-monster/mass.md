+++
id = "ref/carried/core-rulebook/spells/charm-monster/mass"
kind = "spell"
title = "Charm Monster, Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Charm Monster"]
tags = ["enchantment", "charm", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Charm Monster/Mass", path = "core_rulebook/spell/charm_monster_mass.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
components = "V"
effects = [
  { label = "Targets", value = "One or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 day/level"
+++

::: statblock
School: enchantment (charm) \[mind-affecting\]
Level: 6: Bard, Skald, Summoner\
8: Arcanist, Sorcerer, Witch, Wizard
Components: V
Targets: One or more creatures, no two of which can be more than 30 ft. apart
Duration: 1 day/level
:::

_As charm monster, but all within 30 ft._

This spell functions like _[charm monster](ref/spell/charm-monster)_, except that
_[mass charm monster](ref/spell/charm-monster-mass)_ affects a number of creatures whose combined HD
do not exceed twice your level, or at least one creature regardless of HD. If there are more
potential targets than you can affect, you choose them one at a time until you must choose a
creature with too many HD to affect.
