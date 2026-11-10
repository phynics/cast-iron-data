+++
id = "ref/spell/burdened-thoughts"
kind = "spell"
title = "Burdened Thoughts"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burdened_thoughts", path = "json/spells2.json" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "26"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a lead bearing wrapped in clay)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Druid, Hunter, Shaman, Witch\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a lead bearing wrapped in clay)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You fill a creature's mind with the realization of its earthly weight and responsibilities.
Disheartened and wearied by these thoughts, the creature gains heavy encumbrance and is unable to
fly (if already flying, it must land as soon as possible). If the creature is three or more size
categories larger than you, it's also staggered.
