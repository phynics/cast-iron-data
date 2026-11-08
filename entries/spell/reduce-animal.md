+++
id = "ref/spell/reduce-animal"
kind = "spell"
title = "Reduce Animal"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reduce_animal", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/reduce-person" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one willing animal of Small, Medium, Large, or Huge size" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter\
3: Ranger
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: one willing animal of Small, Medium, Large, or Huge size
:::

**Sources:** PRPG Core Rulebook pg 330

This spell functions like [reduce person](ref/spell/reduce-person), except that it affects a single
willing animal. Reduce the damage dealt by the animal's natural attacks
[as appropriate for its new size](ref/umr/natural-attacks).
