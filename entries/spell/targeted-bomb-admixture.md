+++
id = "ref/spell/targeted-bomb-admixture"
kind = "spell"
title = "Targeted Bomb Admixture"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "targeted_bomb_admixture", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "246"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Investigator", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Investigator
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

Upon drinking an extract created with this formula, you make a significant change to your magical
reserve that modifies the nature of all bombs you create and throw during this extract's duration.
This effect on your magical reserve has no effect on any discoveries that you use to modify your
bombs, but you can only have one admixture effect (formula with the word "bomb admixture" in its
title) active at a time. If you drink another bomb admixture, the effects of the former bomb
admixture end and the new one becomes active.

When you throw bombs, they can only hit a direct target; they do not splash. However, the bomb deals
its base damage plus double your Intelligence modifier instead of just its base damage plus your
Intelligence modifier.
