+++
id = "ref/spell/heroic-fortune-mass"
kind = "spell"
title = "Mass Heroic Fortune"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heroic_fortune_mass", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/heroic-fortune" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (diamond dust worth 1,000 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Bard, Skald\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF, M (diamond dust worth 1,000 gp)
Range: close (25 ft. + 5 ft./2 levels)
Targets: one or more creatures, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: no
:::

### Mass Heroic Fortune

**Sources:** Advanced Player's Guide pg 324

This spell functions like [heroic fortune](ref/spell/heroic-fortune), except as noted above.
