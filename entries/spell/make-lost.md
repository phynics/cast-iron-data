+++
id = "ref/spell/make-lost"
kind = "spell"
title = "Make Lost"
source_ids = ["inner-sea-monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "make_lost", path = "json/spells6.json" },
]
[[sources]]
publication = "inner-sea-monster-codex"
page = "41"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 2 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Hunter, Ranger\
2: Bard, Druid, Skald
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

You strip the targets of their senses of direction and recent memories of travel. They immediately
forget the route they took in the last hour (but not details of encounters along the way) and become
lost.
