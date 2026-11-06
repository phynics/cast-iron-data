+++
id = "ref/spell/perceive-cues"
kind = "spell"
title = "Perceive Cues"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "perceive_cues", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of water)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Hunter, Inquisitor, Investigator, Mesmerist, Occultist, Psychic, Ranger, Witch
Casting time: 1 standard action
Components: V, S, M (a drop of water)
Range: personal
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Advanced Player's Guide pg 235

Your senses become preternaturally keen, and you gain insight into subtle behavioral cues. For the
duration of the spell, you receive a +5 competence bonus on Perception and Sense Motive checks.
