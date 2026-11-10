+++
id = "ref/spell/icy-prison-mass"
kind = "spell"
title = "Mass Icy Prison"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "icy_prison_mass", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/icy-prison" },
]
[[sources]]
publication = "ultimate-magic"
page = "224"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart." },
]
duration = "1 minute/level; see text"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target: one creature/level, no two of which can be more than 30 ft. apart.
Duration: 1 minute/level; see text
Saving throw: Reflex partial
Spell resistance: yes
Descriptors: cold
:::

### Mass Icy Prison

This spell functions as [icy prison](ref/spell/icy-prison), except as noted above.
