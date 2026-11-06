+++
id = "ref/spell/animate-objects"
kind = "spell"
title = "Animate Objects"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animate_objects", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one Small object per caster level; see text" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Bard, Cleric, Occultist, Oracle, Psychic, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Targets: one Small object per caster level; see text
:::

**Sources:** PRPG Core Rulebook pg 242

You imbue inanimate objects with mobility and a semblance of life. Each such animated object then
immediately attacks whomever or whatever you initially designate.

An animated object can be of any nonmagical material. You may animate one Small or smaller object or
a corresponding number of larger objects as follows: A Medium object counts as two Small or smaller
objects, a Large object as four, a Huge object as eight, a Gargantuan object as 16, and a Colossal
object as 32. You can change the designated target or targets as a move action, as if directing an
active spell.

This spell cannot affect objects carried or worn by a creature.

Animate objects can be made permanent with a [permanency](ref/spell/permanency) spell.

### Mythic Animate Objects

**Sources:** Mythic Adventures pg 84\
Animated objects you create with this spell get the maximum number of hit points per level, gain a
+4 bonus to their Strength ability scores, and have 1-1/2 times the normal number of construction
points.
