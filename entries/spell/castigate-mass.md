+++
id = "ref/spell/castigate-mass"
kind = "spell"
title = "Mass Castigate"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "castigate_mass", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "fear", "language-dependant", "mind-affecting"]
levels = [
  { class = "Inquisitor", level = 5 },
  { class = "Mesmerist", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level or 1 round; see text"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Inquisitor, Mesmerist
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level or 1 round; see text
Saving throw: Will partial
Spell resistance: yes
Subschool: Compulsion
Descriptors: emotion, fear, language-dependant, mind-affecting
:::

## Castigate

**Sources:** Advanced Player's Guide pg 210

You compel the target to beg for forgiveness. On a failed save, the target cowers with fear. On a
successful save, it is shaken for 1 round. Each round on its turn, a cowering subject may attempt a
new save to end the effect. A creature who worships the same god as you takes a -2 penalty on its
saving throw.

### Mass Castigate

**Sources:** Advanced Player's Guide pg 210

This spell functions as castigate, except it affects many creatures.
