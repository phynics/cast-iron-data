+++
id = "ref/spell/staggering-fall"
kind = "spell"
title = "Staggering Fall"
source_ids = ["rival-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "staggering_fall", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one falling creature" },
]
duration = "1 round/level (see below)"
saving_throw = "Fortitude partial (see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Cleric, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 immediate action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (see below)
Saving throw: Fortitude partial (see below)
Spell resistance: yes
Target: one falling creature
:::

**Sources:** Rival Guide pg 35

This spell must be cast on a creature as it falls, either from a height or after being knocked prone
or tripped. The magic of this spell causes the creature to hit the ground particularly hard,
knocking the wind from it. The creature takes an additional 1d6 points of damage from the fall. In
addition, the creature becomes staggered for the duration of the spell unless it makes a Will save.
Each round the spell's effects persist, the creature may attempt a new Will save as a free action to
end the staggered effect early. A creature under the effects of this spell must take a standard
action to stand up.
