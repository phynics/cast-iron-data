+++
id = "ref/spell/debilitating-pain-mass"
kind = "spell"
title = "Mass Debilitating Pain"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "debilitating_pain_mass", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/debilitating-pain" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting", "pain"]
levels = [
  { class = "Psychic", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/4 levels" },
]
duration = "1 round/3 levels"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Psychic, Witch
Casting time: 1 standard action
Components: V, S, M
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/4 levels
Duration: 1 round/3 levels
Saving throw: Will partial (see text)
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting, pain
:::

### Mass Debilitating Pain

**Sources:** Psychic Anthology pg 10

This spell functions as per [debilitating pain](ref/spell/debilitating-pain), except you can target
one creature for every 4 caster levels you have.
