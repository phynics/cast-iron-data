+++
id = "ref/spell/firestream"
kind = "spell"
title = "Firestream"
source_ids = ["advanced-race-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "firestream", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "20 ft."
effects = [
  { label = "Area", value = "20-ft. line" },
]
duration = "concentration, up to 1 round/level; see text"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 20 ft.
Duration: concentration, up to 1 round/level; see text
Saving throw: Reflex half
Spell resistance: yes
Area: 20-ft. line
Descriptors: fire
:::

**Sources:** Advanced Race Guide pg 131

> _[Ifrits](ref/race/ifrit) have access to the following spell._

A rushing stream of fire sprays from your outstretched hand, dealing 2d6 points of fire damage to
every creature in the area. Each round you continue to concentrate on the spell, you can select a
new area for it to affect.

Firestream sets fire to combustibles and damages objects in the area. It can melt metals with low
melting points, such as lead, gold, copper, silver, and bronze. If the damage caused to an
interposing barrier shatters or breaks through it, the firestream may continue beyond the barrier if
the area permits; otherwise it stops at the barrier just as any other spell effect does.

### Mythic Firestream

**Sources:** Mythic Adventures pg 94\
The damage dealt increases to 2d10 points of fire damage. Any creature that fails its saving throw
also catches fire. The continuous line of fire pushes against all creatures, making them treat the
spell's area as difficult terrain.

_Augmented (4th):_ If you expend two uses of mythic power, you create a second line of fire using
your other hand. If you overlap the lines, creatures in the overlap must attempt two saving throws
and take the lower result, but don't take damage from both lines. You may stop either line of fire
as a free action on your turn, but once you stop maintaining a line, you must cast mythic firestream
again to recreate it.
