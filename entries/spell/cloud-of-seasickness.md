+++
id = "ref/spell/cloud-of-seasickness"
kind = "spell"
title = "Cloud of Seasickness"
source_ids = ["pathfinder-55-the-wormwood-mutiny"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloud_of_seasickness", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/stinking-cloud" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of seaweed)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of seaweed)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates; see text
Spell resistance: no
Effect: cloud spreads in 20-ft. radius, 20 ft. high
Subschool: Creation
Descriptors: poison
:::

**Sources:** Pathfinder \#55: The Wormwood Mutiny pg 73

> _This spell is associated with [Besmara](ref/faith/besmara), but there are no restrictions on its
> use by others._

This spell functions like [stinking cloud](ref/spell/stinking-cloud), except as noted above and that
the vapors make creatures sickened instead of nauseated.

Cloud of seasickness can be made permanent with a [permanency](ref/spell/permanency) spell
(requiring a 9th-level caster and costing 2,500 gp). A permanent cloud of seasickness dispersed by
wind reforms in 10 minutes.
