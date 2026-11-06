+++
id = "ref/spell/calm-animals"
kind = "spell"
title = "Calm Animals"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calm_animals", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "animals within 30 ft. of each other" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Druid, Hunter, Psychic, Ranger, Shaman
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Targets: animals within 30 ft. of each other
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 252

This spell soothes and quiets animals, rendering them docile and harmless. Only ordinary animals
(those with Intelligence scores of 1 or 2) can be affected by this spell. All the subjects must be
of the same kind, and no two may be more than 30 feet apart. The maximum number of HD of animals you
can affect is equal to 2d4 + caster level.

The affected creatures remain where they are and do not attack or flee. They are not helpless and
defend themselves normally if attacked. Any threat breaks the spell on the threatened creatures.
