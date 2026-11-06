+++
id = "ref/spell/cowards-cowl"
kind = "spell"
title = "Coward's Cowl"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cowards_cowl", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Alchemist, Arcanist, Bard, Cleric, Investigator, Mesmerist, Oracle, Psychic, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Agents of Evil pg 30

You imbue the target with a compulsion to avoid threats, enhancing its defensive instincts. So long
as the affected creature does not move closer to enemies during its turn, or moves at least 5 feet
away from adjacent enemies, it gains a +1 morale bonus to its AC, and a +1 morale bonus on saves and
on attack rolls made as readied actions and attacks of opportunity. Alternatively, if the affected
creature does not close with its enemies, it can increase the DC of all spells it casts as part of a
readied action by 1. If the subject of the spell willingly moves toward a threatening creature, the
spell immediately ends.

While affected by coward's cowl, a creature takes a -2 penalty on all saving throws against fear
effects.
