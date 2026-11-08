+++
id = "ref/spell/create-pit"
kind = "spell"
title = "Create Pit"
source_ids = ["advanced-players-guide", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_pit", path = "json/spells3.json" },
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

**Sources:** Advanced Player's Guide pg 213

You create a 10-foot-by-10-foot extradimensional hole with a depth of 10 feet per two caster levels
(maximum 30 feet). You must create the pit on a horizontal surface of sufficient size. Since it
extends into another dimension, the pit has no weight and does not otherwise displace the original
underlying material. You can create the pit in the deck of a ship as easily as in a dungeon floor or
the ground of a forest. Any creature standing in the area where you first conjured the pit must make
a Reflex saving throw to avoid falling into it. In addition, the edges of the pit are sloped, and
any creature ending its turn on a square adjacent to the pit must make a Reflex saving throw with a
+2 bonus to avoid falling into it. Creatures subjected to an effect intended to push them into the
pit (such as bull rush) do not get a saving throw to avoid falling in if they are affected by the
pushing effect.

Creatures who fall into the pit take falling damage as normal. The pit's coarse stone walls have a
Climb DC of 25. When the duration of the spell ends, creatures within the hole rise up with the
bottom of the pit until they are standing on the surface over the course of a single round.
