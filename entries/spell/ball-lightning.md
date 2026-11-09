+++
id = "ref/spell/ball-lightning"
kind = "spell"
title = "Ball Lightning"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ball_lightning", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "204"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air", "electricity"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a small iron ring)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "two or more 5-ft.-diameter spheres" },
]
duration = "1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Bloodrager, Druid, Hunter, Magus, Occultist, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a small iron ring)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Reflex negates
Spell resistance: yes
Effect: two or more 5-ft.-diameter spheres
Descriptors: air, electricity
:::

You create two globes of lightning that fly in whichever direction you indicate. For every 4 caster
levels above 7th, you create an additional globe of lightning (3 globes at 11th, 4 globes at 15th,
to the maximum of 5 globes at 19th). These globes fly at a rate of 20 feet per round and have
perfect maneuverability. Wind does not affect a flying sphere's course.

If a globe enters a space with a creature, it stops moving for the round and deals 3d6 points of
electricity damage to that creature, though a successful Reflex save negates the damage. Creatures
wearing metal armor take a -4 penalty on this saving throw.

Each globe moves as long as you actively direct it (it's a move action for you to direct all the
spheres created by a single casting of this spell); otherwise they stay at rest. These globes have
no mass and cannot push aside unwilling creatures or move solid objects. A ball lightning globe
winks out if it exceeds the spell's range.
