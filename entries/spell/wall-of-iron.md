+++
id = "ref/spell/wall-of-iron"
kind = "spell"
title = "Wall of Iron"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_iron", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a small iron sheet plus gold dust worth 50 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "iron wall whose area is up to one 5-ft. square/level; see text" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Summoner\
6: Arcanist, Magus, Occultist, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a small iron sheet plus gold dust worth 50 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: see text
Spell resistance: no
Effect: iron wall whose area is up to one 5-ft. square/level; see text
Subschool: Creation
:::

**Sources:** PRPG Core Rulebook pg 367

You cause a flat, vertical iron wall to spring into being. The wall inserts itself into any
surrounding nonliving material if its area is sufficient to do so. The wall cannot be conjured so
that it occupies the same space as a creature or another object. It must always be a flat plane,
though you can shape its edges to fit the available space.

A wall of iron is 1 inch thick per four caster levels. You can double the wall's area by halving its
thickness. Each 5-foot square of the wall has 30 hit points per inch of thickness and
[hardness](ref/umr/hardness) 10. A section of wall whose hit points drop to 0 is breached. If a
creature tries to break through the wall with a single attack, the DC for the Strength check is 25 +
2 per inch of thickness.

If you desire, the wall can be created vertically resting on a flat surface but not attached to the
surface, so that it can be tipped over to fall on and crush creatures beneath it. The wall is 50%
likely to tip in either direction if left unpushed. Creatures can push the wall in one direction
rather than letting it fall randomly. A creature must make a DC 40 Strength check to push the wall
over. Creatures with room to flee the falling wall may do so by making successful Reflex saves. Any
Large or smaller creature that fails takes 10d6 points of damage while fleeing from the wall. The
wall cannot crush Huge and larger creatures.

Like any iron wall, this wall is subject to rust, perforation, and other natural phenomena. Iron
created by this spell is not suitable for use in the creation of other objects and cannot be sold.
