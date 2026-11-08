+++
id = "ref/spell/suggestion-mass"
kind = "spell"
title = "Mass Suggestion"
source_ids = ["core-rulebook", "mythic-adventures", "blood-of-the-beast", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suggestion_mass", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/suggestion" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, M (a snake's tongue and a honeycomb)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level or until completed"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Occultist, Psychic, Skald\
6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, M (a snake's tongue and a honeycomb)
Range: medium (100 ft. + 10 ft./level)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 hour/level or until completed
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

### Mythic Suggestion

**Sources:** Mythic Adventures pg 109

Mythic suggestion loses the language-dependent descriptor, and can target one or more living
creatures in a 10-foot-radius burst.

### Mass Suggestion

**Sources:** PRPG Core Rulebook pg 350

This spell functions like [suggestion](ref/spell/suggestion), except that it can affect more
creatures. The same suggestion applies to all these creatures.
