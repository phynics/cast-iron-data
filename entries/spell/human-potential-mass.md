+++
id = "ref/spell/human-potential-mass"
kind = "spell"
title = "Mass Human Potential"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "human_potential_mass", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/human-potential" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a human hair)"
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
Level: 6: Arcanist, Bard, Psychic, Skald, Sorcerer, Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a human hair)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

### Mass Human Potential

**Sources:** Arcane Anthology pg 9

This spell functions like [human potential](ref/spell/human-potential), except it affects multiple
creatures. Each target can choose a different ability score to be enhanced by this spell.
