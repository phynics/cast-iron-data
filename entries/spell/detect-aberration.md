+++
id = "ref/spell/detect-aberration"
kind = "spell"
title = "Detect Aberration"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_aberration", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-animals-or-plants" },
]
[[sources]]
publication = "advanced-players-guide"
page = "215"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 10 min./level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Druid, Hunter, Psychic, Ranger, Shaman
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: concentration, up to 10 min./level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

### Detect Aberration

This spell functions like _[detect animals or plants](ref/spell/detect-animals-or-plants),_ except
it detects creatures of the aberration type.
