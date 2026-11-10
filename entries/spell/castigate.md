+++
id = "ref/spell/castigate"
kind = "spell"
title = "Castigate"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "castigate", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "210"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "fear", "language-dependant", "mind-affecting"]
levels = [
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level or 1 round; see text"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Inquisitor, Mesmerist
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or 1 round; see text
Saving throw: Will partial
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: emotion, fear, language-dependant, mind-affecting
:::

You compel the target to beg for forgiveness. On a failed save, the target cowers with fear. On a
successful save, it is shaken for 1 round. Each round on its turn, a cowering subject may attempt a
new save to end the effect. A creature who worships the same god as you takes a -2 penalty on its
saving throw.
