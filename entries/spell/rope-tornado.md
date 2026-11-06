+++
id = "ref/spell/rope-tornado"
kind = "spell"
title = "Rope Tornado"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rope_tornado", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 4 },
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
components = "V, S, M (a length of twine)"
range = "120 ft."
effects = [
  { label = "Area", value = "120 ft. line" },
]
duration = "instantaneous"
saving_throw = "Reflex negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Druid, Hunter, Magus, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a length of twine)
Range: 120 ft.
Duration: instantaneous
Saving throw: Reflex negates
Spell resistance: yes
Area: 120 ft. line
Descriptors: air
:::

**Sources:** Wilderness Origins pg 27

A spiraling twister of tornado-force wind surges forth from your palm, unbalancing those it rushes
over. Creatures on the ground within the area are knocked prone. A flying creature within the
spell's area must instead succeed at a DC 25 Fly check or plummet to the ground, taking the
appropriate amount of falling damage. Creatures that are Huge or larger in size gain a +2 bonus on
their Reflex saves, while creatures that are Medium or smaller in size take a -2 penalty.

Additionally, the area is subjected to tornado-force winds, extinguishing all nonmagical flames,
dispersing clouds, and scattering unattended objects.
