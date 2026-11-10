+++
id = "ref/spell/dust-of-twilight"
kind = "spell"
title = "Dust of Twilight"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dust_of_twilight", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "217"

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["darkness"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (coal dust)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "creatures and objects in a 10-ft. spread" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (fatigue only)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Bloodrager, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (coal dust)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude negates (fatigue only)
Spell resistance: no
Target: creatures and objects in a 10-ft. spread
Descriptors: darkness
:::

A shower of iridescent black particles clings to and extinguishes torches, lanterns, sunrods, and
similar mundane light sources and dispels any spell of 2nd level or lower with the light descriptor
(as [dispel magic](ref/spell/dispel-magic)). Creatures in the area must make a Fortitude save or
become fatigued.
