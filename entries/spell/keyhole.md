+++
id = "ref/spell/keyhole"
kind = "spell"
title = "Keyhole"
source_ids = ["pathfinder-143-borne-by-the-suns-grace"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "keyhole", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, DF"
range = "touch"
effects = [
  { label = "Target", value = "one touched door or portal" },
]
duration = "1 minute/level"
saving_throw = "special (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, DF
Range: touch
Duration: 1 minute/level
Saving throw: special (see text)
Spell resistance: no
Target: one touched door or portal
:::

**Sources:** Pathfinder \#143: Borne by the Sun's Grace pg 78

By touching a single door, gate, or other portal, you create a keyhole where none existed before or
double the size of an existing keyhole. A conjured keyhole allows you to peer through the door,
though the limited perspective imposes a -10 penalty on Perception checks to spot anything beyond.
It also allows a sealed door to be locked or picked if it could not be before. Locking or unlocking
such a door requires a successful Disable Device check with a DC equal to the barrier's break
DC + 10. Enlarging an existing keyhole allows viewers to peer through to whatever lies beyond, even
if the preexisting keyhole did not allow it, and it reduces the Disable Device DC to open or lock
the door by 5.

This spell does not normally allow a saving throw, but magic doors and barriers can resist the
effect with a successful Will saving throw, as if they were carried by their original creator.
