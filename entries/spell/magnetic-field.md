+++
id = "ref/spell/magnetic-field"
kind = "spell"
title = "Magnetic Field"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magnetic_field", path = "json/spells6.json" },
]
[[sources]]
publication = "people-of-the-river"
page = "26"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Investigator", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius emanation" },
]
duration = "1 round/2 levels (D)"
saving_throw = "Reflex negates (object, see text)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Alchemist, Investigator, Magus, Summoner, Unchained Summoner\
7: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: 1 round/2 levels (D)
Saving throw: Reflex negates (object, see text)
Spell resistance: yes (object)
Area: 30-ft.-radius emanation
:::

You create a spherical magnetic field that surrounds you to a range of 30 feet and follows you for
the duration of the spell. Unattended metal objects in range - including weapons, armor, and
anything made primarily out of metal - are pulled violently toward you, stopping just short of your
space and falling harmlessly to the ground. Objects secured to a nonmetallic fixture remain where
they are unless a forceful tug would be enough to detach them. Loose objects weighing more than 500
pounds are not affected. If the magnetic field would cause a dangerous metal object such as a sword
or anvil to intersect a square occupied by a creature, that creature must succeed at a Reflex save
or take damage as if from an improvised weapon of the object's size (or smaller or larger, at the
GM's discretion).

A creature in the area wearing metal armor, wielding a metal weapon, or holding a metal object must
succeed at a Reflex save or be dragged 5 feet closer to you in a straight line, as if affected by
the [pull](ref/umr/pull) universal monster rule. A creature can drop a metal object it's holding as
a free action to avoid the effect if it's not wearing metal armor; a creature being dragged by its
shield can loosen it as a move action and drop it as a free action. Creatures made entirely or
mostly of metal take a -2 penalty on their Reflex saves. Creatures that fail their saves by 5 or
more are pulled an additional 5 feet closer for every increment of 5 by which they failed their
saves.
