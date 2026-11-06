+++
id = "ref/spell/flurry-of-snowballs"
kind = "spell"
title = "Flurry of Snowballs"
source_ids = ["pathfinder-67-the-snows-of-summer", "people-of-the-north"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flurry_of_snowballs", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold", "water"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Druid, Hunter, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: no
Area: cone-shaped burst
Descriptors: cold, water
:::

**Sources:** Pathfinder \#67: The Snows of Summer pg 72, People of the North pg 26

You send a flurry of snowballs hurtling at your foes. Any creature in the area takes 4d6 points of
cold damage from being pelted with the icy spheres.
