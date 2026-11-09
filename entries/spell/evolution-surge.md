+++
id = "ref/spell/evolution-surge"
kind = "spell"
title = "Evolution Surge"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "evolution_surge", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/evolution-surge-lesser" },
]
[[sources]]
publication = "advanced-players-guide"
page = "220"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
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
Level: 2: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, M (a chameleon scale)
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: your eidolon
:::

### Evolution Surge

This spell functions as [lesser evolution surge](ref/spell/evolution-surge-lesser), except that you
can grant any evolution whose total cost does not exceed 4 evolution points.
