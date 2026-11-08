+++
id = "ref/spell/tireless-pursuers"
kind = "spell"
title = "Tireless Pursuers"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tireless_pursuers", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/tireless-pursuit" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a hard biscuit)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Hunter, Inquisitor, Ranger
Casting time: 1 standard action
Components: V, S, M (a hard biscuit)
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

## Tireless Pursuit

**Sources:** Advanced Player's Guide pg 249

You harden your body against the stresses of long travel. You halve the damage caused by
[hustling and forced marching](ref/rule/overland-movement). In addition, for the duration of the
spell you ignore any fatigue caused by such travel. Once the spell ends, if you still have any
nonlethal damage caused by the hustling or forced march, you become fatigued, or exhausted if
already fatigued.

### Tireless Pursuers

**Sources:** Advanced Player's Guide pg 249

This spell functions as [tireless pursuit](ref/spell/tireless-pursuit), except as noted above.
