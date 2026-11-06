+++
id = "ref/spell/steady-saddle"
kind = "spell"
title = "Steady Saddle"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steady_saddle", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "saddle touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Antipaladin, Druid, Hunter, Paladin, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: saddle touched
:::

**Sources:** Villain Codex pg 177

A saddle affected by this spell becomes more comfortable to sit in, and the magic stabilizes any
shaking motion caused by riding at a high speed. For the duration of the spell, the penalty to use
ranged weapons while mounted in the target saddle decreases by 2. This stacks with the benefit of
the [Mounted Archery](ref/feat/mounted-archery) feat and similar effects. Furthermore, the DC for
any [concentration](ref/rule/concentration) check required as a result of the mount's movement
decreases by 2.
