+++
id = "ref/spell/aggressive-thundercloud-greater"
kind = "spell"
title = "Greater Aggressive Thundercloud"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aggressive_thundercloud_greater", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of a tree struck by lightning)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "5-ft.-diameter sphere" },
]
duration = "1 round/level"
saving_throw = "Reflex negates and Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Druid, Hunter, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of a tree struck by lightning)
Range: medium (100 ft. + 10 ft./level)
Effect: 5-ft.-diameter sphere
Duration: 1 round/level
Saving throw: Reflex negates and Fortitude negates (see text)
Spell resistance: yes
Descriptors: electricity
:::

## Aggressive Thundercloud

**Sources:** Advanced Class Guide pg 172

A crackling, spherical storm cloud flies in whichever direction you point and deals electricity
damage to those it strikes. It has a fly speed of 20 feet with perfect maneuverability. If it enters
a space that contains a creature, the storm stops moving for the round and deals 3d6 points of
electricity damage to that creature, though a successful Reflex save negates that damage. It
provides concealment (20% miss chance) to anything within it, and its flickering light illuminates
the same area a candle would.

The sphere moves as long as you actively direct it (as a move action for you); otherwise, it stays
at rest and crackles with lightning. It can be moved by wind effects and counts as a Small creature
for the purpose of determining how winds affect it. The sphere has no physical substance and cannot
exert any force on corporeal creatures or objects. It disperses if it exceeds the spell's range.

### Greater Aggressive Thundercloud

**Sources:** Advanced Class Guide pg 172

This spell functions as aggressive thundercloud, except it deals 6d6 points of electricity damage to
any creature it strikes. The first creature damaged by the cloud is also stunned for 1 round
(Fortitude negates); this is a sonic effect.
