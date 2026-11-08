+++
id = "ref/spell/acid-pit"
kind = "spell"
title = "Acid Pit"
source_ids = ["advanced-players-guide", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acid_pit", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-pit" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (miniature shovel costing 10 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft.-by-10-ft. hole, 10 ft. deep/2 levels" },
]
duration = "1 round + 1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F (miniature shovel costing 10 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round + 1 round/level
Saving throw: Reflex negates
Spell resistance: no
Effect: 10-ft.-by-10-ft. hole, 10 ft. deep/2 levels
Subschool: Creation
:::

### Acid Pit

**Sources:** Advanced Player's Guide pg 204

This spell functions as [create pit](ref/spell/create-pit), except that it places a 5-foot-deep pool
of acid at the bottom of the pit. The pit has a maximum depth of 100 feet. Creatures who fall into
the pit take falling damage as normal (the acid counts as a yielding surface), plus 2d6 points of
acid damage per round spent in contact with the acid. In addition, exposed items carried by a
creature in the pit may be harmed. Refer to [Table 9-2](ref/rule/saving-throw). Items are affected
one at a time in the order listed on the table, and must make Fortitude saves after 3 consecutive
rounds in the acid or gain the broken condition. Objects with the broken condition (regardless of
how they became broken) must make a Fortitude saving throw each round spent within the acid or be
destroyed. The walls of the pit are quite slippery and have a Climb DC of 30.
