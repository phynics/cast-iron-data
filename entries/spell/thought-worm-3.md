+++
id = "ref/spell/thought-worm-3"
kind = "spell"
title = "Thought Worm III"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_worm_3", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thought-worm-2" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 4 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial (see text)
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Psychic Anthology pg 11

This functions as per [thought worm II](ref/spell/thought-worm-2), except a target that succeeds at
its Will save still takes a -2 penalty on Will saves against your mind-affecting spells and effects
for the same duration. This spell can be undercast.
