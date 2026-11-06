+++
id = "ref/spell/mind-swap"
kind = "spell"
title = "Mind Swap"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_swap", path = "json/spells14.json" },
]

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

**Sources:** Occult Adventures pg 176

This spell is similar to [possession](ref/spell/possession), except you switch minds with the
target, so instead of the target's soul sharing its body with yours and being unable to act, the
target's mind moves to your body and can control it as if you each had cast possession on the other.

### Major Mind Swap

**Sources:** Occult Adventures pg 176

The spell functions as mind swap, except as noted above. In addition, after 24 hours, instead of
using each other's hit points, you each revert to your original hit points, modified by your new
Constitution modifiers. This spell can be reversed only with miracle, wish, or another major mind
swap.
