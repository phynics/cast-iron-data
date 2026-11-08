+++
id = "ref/spell/thought-worm-4"
kind = "spell"
title = "Thought Worm IV"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_worm_4", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thought-worm-3" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 5 },
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
Level: 5: Psychic
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

This functions as per [thought worm III](ref/spell/thought-worm-3), except that the penalty on Will
saves is -6 and a target that succeeds at its Will save still takes a -3 penalty on Will saves
against your mind-affecting spells and effects for the same duration. This spell can be undercast.
