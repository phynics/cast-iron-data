+++
id = "ref/spell/blacklight"
kind = "spell"
title = "Blacklight"
source_ids = ["pathfinder-campaign-setting"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blacklight", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft.-radius emanation" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates or none (object)"
spell_resistance = "yes or no (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates or none (object)
Spell resistance: yes or no (object)
Area: 20-ft.-radius emanation
Descriptors: darkness
:::

**Sources:** Pathfinder Campaign Setting pg 206

You create an area of total darkness. The darkness is impenetrable even to
[darkvision](ref/rule/darkvision), but you can see normally within it. Creatures outside the spell's
area, even you, cannot see through it.

You can cast the spell on a point in space, but the effect is stationary unless cast on a mobile
object. You can cast the spell on a creature, and the effect then radiates from the creature and
moves as it moves. Unattended objects and points in space do not get saving throws or benefit from
[spell resistance](ref/rule/spell-resistance). Blacklight counters or dispels any light spell of
equal or lower level. [Daylight](ref/spell/daylight) counters or dispels blacklight.
