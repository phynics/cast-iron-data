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
  { class = "Inquisitor", level = 4 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a hard biscuit broken into pieces)"
range = "touch"
effects = [
  { label = "Target", value = "you plus one touched creature/3 levels" },
]
duration = "1 hour/level (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Ranger\
4: Inquisitor
Casting time: 1 standard action
Components: V, S, M (a hard biscuit broken into pieces)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: you plus one touched creature/3 levels
:::

### Tireless Pursuers

This spell functions as [tireless pursuit](ref/spell/tireless-pursuit), except as noted above.
