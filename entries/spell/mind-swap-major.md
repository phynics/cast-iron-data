+++
id = "ref/spell/mind-swap-major"
kind = "spell"
title = "Major Mind Swap"
aon = "SpellDisplay.aspx?ItemName=Mind%20Swap%2C%20Major"
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
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 9 },
]
casting_time = "1 minute"
components = "V, S, M (diamonds worth 10,000 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature of your same race" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 9: Psychic
Casting time: 1 minute
Components: V, S, M (diamonds worth 10,000 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one creature of your same race
Subschool: compulsion
Descriptors: mind-affecting
:::

### Major Mind Swap

The spell functions as [mind swap](ref/spell/mind-swap), except as noted above. In addition, after
24 hours, instead of using each other's hit points, you each revert to your original hit points,
modified by your new Constitution modifiers. This spell can be reversed only with miracle, wish, or
another major mind swap.
