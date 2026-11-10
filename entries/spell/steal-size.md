+++
id = "ref/spell/steal-size"
kind = "spell"
title = "Steal Size"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steal_size", path = "json/spells9.json" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "27"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of iron shaped like a scale tray)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one humanoid creature larger than you" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bloodrager, Sorcerer, Witch, Wizard\
3: Druid, Hunter, Magus
Casting time: 1 standard action
Components: V, S, M (a piece of iron shaped like a scale tray)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Targets: one humanoid creature larger than you
:::

This spell reduces the target's size by one size category, as if it were affected by reduce person.
You grow in size by one category, as if affected by enlarge person (if you can be targeted by that
spell). If the spell is dispelled or otherwise ends for either you or the target, both you and the
target return to your normal sizes.
