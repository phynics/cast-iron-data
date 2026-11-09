+++
id = "ref/spell/scorching-ray"
kind = "spell"
title = "Scorching Ray"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scorching_ray", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "337"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one or more rays" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Adept, Arcanist, Bloodrager, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Effect: one or more rays
Descriptors: fire
:::

You blast your enemies with a searing beam of fire. You may fire one ray, plus one additional ray
for every four levels beyond 3rd (to a maximum of three rays at 11th level). Each ray requires a
ranged touch attack to hit and deals 4d6 points of fire damage. The rays may be fired at the same or
different targets, but all rays must be aimed at targets within 30 feet of each other and fired
simultaneously.
