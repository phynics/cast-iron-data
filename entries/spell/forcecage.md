+++
id = "ref/spell/forcecage"
kind = "spell"
title = "Forcecage"
aon = "SpellDisplay.aspx?ItemName=Forcecage"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forcecage", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "285"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (ruby dust worth 500 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "barred cage (20-ft. cube) or windowless cell (10-ft. cube)" },
]
duration = "1 round/level (D)"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (ruby dust worth 500 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Reflex negates
Spell resistance: no
Area: barred cage (20-ft. cube) or windowless cell (10-ft. cube)
Descriptors: force
:::

This spell creates an immobile, invisible cubical prison composed of either bars of force or solid
walls of force (your choice).

Creatures within the area are caught and contained unless they are too big to fit inside, in which
case the spell automatically fails. Teleportation and other forms of astral travel provide a means
of escape, but the force walls or bars extend into the Ethereal Plane, blocking ethereal travel.

Like a [wall of force](ref/spell/wall-of-force), a forcecage resists
[dispel magic](ref/spell/dispel-magic), although a [mage's disjunction](ref/spell/mages-disjunction)
still functions. The walls of a forcecage can be damaged by spells as normal, except for
[disintegrate](ref/spell/disintegrate), which automatically destroys it. The walls of a forcecage
can be damaged by weapons and supernatural abilities, but they have a [Hardness](ref/umr/hardness)
of 30 and a number of hit points equal to 20 per caster level. Contact with a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation) or
[rod of cancellation](ref/magic-rod/rod-of-cancellation) instantly destroys a forcecage.

_Barred Cage:_ This version of the spell produces a 20-foot cube made of bands of force (similar to
a wall of force spell) for bars. The bands are a half-inch wide, with half-inch gaps between them.
Any creature capable of passing through such a small space can escape; others are confined within
the barred cage. You can't attack a creature in a barred cage with a weapon unless the weapon can
fit between the gaps. Even against such weapons (including arrows and similar ranged attacks), a
creature in the barred cage has cover. All spells and breath weapons can pass through the gaps in
the bars.

_Windowless Cell:_ This version of the spell produces a 10-foot cube with no way in and no way out.
Solid walls of force form its six sides.
