+++
id = "ref/spell/binding-earth-mass"
kind = "spell"
title = "Mass Binding Earth"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "binding_earth_mass", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or unattended object (see text)" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature or unattended object (see text)
Descriptors: earth
:::

## Binding Earth

**Sources:** Advanced Race Guide pg 149

> _[Oreads](ref/race/oread) have access to the following spell._

If the target of this spell fails its Fortitude save, areas of earth and stone floor act as a
snapping quagmire that pulls the target down and damages it if it attempts to move through such
terrain.

If the target is a creature, it treats all areas of earth and stone it moves through as difficult
terrain. Furthermore, for each 5 feet a creature moves through such areas, it takes 1d6 points of
damage. Creatures with a burrow speed or the earth glide ability are unaffected by binding earth.

If cast on an unattended object resting on an area of stone or earth, the stone or earth warps and
wraps around it, pulling it firmly to the ground. A DC 15 Strength check is required to pull the
object free from snapping earth or stone.

### Mass Binding Earth

**Sources:** Advanced Race Guide pg 149

> _[Oreads](ref/race/oread) have access to the following spell._

This spell functions as binding earth, except as noted above.
