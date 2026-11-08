+++
id = "ref/spell/bulls-strength-mass"
kind = "spell"
title = "Mass Bull's Strength"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bulls_strength_mass", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bulls-strength" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Magus", level = 6 },
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
components = "V, S, M/DF (a few hairs, or a pinch of dung, from a bull)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner\
6: Arcanist, Cleric, Druid, Hunter, Magus, Oracle, Psychic, Shaman, Sorcerer, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a few hairs, or a pinch of dung, from a bull)
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Mass Bull's Strength

**Sources:** PRPG Core Rulebook pg 251

This spell functions like [bull's strength](ref/spell/bulls-strength), except that it affects
multiple creatures.
