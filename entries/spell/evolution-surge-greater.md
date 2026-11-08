+++
id = "ref/spell/evolution-surge-greater"
kind = "spell"
title = "Greater Evolution Surge"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "evolution_surge_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/evolution-surge-lesser" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a chameleon scale)"
range = "touch"
effects = [
  { label = "Target", value = "your eidolon" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, M (a chameleon scale)
Range: touch
Target: your eidolon
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
:::

### Greater Evolution Surge

**Sources:** Advanced Player's Guide pg 220

This spell functions as [lesser evolution surge](ref/spell/evolution-surge-lesser), except that you
can grant any two evolutions whose total cost does not exceed 6 evolution points.
