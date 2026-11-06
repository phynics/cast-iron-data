+++
id = "ref/spell/diminish-resistance"
kind = "spell"
title = "Diminish Resistance"
source_ids = ["planar-adventures", "monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "diminish_resistance", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of coarse sand)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bard, Cleric, Inquisitor, Magus, Mesmerist, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of coarse sand)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
:::

**Sources:** Planar Adventures pg 40, Monster Hunter's Handbook pg 30

You weaken a creature's resistance against one energy type you select: acid, cold, electricity,
fire, or sonic. The creature's resistance to that energy type decreases by 5 (minimum 0), plus an
additional 5 for every 5 caster levels beyond 3rd (to a maximum of 20 at 18th level).
