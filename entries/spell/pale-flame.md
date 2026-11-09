+++
id = "ref/spell/pale-flame"
kind = "spell"
title = "Pale Flame"
source_ids = ["core-rulebook", "heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pale_flame", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/produce-flame" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "15"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "flame in your palm" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S
Range: 0 ft.
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: yes
Effect: flame in your palm
Descriptors: fire
:::

### Pale Flame

This spell functions as per [produce flame](ref/spell/produce-flame), except that the flames never
glow brighter than dim light, including any fires started by this spell. These flames cast light
only half the distance of a torch and cannot be seen from more than 100 feet away. The flames deal
2d6 points of fire damage + 1 point per caster level (maximum +5). Against plants, this damage
increases to 2d6 points + 2 points per caster level (maximum +10).
