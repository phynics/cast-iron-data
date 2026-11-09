+++
id = "ref/spell/aerial-tracks"
kind = "spell"
title = "Aerial Tracks"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aerial_tracks", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "203"

[fields]
kind = "spell"
school = "divination"
descriptors = ["air"]
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "circle centered on you, with a radius of 100 feet + 10 feet per level" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Hunter, Ranger\
4: Druid, Inquisitor, Shaman
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Area: circle centered on you, with a radius of 100 feet + 10 feet per level
Descriptors: air
:::

You cause the air in the area to ripple where creatures have flown through it up to 1 day ago per
caster level. These aerial ripples are tinged by glowing wisps, providing enough illumination to
follow the tracks without penalties due to poor lighting. The area moves with you, allowing you to
follow the tracks through the air over long distances provided you can fly or follow the route along
the ground within range to read the aerial tracks. Other creatures can also follow the trail as long
as they move with you. The base DC of Survival checks to track creatures through the air with this
spell is the same as tracking creatures across soft ground.
