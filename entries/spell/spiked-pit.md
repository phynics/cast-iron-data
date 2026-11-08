+++
id = "ref/spell/spiked-pit"
kind = "spell"
title = "Spiked Pit"
source_ids = ["advanced-players-guide", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spiked_pit", path = "json/spells3.json" },
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

### Spiked Pit

**Sources:** Advanced Player's Guide pg 246

This spell functions as [create pit](ref/spell/create-pit), except that the pit is lined with
wickedly sharp spikes along its bottom and walls and has a maximum depth of 50 feet. Creatures who
fall into the pit take falling damage as normal, plus 2d6 points of piercing damage from the spikes.
Any creature or object coming into contact with the spikes along the walls, such as a creature
trying to climb out, or rope or other typical aids to climbing, takes 1d6 points of piercing damage
each round they are in contact with the walls. For those willing to accept the damage incurred while
climbing, the pit's walls have a Climb DC of 20.
