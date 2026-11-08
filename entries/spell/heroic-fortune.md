+++
id = "ref/spell/heroic-fortune"
kind = "spell"
title = "Heroic Fortune"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heroic_fortune", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (diamond dust worth 100 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Bard, Cleric, Investigator, Oracle, Skald, Warpriest\
3: Paladin
Casting time: 1 standard action
Components: V, S, DF, M (diamond dust worth 100 gp)
Range: touch
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

**Sources:** Advanced Player's Guide pg 324

This spell grants 1 hero point to the target. This hero point must be spent before the duration
expires, or it is lost. The bonus hero point is spent before any other hero points the target might
possess.
