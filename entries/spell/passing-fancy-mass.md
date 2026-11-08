+++
id = "ref/spell/passing-fancy-mass"
kind = "spell"
title = "Mass Passing Fancy"
source_ids = ["spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "passing_fancy_mass", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/passing-fancy" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature/level, no two of which can be more thatn 30 ft. apart" },
]
duration = "4d4 rounds (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Mesmerist, Skald\
5: Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature/level, no two of which can be more thatn 30 ft. apart
Duration: 4d4 rounds (D)
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Mass Passing Fancy

**Sources:** Spymaster's Handbook pg 29

This spell functions as per [passing fancy](ref/spell/passing-fancy) except as noted above.
