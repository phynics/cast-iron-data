+++
id = "ref/spell/mind-thrust-5"
kind = "spell"
title = "Mind Thrust V"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_thrust_5", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mind-thrust-4" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

### Mind Thrust V

**Sources:** Occult Adventures pg 177

This functions as [mind thrust IV](ref/spell/mind-thrust-4), but the target is also exhausted for 1
round if it fails its save and fatigued for 1 round if it succeeds at its save. This spell can be
undercast.
