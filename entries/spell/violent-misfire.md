+++
id = "ref/spell/violent-misfire"
kind = "spell"
title = "Violent Misfire"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "violent_misfire", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a small piece of flint)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one early or advanced firearm" },
]
duration = "1 round/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a small piece of flint)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one early or advanced firearm
:::

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

This spell functions as violent misfire except as noted above.
