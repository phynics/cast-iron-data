+++
id = "ref/spell/mind-swap-major"
kind = "spell"
title = "Major Mind Swap"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_swap_major", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mind-swap" },
]
[[sources]]
publication = "occult-adventures"
page = "176"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 5 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 round"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Medium\
4: Occultist, Spiritualist\
5: Mesmerist, Psychic, Summoner\
6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Major Mind Swap

The spell functions as [mind swap](ref/spell/mind-swap), except as noted above. In addition, after
24 hours, instead of using each other's hit points, you each revert to your original hit points,
modified by your new Constitution modifiers. This spell can be reversed only with miracle, wish, or
another major mind swap.
