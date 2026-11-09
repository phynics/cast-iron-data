+++
id = "ref/spell/ice-storm"
kind = "spell"
title = "Ice Storm"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ice_storm", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "298"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (dust and water)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "cylinder (20-ft. radius, 40 ft. high)" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Bloodrager, Druid, Hunter, Magus, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (dust and water)
Range: long (400 ft. + 40 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Area: cylinder (20-ft. radius, 40 ft. high)
Descriptors: cold
:::

Great magical hailstones pound down upon casting this spell, dealing 3d6 points of bludgeoning
damage and 2d6 points of cold damage to every creature in the area. This damage only occurs once,
when the spell is cast. For the remaining duration of the spell, heavy snow and sleet rains down in
the area. Creatures inside this area take a -4 penalty on Perception skill checks and the entire
area is treated as difficult terrain. At the end of the duration, the snow and hail disappear,
leaving no after-effects (other than the damage dealt).
