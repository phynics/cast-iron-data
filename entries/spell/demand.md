+++
id = "ref/spell/demand"
kind = "spell"
title = "Demand"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demand", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "10 minutes"
components = "V, S, M/DF (fine copper wire)"
range = "see text"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round; see text"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Mesmerist\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M/DF (fine copper wire)
Range: see text
Duration: 1 round; see text
Saving throw: Will partial
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 265

This spell functions like sending, but the message can also contain a suggestion (see the
[suggestion](ref/spell/suggestion) spell), which the subject does its best to carry out. A
successful Will save negates the suggestion effect but not the contact itself. The demand, if
received, is understood even if the subject's Intelligence score is as low as 1. If the message is
impossible or meaningless according to the circumstances that exist for the subject at the time the
demand is issued, the message is understood but the suggestion is ineffective.

The demand's message to the creature must be 25 words or less, including the suggestion. The
creature can also give a short reply immediately.
