+++
id = "ref/spell/confusion-lesser"
kind = "spell"
title = "Lesser Confusion"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "confusion_lesser", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/confusion" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sahirafiyun", level = 1 },
  { class = "Skald", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Medium, Mesmerist, Psychic, Sahirafiyun, Skald
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Lesser Confusion

**Sources:** PRPG Core Rulebook pg 258

This spell causes a single creature to become confused for 1 round.
