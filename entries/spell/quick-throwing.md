+++
id = "ref/spell/quick-throwing"
kind = "spell"
title = "Quick Throwing"
source_ids = ["pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "quick_throwing", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Antipaladin, Bloodrager, Hunter, Magus, Paladin, Ranger
Casting time: 1 standard action
Components: V, S, M
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: one creature/level, no two of which can be more than 30 ft. apart
:::

**Sources:** Pathfinder \#91: Battle of Bloodmarch Hills pg 71

Those under the effects of this spell become faster in the use of thrown weapons. They can draw
thrown weapons (including rocks if they have the rock throwing ability) on their bodies or within
their space without the need for the [Quick Draw](ref/feat/quick-draw) feat, allowing them to make
their full normal rate of attacks with such weapons. This has no effects on other forms of ranged
weapon ammunition.
