+++
id = "ref/spell/borrow-fortune"
kind = "spell"
title = "Borrow Fortune"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "borrow_fortune", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Medium, Oracle, Psychic
Casting time: 1 immediate action
Components: V
Range: personal
Duration: instantaneous; see text
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Advanced Player's Guide pg 206

When you make a d20 roll, you may choose to immediately cast this spell to reroll that die before
success or failure is known, keeping the more favorable result. For the next two rounds following
your casting of the spell, you must roll two dice each time a d20 roll is called for, keeping the
less favorable result.
