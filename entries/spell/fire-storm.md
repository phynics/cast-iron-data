+++
id = "ref/spell/fire-storm"
kind = "spell"
title = "Fire Storm"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fire_storm", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 7 },
  { class = "Oracle", level = 8 },
  { class = "Shaman", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "two 10-ft. cubes per level (S)" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Druid\
8: Cleric, Oracle, Shaman
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: two 10-ft. cubes per level (S)
Descriptors: fire
:::

**Sources:** PRPG Core Rulebook pg 282

When a fire storm spell is cast, the whole area is shot through with sheets of roaring flame. The
raging flames do not harm natural vegetation, ground cover, or any plant creatures in the area that
you wish to exclude from damage. Any other creature within the area takes 1d6 points of fire damage
per caster level (maximum 20d6). Creatures that fail their Reflex save catch on fire, taking 4d6
points of fire damage each round until the flames are extinguished. Extinguishing the flames is a
full-round action that requires a DC 20 Reflex save.
