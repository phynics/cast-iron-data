+++
id = "ref/spell/piercing-shriek"
kind = "spell"
title = "Piercing Shriek"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "piercing_shriek", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["pain", "sonic"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Bard, Psychic, Skald
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: pain, sonic
:::

**Sources:** Ultimate Magic pg 231

You emit an ear-splitting shriek which can be heard only by the target of this spell; all other
observers merely see you screaming silently. The target suffers wracking pain from the scream,
gaining the staggered condition. This spell has no effect on deaf creatures and cannot penetrate an
area of silence.
