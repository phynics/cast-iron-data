+++
id = "ref/spell/utter-contempt"
kind = "spell"
title = "Utter Contempt"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "utter_contempt", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["emotion"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (spittle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Antipaladin\
4: Bard, Mesmerist, Skald\
5: Psychic\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (spittle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: emotion
:::

**Sources:** Ultimate Magic pg 246

You fill the target's heart with malice for all other creatures. The target's attitude toward all
creatures other than itself worsens by two steps.
