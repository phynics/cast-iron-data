+++
id = "ref/carried/core-rulebook/spells/heroism/greater"
kind = "spell"
title = "Heroism, Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Heroism"]
tags = ["enchantment", "compulsion", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Heroism/Greater", path = "core_rulebook/spell/heroism_greater.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 min./level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: enchantment (compulsion) \[mind-affecting\]
Level: 5: Bard, Skald, Summoner\
6: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: touch
Target: creature touched
Duration: 1 min./level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_Gives +4 bonus on attack rolls, saves, skill checks; immunity to fear; temporary hp._

This spell functions like _[heroism](ref/spell/heroism)_, except the creature gains a +4 morale
bonus on attack rolls, saves, and skill checks, immunity to fear effects, and temporary hit points
equal to your caster level (maximum 20).
