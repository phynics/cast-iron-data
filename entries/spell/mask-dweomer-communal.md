+++
id = "ref/spell/mask-dweomer-communal"
kind = "spell"
title = "Communal Mask Dweomer"
source_ids = ["advanced-players-guide", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mask_dweomer_communal", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mask-dweomer" },
]
[[sources]]
publication = "ultimate-combat"
page = "236"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of gauze)"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "1 day/level (D)"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Occultist, Psychic, Witch
Casting time: 1 standard action
Components: V, S, M (a piece of gauze)
Range: touch
Duration: 1 day/level (D)
Saving throw: none, see text
Spell resistance: no
Target: creature or object touched
Subschool: Glamer
Descriptors: glamer
:::

### Communal Mask Dweomer

This spell functions like [mask dweomer](ref/spell/mask-dweomer), except you divide the duration in
1-day increments among the creatures or objects touched.
