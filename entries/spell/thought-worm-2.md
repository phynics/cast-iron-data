+++
id = "ref/spell/thought-worm-2"
kind = "spell"
title = "Thought Worm II"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_worm_2", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thought-worm-1" },
]
[[sources]]
publication = "psychic-anthology"
page = "11"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell functions as per [thought worm I](ref/spell/thought-worm-1), but the penalty on Will
saves is -4. This spell can be undercast.
