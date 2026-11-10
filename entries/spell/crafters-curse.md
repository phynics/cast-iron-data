+++
id = "ref/spell/crafters-curse"
kind = "spell"
title = "Crafter's Curse"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crafters_curse", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "213"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a broken tool)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Occultist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a broken tool)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

The target of crafter's curse takes a -5 penalty on all Craft skill checks while the spell lasts.
