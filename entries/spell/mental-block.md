+++
id = "ref/spell/mental-block"
kind = "spell"
title = "Mental Block"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mental_block", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Mesmerist\
2: Bard, Psychic, Skald
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

**Sources:** Occult Adventures pg 176

You lock access to the target's procedural memories, preventing it from drawing upon its experience
and expertise. The target loses all skill ranks, spells known, spells prepared, and activated feats,
as well as its extraordinary, supernatural, and
[spell-like abilities](ref/umr/spell-like-abilities). Each round at the end of the target's turn,
the target can attempt another Will save to end this effect.
