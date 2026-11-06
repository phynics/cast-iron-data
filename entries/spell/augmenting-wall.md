+++
id = "ref/spell/augmenting-wall"
kind = "spell"
title = "Augmenting Wall"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "augmenting_wall", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "evocation [see text]"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "20-ft.-high wall of energy whose area is up to one 10-ft. square/level" },
]
duration = "1 round/2 levels (see text)"
saving_throw = "none"
spell_resistance = "no (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation \[see text\]
Level: 5: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/2 levels (see text)
Saving throw: none
Spell resistance: no (object)
Effect: 20-ft.-high wall of energy whose area is up to one 10-ft. square/level
:::

**Sources:** Ranged Tactics Toolbox pg 30

You create a wall of faintly shimmering elemental energy. Upon casting the spell, choose either
acid, cold, electricity, or fire. The spell gains the chosen descriptor, and any thrown weapons or
ammunition that pass through the augmenting wall as part of a ranged attack deal 1d6 points of
energy damage of the specified type in addition to their normal damage. The wall has no effect on
melee weapons or items not thrown as part of an attack.

As you cast the spell, you can limit the wall so that it only affects ranged weapons passing through
it in the direction of your choice. Doing so halves the spell's duration.
