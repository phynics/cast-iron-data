+++
id = "ref/spell/hungry-pit"
kind = "spell"
title = "Hungry Pit"
aon = "SpellDisplay.aspx?ItemName=Hungry%20Pit"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hungry_pit", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-pit" },
]
[[sources]]
publication = "advanced-players-guide"
page = "228"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["creation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (miniature shovel costing 10 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft.-by-10-ft. hole, 10 ft. deep/2 levels" },
]
duration = "1 round + 1 round/level"
saving_throw = "Reflex negates, Reflex half, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F (miniature shovel costing 10 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round + 1 round/level
Saving throw: Reflex negates, Reflex half, see text
Spell resistance: no
Effect: 10-ft.-by-10-ft. hole, 10 ft. deep/2 levels
Subschool: creation
:::

### Hungry Pit

This spell functions as [create pit](ref/spell/create-pit), except that the pit has the ability to
squeeze and crush any creature trapped within it and has a maximum depth of 100 feet. Creatures who
fall into the hole take falling damage as normal. In addition, anyone within the pit, not just those
on the bottom, takes 4d6 points of bludgeoning damage each round as the pit contracts and then
returns to its normal size (a successful Reflex save halves this damage). The ever-shifting walls of
the pit are quite difficult to scale and have a Climb DC of 35.
