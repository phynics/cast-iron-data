+++
id = "ref/spell/intensify-psyche"
kind = "spell"
title = "Intensify Psyche"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "intensify_psyche", path = "json/spells14.json" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "20"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Mesmerist, Skald\
2: Arcanist, Cleric, Medium, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Effect: one creature
Descriptors: emotion, mind-affecting
:::

A sense of euphoria suffuses the target, amplifying all sensations, good or bad. The target creature
gains a +2 competence bonus on Diplomacy, Handle Animal, Perform, and Sense Motive checks. In
addition, the DC for any spells or effects with the emotion or pain descriptors cast or caused by
the target increases by 1 while the target is under the effects of the spell. However, increased
sensitivity causes the target to take a -2 penalty on saving throws against spells and effects with
the emotion or pain descriptor.
