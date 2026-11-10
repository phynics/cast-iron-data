+++
id = "ref/spell/solidify-earth"
kind = "spell"
title = "Solidify Earth"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "solidify_earth", path = "json/spells9.json" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "31"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "up to two 10-foot cubes per level (S)" },
]
duration = "1 minute/level"
saving_throw = "Reflex negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Cleric, Druid, Hunter, Oracle, Shaman, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Reflex negates (see text)
Spell resistance: no
Area: up to two 10-foot cubes per level (S)
Descriptors: earth
:::

Stone, dirt, and other types of earth within the area become more tightly packed. Burrowing creature
(including those using earth glide) treat the area as difficult terrain. Any creature that begins
its turn burrowing in the affected area becomes entangled for 1 round (Reflex negates).
[Tremorsense](ref/umr/tremorsense) and similar senses are ineffective within the affected area.
Creatures with the earth mastery special ability (such as earth elementals) double their bonus on
attack and damage rolls so long as both they and their targets are touching the area affected by
this spell.
