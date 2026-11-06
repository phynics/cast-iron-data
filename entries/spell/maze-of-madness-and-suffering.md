+++
id = "ref/spell/maze-of-madness-and-suffering"
kind = "spell"
title = "Maze of Madness and Suffering"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "maze_of_madness_and_suffering", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
descriptors = ["evil", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M (an ornate puzzle box worth 1,000 gp and soaked in fresh blood)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "see text"
saving_throw = "Will partial, see below"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (an ornate puzzle box worth 1,000 gp and soaked in fresh blood)
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: Will partial, see below
Spell resistance: yes
Target: one creature
Subschool: Teleportation
Descriptors: evil, mind-affecting
:::

**Sources:** Horror Adventures pg 122

This spell works like maze, except the DC of the Intelligence check to escape is 22 and each round a
creature remains in the maze a different effect occurs depending on which section of the maze it is
in. Roll on the following table each time the creature attempts an Intelligence check to escape the
maze to see which part of the maze it wanders through; if a creature doesn't attempt an Intelligence
check, it stays in the same section and suffers that section's effects. Any conditions or damage
taken persist for the listed duration even if the creature exits the maze before then, but
conditions don't stack with themselves.

|d%|Maze Section|
| --- | --- |
|01-20|Circus|
|21-40|Haunted forest|
|41-60|Hellscape|
|61-80|Oasis of respite|
|81-100|Strange city|

_Circus:_ The creature finds itself in a nightmarish circus of giant beasts, garishly painted faces,
and hideous, mocking laughter. The creature must succeed at a Will save or gain a lesser
[madness](ref/rule/madness). The save uses the madness's normal DC.

_Haunted Forest:_ The creature travels through a dark forest of grasping trees while shadowy beasts
prowl at the edge of its vision. The creature must succeed at a Will save or become frightened for
2d4 rounds. This is a fear effect. A frightened creature can still attempt Intelligence checks to
escape the maze, but it takes 3d6 points of slashing and piercing damage from the trees' branches.

_Hellscape:_ The creature navigates a landscape of fire and stone walls carved with diabolical faces
while the cries of the damned echo in the air. The creature must succeed at a Will save or become
paralyzed by fear and potential torment for 1 round. This is a fear effect. The creature can't
attempt to escape the maze while paralyzed, and if it fails three consecutive saving throws against
this paralysis, the hellscape delivers a coup de grace, dealing the creature 4d6 points of fire
damage. The creature must succeed at a Fortitude save (DC = 10 + the damage dealt) or die. A
creature that survives the coup de grace escapes from the paralysis as well.

_Oasis of Respite:_ Whether it appears as a beautiful glade, a perfumed palace, or a literal desert
oasis, this section of the maze is supernaturally peaceful, especially in comparison to the rest of
the maze. The creature must succeed at a Will save or become fascinated for 1 round. The creature
can't attempt to escape the maze while fascinated. A creature that fails three consecutive saving
throws to this fascination enters a state of lethargy and gives up ever escaping the maze, remaining
in this area until the spell ends on its own in 10 minutes (as per maze).

_Strange City:_ The creature journeys through a city of cyclopean architecture under a sky of
indescribable color and numerous stars. The creature must succeed at a Will save or take 2d4 points
of Wisdom damage. If your campaign uses [the sanity system](ref/rule/sanity), the creature instead
takes 2d10 points of sanity damage.
