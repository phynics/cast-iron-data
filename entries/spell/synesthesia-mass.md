+++
id = "ref/spell/synesthesia-mass"
kind = "spell"
title = "Mass Synesthesia"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "synesthesia_mass", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/synesthesia" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one or more living creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Mesmerist\
7: Psychic
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Targets: one or more living creatures, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Phantasm
Descriptors: mind-affecting
:::

### Mass Synesthesia

**Sources:** Occult Adventures pg 188

This spell functions like [synesthesia](ref/spell/synesthesia), except as noted above.
