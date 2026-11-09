+++
id = "ref/spell/thought-worm-1"
kind = "spell"
title = "Thought Worm I"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_worm_1", path = "json/spells10.json" },
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
  { class = "Psychic", level = 2 },
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
Level: 2: Psychic
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

You implant a minor suggestion within the target creature's psyche that makes it less inclined to
resist mental intrusion. The target creature takes a -2 penalty on Will saves against all
mind-affecting spells and effects for the duration of the spell.
