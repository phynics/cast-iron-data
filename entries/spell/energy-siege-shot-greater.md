+++
id = "ref/spell/energy-siege-shot-greater"
kind = "spell"
title = "Greater Energy Siege Shot"
aon = "SpellDisplay.aspx?ItemName=Energy%20Siege%20Shot%2C%20Greater"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "energy_siege_shot_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/energy-siege-shot" },
]
[[sources]]
publication = "ultimate-combat"
page = "229"

[fields]
kind = "spell"
school = "transmutation [variable]"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (a ball of pitch)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one siege engine of any size" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (harmless, object)"
spell_resistance = "yes (harmless/object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation \[variable\]
Level: 6: Arcanist, Occultist, Sorcerer, Summoner, Wizard
Casting time: 10 minutes
Components: V, S, M (a ball of pitch)
Range: close (25 ft. + 5 ft./2 levels)
Target: one siege engine of any size
Duration: 10 minutes/level
Saving throw: Fortitude negates (harmless, object)
Spell resistance: yes (harmless/object)
:::

### Greater Energy Siege Shot

This spell functions like [energy siege shot](ref/spell/energy-siege-shot), except it can target
siege engines of any size, not just Large siege engines.
