+++
id = "ref/spell/thought-shield-2"
kind = "spell"
title = "Thought Shield II"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_shield_2", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thought-shield-1" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Psychic", level = 2 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Psychic
Casting time: 1 immediate action
Components: V
Range: personal
Duration: 1 round
Saving throw: none
Spell resistance: no
Target: you
:::

### Thought Shield II

**Sources:** Occult Adventures pg 189

This functions as [thought shield I](ref/spell/thought-shield-1), but the circumstance bonus on Will
saves to resist mind-affecting effects increases to +6. This spell can be undercast.
