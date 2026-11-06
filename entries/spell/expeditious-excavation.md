+++
id = "ref/spell/expeditious-excavation"
kind = "spell"
title = "Expeditious Excavation"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "expeditious_excavation", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (tiny shovel)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "dirt in a 5-ft. cube" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Druid, Hunter, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (tiny shovel)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: see text
Spell resistance: no
Area: dirt in a 5-ft. cube
Descriptors: earth
:::

**Sources:** Advanced Player's Guide pg 220

You can excavate and move earth, dust, and sand up to the size of a 5-foot cube. If you are buried,
you may open a 5-foot cube around yourself, but the spell cannot be used for tunneling. Besides its
mundane applications, you can open a 5-foot-deep pit at a creature's feet. A Medium or smaller
creature falls prone in the pit unless it succeeds on a Reflex save. With a successful save, it can
choose to land harmlessly on its feet in the pit or hop to an adjacent square; this movement does
not provoke attacks of opportunity. A creature can escape a 5-foot-deep pit with a DC 5 Climb check.
Larger creatures may ignore pits smaller than their size.

The earth excavated by this spell is ordinarily distributed harmlessly across the spell's range, but
you may choose to throw up a burst of grit and debris when you dig a pit. This cloud of debris
provides [concealment](ref/rule/concealment) to any creatures in the square affected and all
adjacent squares for 1 round. Expeditious excavation has no effect on solid rock or earth creatures.
