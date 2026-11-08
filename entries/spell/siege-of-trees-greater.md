+++
id = "ref/spell/siege-of-trees-greater"
kind = "spell"
title = "Greater Siege of Trees"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_of_trees_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/siege-of-trees" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one Gargantuan, Huge, or Large plant per three caster levels" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 9: Druid
Casting time: 10 minutes
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Targets: one Gargantuan, Huge, or Large plant per three caster levels
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
:::

### Greater Siege of Trees

**Sources:** Ultimate Combat pg 244

As [siege of trees](ref/spell/siege-of-trees), but you can affect larger-sized plants. Each plant
acts as a catapult of its size.
