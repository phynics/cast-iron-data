+++
id = "ref/spell/bane"
kind = "spell"
title = "Bane"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bane", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "50 ft."
effects = [
  { label = "Area", value = "50-ft.-radius burst, centered on you" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Antipaladin, Cleric, Inquisitor, Mesmerist, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 50 ft.
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Area: 50-ft.-radius burst, centered on you
Subschool: Compulsion
Descriptors: emotion, fear, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 246

Bane fills your enemies with fear and doubt. Each affected creature takes a -1 penalty on attack
rolls and a -1 penalty on saving throws against fear effects. Bane counters and dispels
[bless](ref/spell/bless).
