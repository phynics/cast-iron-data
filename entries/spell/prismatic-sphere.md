+++
id = "ref/spell/prismatic-sphere"
kind = "spell"
title = "Prismatic Sphere"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prismatic_sphere", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/prismatic-wall" },
]
[[sources]]
publication = "core-rulebook"
page = "325"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V"
range = "10 ft."
effects = [
  { label = "Effect", value = "10-ft.-radius sphere centered on you" },
]
duration = "10 minutes/level (D)"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 9: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: 10 ft.
Duration: 10 minutes/level (D)
Saving throw: see text
Spell resistance: see text
Effect: 10-ft.-radius sphere centered on you
:::

This spell functions like [prismatic wall](ref/spell/prismatic-wall), except you conjure up an
immobile, opaque globe of shimmering, multicolored light that surrounds you and protects you from
all forms of attack. The sphere flashes in all colors of the visible spectrum.

The sphere's blindness effect on creatures with less than 8 HD lasts 2d4 × 10 minutes.

You can pass into and out of the prismatic sphere and remain near it without harm. When you're
inside it, however, the sphere blocks any attempt to project something through the sphere (including
spells). Other creatures that attempt to attack you or pass through suffer the effects of each
color, one at a time.

Typically, only the upper hemisphere of the globe exists, since you are at the center of the sphere,
so the lower half is usually occluded by the floor surface you are standing on.

The colors of the sphere have the same effects as the colors of a prismatic wall.

Prismatic sphere can be made permanent with a [permanency](ref/spell/permanency) spell.
