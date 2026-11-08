+++
id = "ref/spell/violent-misfire-greater"
kind = "spell"
title = "Greater Violent Misfire"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "violent_misfire_greater", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/violent-misfire" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a small piece of flint)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one early or advanced firearm/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a small piece of flint)
Range: medium (100 ft. + 10 ft./level)
Target: one early or advanced firearm/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
:::

## Violent Misfire

**Sources:** People of the Wastes pg 29

This spell creates a chaotic charge within the black powder loaded in a target firearm. The next
time the target weapon fires during this spell's duration, it automatically misfires. If this
misfire causes the firearm to explode, the radius of the explosion is doubled and it deals maximum
damage to all creatures in the radius. The firearm's wielder also takes 1d6 additional points of
fire damage per 2 caster levels (maximum 10d6) you have.

If the target is an advanced firearm, and the firearm misfires a second time in a row while this
spell is in effect, it does not explode but still deals the additional damage to the wielder as
described.

### Greater Violent Misfire

**Sources:** People of the Wastes pg 29

This spell functions as [violent misfire](ref/spell/violent-misfire) except as noted above.
