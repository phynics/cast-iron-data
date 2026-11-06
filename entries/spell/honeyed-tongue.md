+++
id = "ref/spell/honeyed-tongue"
kind = "spell"
title = "Honeyed Tongue"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "honeyed_tongue", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, M/DF (a drop of honey)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Paladin\
2: Bard, Inquisitor, Mesmerist, Skald
Casting time: 1 standard action
Components: V, M/DF (a drop of honey)
Range: personal
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Advanced Player's Guide pg 228

This spell augments your diplomacies. While under the effects of spell, you roll two dice each time
you make a Diplomacy check to change a creature's attitude, taking the highest roll. If this results
in a roll low enough to reduce the creature's attitude by a step, that creature gets some clue that
you are manipulating it with a spell. Alternatively you can cast this spell before making a
Diplomacy check to gather information, gaining a +5 competence bonus on the check.
