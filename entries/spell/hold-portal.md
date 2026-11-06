+++
id = "ref/spell/hold-portal"
kind = "spell"
title = "Hold Portal"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hold_portal", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one portal, up to 20 sq. ft./level" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Arcanist, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: one portal, up to 20 sq. ft./level
:::

**Sources:** PRPG Core Rulebook pg 297

This spell magically holds shut a door, gate, window, or shutter of wood, metal, or stone. The magic
affects the portal just as if it were securely closed and normally locked. A
[knock](ref/spell/knock) spell or a successful [dispel magic](ref/spell/dispel-magic) spell can
negate a hold portal spell.

Add 5 to the normal DC for forcing open a portal affected by this spell.

### Mythic Hold Portal

**Sources:** Mythic Adventures pg 98\
The target portal can be as large as 30 square feet per caster level. A creature attempting to force
open the portal must first succeed at a Will save against the spell's DC. This is a mind-affecting
effect. Failure means the creature can't open the door while the spell is in effect.
