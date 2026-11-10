+++
id = "ref/spell/mind-maze"
kind = "spell"
title = "Mind Maze"
source_ids = ["inner-sea-monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_maze", path = "json/spells14.json" },
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
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a chicken skull)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Cleric, Oracle, Shaman, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a chicken skull)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell causes the target to act as though it's wandering through a maze. While under the effects
of the spell, the target can't make attacks or cast spells and must take at least one move action
each round to walk in a random direction determined using the guidelines for missed splash weapons.
The target must move at its maximum speed during this required movement, though additional move
actions after the first can cover shorter distances. If this movement takes the target into a
dangerous area, such as through a threatened square or off a ledge, the target receives a second
saving throw to end the effect before moving into peril. Walking into a harmless obstacle, such as a
wall, ends the target's movement.
