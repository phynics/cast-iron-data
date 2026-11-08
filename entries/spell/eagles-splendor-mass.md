+++
id = "ref/spell/eagles-splendor-mass"
kind = "spell"
title = "Mass Eagle's Splendor"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eagles_splendor_mass", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/eagles-splendor" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (feathers or droppings from an eagle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner\
6: Arcanist, Bard, Cleric, Oracle, Psychic, Shaman, Skald, Sorcerer, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (feathers or droppings from an eagle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
:::

**Sources:** PRPG Core Rulebook pg 275

This spell functions like [eagle's splendor](ref/spell/eagles-splendor), except that it affects
multiple creatures.
