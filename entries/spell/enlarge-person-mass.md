+++
id = "ref/spell/enlarge-person-mass"
kind = "spell"
title = "Mass Enlarge Person"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enlarge_person_mass", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/enlarge-person" },
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

### Mythic Enlarge Person

**Sources:** Mythic Adventures pg 93

You can increase the target's size by up to two size categories, to a maximum of Huge. If the target
grows two sizes, its weight increases by a factor of 25, it gains a +4 size bonus to Strength, and
takes a -4 size penalty to Dexterity and a -2 penalty on attack rolls and to AC because of its
increased size. A Medium humanoid creature whose size increases to Huge has a space of 15 feet and a
natural reach of 10 feet. Mythic enlarge person counters and dispels mythic
_[reduce person](ref/spell/reduce-person)._

### Mass Enlarge Person

**Sources:** PRPG Core Rulebook pg 278

This spell functions like [enlarge person](ref/spell/enlarge-person), except that it affects
multiple creatures.
