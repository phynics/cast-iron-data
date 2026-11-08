+++
id = "ref/spell/reduce-person-mass"
kind = "spell"
title = "Mass Reduce Person"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reduce_person_mass", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/reduce-person" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (a pinch of powdered iron)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Summoner\
4: Arcanist, Bloodrager, Magus, Psychic, Red Mantis Assassin, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 round
Components: V, S, M (a pinch of powdered iron)
Range: close (25 ft. + 5 ft./2 levels)
Target: one humanoid creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
:::

### Mass Reduce Person

**Sources:** PRPG Core Rulebook pg 331

This spell functions like [reduce person](ref/spell/reduce-person), except that it affects multiple
creatures.
