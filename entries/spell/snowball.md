+++
id = "ref/spell/snowball"
kind = "spell"
title = "Snowball"
source_ids = ["ultimate-wilderness", "people-of-the-north", "pathfinder-67-the-snows-of-summer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "snowball", path = "json/spells9.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "235"
[[sources]]
publication = "people-of-the-north"
page = "26"
[[sources]]
publication = "pathfinder-67-the-snows-of-summer"
page = "73"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold", "water"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one ball of ice and snow" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Bloodrager, Druid, Hunter, Magus, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Effect: one ball of ice and snow
Descriptors: cold, water
:::

You throw a ball of elemental ice and snow at a single target as a ranged touch attack. The snowball
deals 1d6 points of cold damage per caster level you have (maximum 5d6).
