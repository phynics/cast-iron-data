+++
id = "ref/spell/constricting-coils"
kind = "spell"
title = "Constricting Coils"
source_ids = ["pathfinder-42-sanctum-of-the-serpent-god"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "constricting_coils", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hold-monster" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a snakeskin)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a snakeskin)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (d); see text
Saving throw: Will negates; see text
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Pathfinder \#42: Sanctum of the Serpent God pg 71

> _Priests of [Ydersius](ref/faith/ydersius) have access to the following spell._

This spell functions like [hold monster](ref/spell/hold-monster), except that the target is
constricted as if by the coils of a large snake, taking 1d6+6 points of bludgeoning damage each
round that it fails its save. A successful save ends both the paralyzing and constriction effects.
