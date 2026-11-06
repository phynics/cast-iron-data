+++
id = "ref/spell/submerge-ship"
kind = "spell"
title = "Submerge Ship"
source_ids = ["pathfinder-56-raiders-of-the-fever-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "submerge_ship", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 minute"
components = "V, S, M/DF (a glass marble or piece of soap)"
range = "touch"
effects = [
  { label = "Target", value = "1 sailing vessel" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S, M/DF (a glass marble or piece of soap)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: 1 sailing vessel
:::

**Sources:** Pathfinder \#56: Raiders of the Fever Sea pg 70

When this spell is cast upon a vessel, the ship is surrounded by a protective bubble of constantly
replenishing, breathable air and sinks beneath the waves. For the duration of the spell, the ship
can travel beneath the water as easily as it did above. While under the effects of this spell, the
ship has magical propulsion that gives it a maximum speed of 120 feet and an acceleration of 30 feet
(see [ship-to-ship combat](ref/rule/ship-to-ship-combat) for details). The ship's pilot uses the
normal sailing skill to control the ship while under this spell's effects, and can command it to
dive and ascend as part of the vessel's normal movement. Despite the magical propulsion, the ship
still requires its crew to perform its normal functions.

The spell protects the ship and all aboard from the dangers of drowning and pressure, but not from
damage from outside obstacles or creatures. The bubble cannot be used offensively and prevents an
affected ship from rising into a space that won't accommodate it (like a sea cave too small to
contain it or under another vessel). Creatures can enter or leave the bubble at will, but those
outside the sphere cannot be forced inside against their will, the sphere proving substantial enough
that such creatures may choose whether to enter or to slip away along its sides. At the end of the
spell's duration the bubble pops, causing a ship still underwater at that time to gain the sinking
condition. This spell has no effect if cast upon a ship in water that cannot cover the vessel
entirely.

Although largely beneficial, this spell can be cast on a ship whose pilot does not want to submerge
her vessel. The ship itself uses its Will saving throw to resist this effect.
