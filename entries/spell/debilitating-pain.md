+++
id = "ref/spell/debilitating-pain"
kind = "spell"
title = "Debilitating Pain"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "debilitating_pain", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting", "pain"]
levels = [
  { class = "Psychic", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/3 levels"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Psychic, Witch
Casting time: 1 standard action
Components: V, S, M
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/3 levels
Saving throw: Will partial (see text)
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting, pain
:::

**Sources:** Psychic Anthology pg 10

The target is overcome with intense pain, causing it to be stunned on a failed save or dazed for 1
round on a successful save.

### Mass Debilitating Pain

**Sources:** Psychic Anthology pg 10

This spell functions as per debilitating pain, except you can target one creature for every 4 caster
levels you have.
