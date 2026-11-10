+++
id = "ref/spell/cone-of-cold"
kind = "spell"
title = "Cone of Cold"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cone_of_cold", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "258"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a small crystal or glass cone)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Magus, Occultist, Sorcerer, Wizard\
6: Shaman, Witch
Casting time: 1 standard action
Components: V, S, M (a small crystal or glass cone)
Range: 60 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: cone-shaped burst
Descriptors: cold
:::

Cone of cold creates an area of extreme cold, originating at your hand and extending outward in a
cone. It drains heat, dealing 1d6 points of cold damage per caster level (maximum 15d6).
