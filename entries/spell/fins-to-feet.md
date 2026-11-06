+++
id = "ref/spell/fins-to-feet"
kind = "spell"
title = "Fins to Feet"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fins_to_feet", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "willing creature touched" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Druid, Hunter, Red Mantis Assassin, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: willing creature touched
Subschool: Polymorph
:::

**Sources:** Advanced Race Guide pg 195

> _[Merfolk](ref/race/merfolk) have access to the following spell._

You transform the target's fins, flippers, or tail into legs and feet, allowing it to walk on land.
The target loses its swim speed but gains a base speed appropriate for a humanoid of its size (speed
30 if a Medium or larger creature, speed 20 if Small). If the creature is immersed in water for 1
round, the transformation reverts, allowing it to swim normally. One round after leaving the water,
the transformation occurs again, allowing it to walk.

This spell only works on merfolk, tritons, seals, fish, and other creatures whose bodies or limbs
are used mainly for swimming and are not suitable for walking. It does not give the target the
ability to breathe air.
