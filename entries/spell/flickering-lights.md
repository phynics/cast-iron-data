+++
id = "ref/spell/flickering-lights"
kind = "spell"
title = "Flickering Lights"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flickering_lights", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness", "light"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 round"
components = "V, S, M (a patch of white cloth and a patch of black cloth)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "contiguous area consisting of one 10-foot cube/level (S)" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bard, Cleric, Inquisitor, Magus, Occultist, Oracle, Shaman, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 round
Components: V, S, M (a patch of white cloth and a patch of black cloth)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Area: contiguous area consisting of one 10-foot cube/level (S)
Descriptors: darkness, light
:::

**Sources:** Horror Adventures pg 118

You cause the illumination in the area to seem to flicker erratically, fluctuating between absolute
darkness and blinding brightness. The level of light in the area changes at the start of each
creature's turn, as determined by rolling a percentile die and consulting the following table.

|d%|Illumination Level|
| --- | --- |
|01-10|Supernatural darkness|
|11-25|Darkness|
|26-50|Dim light|
|51-90|Normal light|
|91-00|Bright light|

Even [darkvision](ref/rule/darkvision) can't see through supernatural darkness (as
[deeper darkness](ref/spell/deeper-darkness)). Bright light affects creatures with light blindness
or light sensitivity. For the purpose of superseding its effects with higher-level light or darkness
spells, flickering lights counts as a light spell when it increases the ambient light level and a
darkness spell when it decreases the ambient light level.
