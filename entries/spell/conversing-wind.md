+++
id = "ref/spell/conversing-wind"
kind = "spell"
title = "Conversing Wind"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conversing_wind", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "1 mile/level"
effects = [
  { label = "Area", value = "10-ft.-radius spread" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 1 mile/level
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Area: 10-ft.-radius spread
Descriptors: air
:::

**Sources:** Ranged Tactics Toolbox pg 30

This spell functions as [whispering wind](ref/spell/whispering-wind), except it can carry responses
and doesn't end after delivering its first message. After the wind completes its initial message, it
waits for 1 round, then copies what it hear, and returns at the same speed and by the same route. It
delivers what it heard to the location where the spell was originally cast. The wind continues back
and forth in this way until the duration ends or the spell is dismissed.
