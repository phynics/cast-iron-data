+++
id = "ref/spell/displacement"
kind = "spell"
title = "Displacement"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "displacement", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, M (a small loop of leather)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Alchemist, Arcanist, Bard, Investigator, Magus, Medium, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, M (a small loop of leather)
Range: touch
Duration: 1 round/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** PRPG Core Rulebook pg 273

The subject of this spell appears to be about 2 feet away from its true location. The creature
benefits from a 50% miss chance as if it had [total concealment](ref/rule/concealment). Unlike
actual total concealment, displacement does not prevent enemies from targeting the creature
normally. True seeing reveals its true location and negates the miss chance.
