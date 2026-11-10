+++
id = "ref/spell/resonating-word"
kind = "spell"
title = "Resonating Word"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resonating_word", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "235"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "3 rounds"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Bard, Skald\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: 3 rounds
Saving throw: Fortitude partial
Spell resistance: yes
Target: one creature
Descriptors: sonic
:::

You speak a terrible word of power, setting up potentially lethal vibrations in the chosen target.
The target must save once each round on your turn, and the effects grow stronger for each saving
throw the creature fails.

On the first round, the target takes 5d6 points of sonic damage and is staggered for 1 round. A
successful save halves the damage and negates the staggered effect.

On the second round, the target takes 5d6 points of damage and is stunned for 1 round. A successful
save halves the damage and negates the stunning effect.

On the third round, the target takes 10d6 points of damage and is stunned for 1d4+1 rounds. A
successful save halves the damage and negates the stunning effect.

The resonating word has no power after the third round, even if the spell's duration is increased.
