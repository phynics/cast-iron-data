+++
id = "ref/spell/enlarge-person-mass"
kind = "spell"
title = "Mass Enlarge Person"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enlarge_person_mass", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/enlarge-person" },
]
[[sources]]
publication = "core-rulebook"
page = "278"

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
components = "V, S, M (powdered iron)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "One humanoid creature/level, no two of which can be more than 30 ft. apart" },
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
Components: V, S, M (powdered iron)
Range: close (25 ft. + 5 ft./2 levels)
Target: One humanoid creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
:::

### Mass Enlarge Person

This spell functions like [enlarge person](ref/spell/enlarge-person), except that it affects
multiple creatures.
