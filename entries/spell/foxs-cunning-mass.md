+++
id = "ref/spell/foxs-cunning-mass"
kind = "spell"
title = "Mass Fox's Cunning"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "foxs_cunning_mass", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/foxs-cunning" },
]
[[sources]]
publication = "core-rulebook"
page = "286"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (hairs or dung from a fox)"
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
6: Arcanist, Bard, Psychic, Skald, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (hairs or dung from a fox)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

### Mass Fox's Cunning

This spell functions like [fox's cunning](ref/spell/foxs-cunning), except that it affects multiple
creatures.
