+++
id = "ref/spell/qualm"
kind = "spell"
title = "Qualm"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "qualm", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "241"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level or until discharged"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bard, Inquisitor, Medium, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level or until discharged
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

The target is suddenly beset with unexplainable doubts about the effectiveness of its actions and
the righteousness of its cause. The creature takes a -10 penalty on its ability checks, skill
checks, and [concentration](ref/rule/concentration) checks, until the duration ends, or until it
spends its entire turn doing absolutely nothing (it spends a full-round action gaining focus).
Spending an entire turn doing nothing discharges the spell.
