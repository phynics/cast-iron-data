+++
id = "ref/spell/stage-fright"
kind = "spell"
title = "Stage Fright"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stage_fright", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "1 creature/level, no two of which may be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Antipaladin, Arcanist, Bard, Inquisitor, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: 1 creature/level, no two of which may be more than 30 ft. apart
Subschool: Compulsion
Descriptors: emotion, fear, mind-affecting
:::

**Sources:** Arcane Anthology pg 27

You fill your targets with the sudden fear of failure. A creature that fails its saving throw takes
a -4 penalty on ability checks, skill checks, and any checks that require concentration (such as
casting a spell in difficult circumstances or operating a complex device).
