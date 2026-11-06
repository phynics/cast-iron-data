+++
id = "ref/spell/enemy-insight"
kind = "spell"
title = "Enemy Insight"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enemy_insight", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "you plus one willing creature/3 levels, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Targets: you plus one willing creature/3 levels, no two of which can be more than 30 ft. apart
:::

**Sources:** Advanced Class Guide pg 181

You forge a mental bond between yourself and the other targets, each of which must have an
Intelligence score of 3 or higher. Choose one of your [favored enemy](ref/ability/favored-enemy)
types (such as goblinoids or magical beasts). You grant the targets half your favored enemy bonus
against that type of creature. If any target moves out of range, the spell ends for it.
