+++
id = "ref/spell/echeans-excellent-enclosure"
kind = "spell"
title = "Echean's Excellent Enclosure"
source_ids = ["rival-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "echeans_excellent_enclosure", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M (a sphere of glass worth 100 gp and an iron nail, with which you pierce the glass on casting)"
range = "touch"
effects = [
  { label = "Area", value = "immobile 10-ft.-radius emanation" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 9: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a sphere of glass worth 100 gp and an iron nail, with which you pierce the glass on casting)
Range: touch
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: see text
Area: immobile 10-ft.-radius emanation
Descriptors: force
:::

**Sources:** Rival Guide pg 11

You call into being around you an invisible barrier of force within which magic cannot persist.
Within the area of the spell, effects are suppressed and creatures are affected as by antimagic
field. An immobile sphere of impenetrable force surrounds the field, equivalent in all ways to a
spherical wall of force, including its immunity to [dispel magic](ref/spell/dispel-magic) and
vulnerability to a [sphere of annihilation](ref/magic-artifact/sphere-of-annihilation) or
[rod of cancellation](ref/magic-rod/rod-of-cancellation). The barrier has
[hardness](ref/umr/hardness) 40 and 20 hit points per caster level, and can be damaged by both
mundane attacks and spells cast from outside the field. If the bubble of force is destroyed, the
spell's duration ends.

Spells cannot be cast within, into, or out of the enclosure, and teleportation effects that ignore a
wall of force (such as dimension door or teleport) are thwarted by the enclosure's field of
antimagic.

Echean's excellent enclosure has the same effect on summoned creatures of any type and incorporeal
undead that an antimagic field does, causing them to wink out of existence for the duration of
Echean's excellent enclosure unless their [spell resistance](ref/rule/spell-resistance), if any,
allows them to remain where they are within the field.
