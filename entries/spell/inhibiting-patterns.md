+++
id = "ref/spell/inhibiting-patterns"
kind = "spell"
title = "Inhibiting Patterns"
source_ids = ["distant-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inhibiting_patterns", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Pattern"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a sprikle of ground glass)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one cylinder (10-ft. radius, 40-ft. high)/3 levels" },
]
duration = "concentration+ 1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Skald\
4: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a sprikle of ground glass)
Range: medium (100 ft. + 10 ft./level)
Duration: concentration+ 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Effect: one cylinder (10-ft. radius, 40-ft. high)/3 levels
Subschool: Pattern
Descriptors: mind-affecting
:::

**Sources:** Distant Realms pg 42

You create one or more vibrant pillars of kaleidoscopic color that rise out from the ground. A
creature attempting to move through one of the pillars must attempt a Will save. Failure means the
creature can't move through the pillar and can't take any other actions for the duration of its turn
that round, but it can attempt to pass through the pillar again in subsequent rounds (attempting
another save against the effect). A creature need only succeed at one saving throw to move through
all pillars created by this spell.

A creature standing within the area of a pillar is dazzled (no save), while a creature making a
ranged attack that passes through one or more of the illusory pillars takes a 50% miss chance. A
creature can make a melee attack against a target within a pillar at no penalty.
