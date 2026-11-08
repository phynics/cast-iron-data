+++
id = "ref/spell/walk-the-plank"
kind = "spell"
title = "Walk the Plank"
source_ids = ["advanced-players-guide", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "walk_the_plank", path = "json/spells3.json" },
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

## Create Pit

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

### Hungry Pit

**Sources:** Advanced Player's Guide pg 228

This spell functions as create pit, except that the pit has the ability to squeeze and crush any
creature trapped within it and has a maximum depth of 100 feet. Creatures who fall into the hole
take falling damage as normal. In addition, anyone within the pit, not just those on the bottom,
takes 4d6 points of bludgeoning damage each round as the pit contracts and then returns to its
normal size (a successful Reflex save halves this damage). The ever-shifting walls of the pit are
quite difficult to scale and have a Climb DC of 35.

### Spiked Pit

**Sources:** Advanced Player's Guide pg 246

This spell functions as create pit, except that the pit is lined with wickedly sharp spikes along
its bottom and walls and has a maximum depth of 50 feet. Creatures who fall into the pit take
falling damage as normal, plus 2d6 points of piercing damage from the spikes. Any creature or object
coming into contact with the spikes along the walls, such as a creature trying to climb out, or rope
or other typical aids to climbing, takes 1d6 points of piercing damage each round they are in
contact with the walls. For those willing to accept the damage incurred while climbing, the pit's
walls have a Climb DC of 20.

### Walk the Plank

**Sources:** Villain Codex pg 188

This spell functions as per create pit, except as noted here. All but the top 10 feet of the hole is
filled with saltwater, reducing the fall damage for anyone falling into the pit to 1d3 points of
nonlethal damage and allowing Huge or larger creatures at the water's surface to simply pull
themselves out of the pit as part of a normal move action, without a Climb check. Additionally, the
pit contains a single advanced shark for every 4 caster levels you have (maximum four advanced
sharks). If desired, when you cast the spell, you can substitute two of the summoned sharks for one
great white shark. These sharks immediately attack any creature that falls into the pit, even you.
If multiple creatures fall in the pit, the sharks attack randomly. When the spell ends, creatures
inside the hole rise up with the bottom of the pit, as normal for create pit, but the conjured water
and sharks vanish.
