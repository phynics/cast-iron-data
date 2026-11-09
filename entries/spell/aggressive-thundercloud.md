+++
id = "ref/spell/aggressive-thundercloud"
kind = "spell"
title = "Aggressive Thundercloud"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aggressive_thundercloud", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "172"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of a tree struck by lightning)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "5-ft.-diameter sphere" },
]
duration = "1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Druid, Hunter, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of a tree struck by lightning)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Reflex negates
Spell resistance: yes
Effect: 5-ft.-diameter sphere
Descriptors: electricity
:::

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
