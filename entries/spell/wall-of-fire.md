+++
id = "ref/spell/wall-of-fire"
kind = "spell"
title = "Wall of Fire"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_fire", path = "json/spells11.json" },
]
[[sources]]
publication = "core-rulebook"
page = "365"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Adept", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of phosphor)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "opaque sheet of flame up to 20 ft. long/level or a ring of fire with a radius of up to 5 ft./two levels; either form 20 ft. high" },
]
duration = "concentration+ 1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Summoner\
4: Adept, Arcanist, Bloodrager, Magus, Occultist, Sorcerer, Unchained Summoner, Wizard\
5: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, M/DF (a piece of phosphor)
Range: medium (100 ft. + 10 ft./level)
Duration: concentration+ 1 round/level
Saving throw: none
Spell resistance: yes
Effect: opaque sheet of flame up to 20 ft. long/level or a ring of fire with a radius of up to 5 ft./two levels; either form 20 ft. high
Descriptors: fire
:::

An immobile, blazing curtain of shimmering violet fire springs into existence. One side of the wall,
selected by you, sends forth waves of heat, dealing 2d4 points of fire damage to creatures within 10
feet and 1d4 points of fire damage to those past 10 feet but within 20 feet. The wall deals this
damage when it appears, and to all creatures in the area on your turn each round. In addition, the
wall deals 2d6 points of fire damage + 1 point of fire damage per caster level (maximum +20) to any
creature passing through it. The wall deals double damage to undead creatures.

If you evoke the wall so that it appears where creatures are, each creature takes damage as if
passing through the wall. If any 5-foot length of wall takes 20 points or more of cold damage in 1
round, that length goes away. (Do not divide cold damage by 2, as normal for objects.)

Wall of fire can be made permanent with a [permanency](ref/spell/permanency) spell. A permanent wall
of fire that is extinguished by cold damage becomes inactive for 10 minutes, then reforms at normal
strength.
