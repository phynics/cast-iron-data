+++
id = "ref/spell/tireless-pursuers"
kind = "spell"
title = "Tireless Pursuers"
aon = "SpellDisplay.aspx?ItemName=Tireless%20Pursuers"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tireless_pursuers", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/tireless-pursuit" },
]
[[sources]]
publication = "advanced-players-guide"
page = "249"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a hard biscuit)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Hunter, Inquisitor, Ranger
Casting time: 1 standard action
Components: V, S, M (a hard biscuit)
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

### Tireless Pursuers

This spell functions as [tireless pursuit](ref/spell/tireless-pursuit), except as noted above.
