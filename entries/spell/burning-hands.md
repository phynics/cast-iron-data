+++
id = "ref/spell/burning-hands"
kind = "spell"
title = "Burning Hands"
aon = "SpellDisplay.aspx?ItemName=Burning%20Hands"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burning_hands", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "251"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "15 ft."
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
Level: 1: Adept, Arcanist, Bloodrager, Magus, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 15 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: cone-shaped burst
Descriptors: fire
:::

A cone of searing flame shoots from your fingertips. Any creature in the area of the flames takes
1d4 points of fire damage per caster level (maximum 5d4). Flammable materials burn if the flames
touch them. A character can extinguish burning items as a full-round action.
