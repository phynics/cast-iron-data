+++
id = "ref/spell/owls-wisdom-mass"
kind = "spell"
title = "Mass Owl's Wisdom"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "owls_wisdom_mass", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/owls-wisdom" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (feathers or droppings from an owl)"
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
6: Arcanist, Cleric, Druid, Hunter, Oracle, Psychic, Shaman, Sorcerer, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (feathers or droppings from an owl)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

## Owl's Wisdom

**Sources:** PRPG Core Rulebook pg 318

The transmuted creature becomes wiser. The spell grants a +4 enhancement bonus to Wisdom, adding the
usual benefit to Wisdom-related skills. Clerics, druids, and rangers (and other Wisdom-based
spellcasters) who receive owl's wisdom do not gain any additional bonus spells for the increased
Wisdom, but the save DCs for their spells increase.

### Mass Owl's Wisdom

**Sources:** PRPG Core Rulebook pg 318

This spell functions like [owl's wisdom](ref/spell/owls-wisdom), except that it affects multiple
creatures.
