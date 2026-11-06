+++
id = "ref/spell/detect-radiation"
kind = "spell"
title = "Detect Radiation"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_radiation", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "120 ft."
effects = [
  { label = "Area", value = "spherical emanation, centered on you" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Arcanist, Bard, Cleric, Druid, Hunter, Oracle, Ranger, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: 120 ft.
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Area: spherical emanation, centered on you
:::

**Sources:** Technology Guide pg 8

You detect radiation in the surrounding area. You see radioactive auras as a glowing green shimmer
in the air that emanates from radioactive objects; the brighter and more intense the green, the more
powerful the radioactivity. This glow does not provide illumination or allow you to see in darkness,
apart from being able to see the glow itself. The spell can penetrate barriers, but 3 feet of dirt
or wood, 1 foot of stone, 1 inch of common metal, or a thin sheet of lead blocks it - although
radiation can seep into such barriers, causing them to become radioactive (and thus visible to the
spell) in time.
