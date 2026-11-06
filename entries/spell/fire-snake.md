+++
id = "ref/spell/fire-snake"
kind = "spell"
title = "Fire Snake"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fire_snake", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a snake scale)"
range = "60 ft."
effects = [
  { label = "Area", value = "see text" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Druid, Hunter, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a snake scale)
Range: 60 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: see text
Descriptors: fire
:::

**Sources:** Advanced Player's Guide pg 222

You create a sinuous line of flames that you may shape as desired. The fire snake affects one 5-foot
square per caster level, and each square must be adjacent to the previous square, starting with you.
The fire snake may not extend beyond its maximum range. Creatures in the path of the fire snake take
1d6 points of fire damage per caster level (maximum 15d6).

### Mythic Fire Snake

**Sources:** Mythic Adventures pg 94\
The damage dealt increases to 1d10 points of damage per level (maximum 15d10). Any creature that
fails its saving throw against the spell is grappled by a snake made of fire that lasts for 1 round
per caster level. The snake can be dispelled, but not attacked. A grappled creature takes 1d10
points of fire damage on your turn each round. The snake's CMB is equal to your caster level plus
your tier, and its CMD is equal to its CMB + 10.

_Augmented (6th):_ If you expend two uses of mythic power, the maximum damage increases to 20d10,
and any creature that fails its saving throw against the spell is pinned instead of grappled.
