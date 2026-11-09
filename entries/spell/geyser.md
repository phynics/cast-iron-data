+++
id = "ref/spell/geyser"
kind = "spell"
title = "Geyser"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geyser", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "225"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["fire", "water"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of lava rock)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "spout of boiling water filling a 5 ft. square and spraying upward 10 ft./2 levels" },
]
duration = "concentration+ 1 round/level"
saving_throw = "Reflex partial (see below)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Druid, Hunter\
5: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of lava rock)
Range: long (400 ft. + 40 ft./level)
Duration: concentration+ 1 round/level
Saving throw: Reflex partial (see below)
Spell resistance: no
Effect: spout of boiling water filling a 5 ft. square and spraying upward 10 ft./2 levels
Subschool: Creation
Descriptors: fire, water
:::

You cause a column of boiling water to spring forth from any horizontal surface, knocking over
creatures directly over it and exposing nearby creatures to searing droplets as its spray falls back
to the ground.

Any creature entering the geyser, or occupying the square it appears in, must make a Reflex saving
throw to avoid being hurled into the air and then tossed to the ground. If the creature fails its
saving throw, it takes 3d6 points of fire damage from the boiling water and also takes falling
damage based upon the height of the geyser (e.g., if the geyser is 50 feet tall, the creature takes
5d6 falling damage), landing prone in a random square adjacent to the geyser. A successful saving
throw halves the damage and negates the falling damage, and the creature is moved to the closest
square adjacent to the geyser (Large-sized or larger creatures are moved enough so that they are not
on top of the geyser but still adjacent to it). This movement does not provoke attacks of
opportunity and does not count toward the creature's normal movement.

In addition, the geyser sprays boiling water in a hemispherical emanation around its square. The
radius of this emanation is equal to one-half the geyser's height (e.g., a 50-foot geyser has a
25-foot-radius emanation). Any creature within this area, including yourself, takes 1d6 points of
fire damage each round as droplets of boiling water cascade on them.

You can choose to make a smaller geyser than your level permits if an obstruction prevents it from
reaching its full height, or if you simply want to create a spread of boiling rain that's smaller
than what would be created by a full-height geyser spell.
