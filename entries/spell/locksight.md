+++
id = "ref/spell/locksight"
kind = "spell"
title = "Locksight"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "locksight", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a small key)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Investigator, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a small key)
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

**Sources:** Heroes of the Streets pg 31

The target can observe for 1 full round a lock that he is aware of (or object that includes a lock,
such as a chest or door) that is within 60 feet to automatically determine whether it is open,
closed, or jammed. If the target creature is trained in Disable Device, by concentrating on a lock
for 3 rounds, he can also determine the quality of the lock (simple, average, good, or superior).
This spell does not enable the target to see hidden locks, such as those on secret doors.
