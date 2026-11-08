+++
id = "ref/spell/battle-trance"
kind = "spell"
title = "Battle Trance"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "battle_trance", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Alchemist, Antipaladin, Hunter, Inquisitor, Investigator, Ranger\
4: Cleric, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

**Sources:** Advanced Race Guide pg 58

> _[Half-orcs](ref/race/half-orc) have access to the following spell._

You are transformed into a single-minded force of destruction. You gain the ferocity monster special
ability, a number of temporary hit points equal to 1d6 + your caster level (maximum +10), and a +4
morale bonus on saving throws against mind-affecting effects. You cannot use the withdraw action or
willingly move away from a creature that has attacked you.

When you use this spell, you immediately take 4 points of Intelligence damage. You must make a DC 20
[concentration](ref/rule/concentration) check to cast spells, and all other concentration checks to
cast spells have a -5 penalty.
