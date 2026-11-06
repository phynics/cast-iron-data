+++
id = "ref/spell/maze"
kind = "spell"
title = "Maze"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "maze", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Summoner\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: none
Spell resistance: yes
Target: one creature
Subschool: Teleportation
:::

**Sources:** PRPG Core Rulebook pg 312

You banish the subject into an extradimensional labyrinth. Each round on its turn, it may attempt a
DC 20 Intelligence check to escape the labyrinth as a full-round action. If the subject doesn't
escape, the maze disappears after 10 minutes, freeing the subject.

On escaping or leaving the maze, the subject reappears where it had been when the maze spell was
cast. If this location is filled with a solid object, the subject appears in the nearest open space.
Spells and abilities that move a creature within a plane, such as teleport and dimension door, do
not help a creature escape a maze spell, although a plane shift spell allows it to exit to whatever
plane is designated in that spell. Minotaurs are not affected by this spell.

### Mythic Maze

**Sources:** Mythic Adventures pg 100\
A spectral minotaur hunts the target trapped in the maze. Every round the creature fails to escape
from the maze, it takes 2d8 + your tier points of piercing and slashing damage from this phantom
opponent.
