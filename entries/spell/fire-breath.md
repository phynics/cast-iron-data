+++
id = "ref/spell/fire-breath"
kind = "spell"
title = "Fire Breath"
aon = "SpellDisplay.aspx?ItemName=Fire%20Breath"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fire_breath", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "221"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a chili pepper)"
range = "15 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "1 round/level or until discharged; see text"
saving_throw = "Reflex half, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a chili pepper)
Range: 15 ft.
Duration: 1 round/level or until discharged; see text
Saving throw: Reflex half, see text
Spell resistance: yes
Area: cone-shaped burst
Descriptors: fire
:::

Up to thrice during this spell's duration, you can belch forth a cone of fire as a standard action.
The first cone deals 4d6 points of fire damage to every creature in the area. The second cone of
flame deals 2d6 points of fire damage to every creature in the area. The third cone of flame deals
1d6 points of fire damage to every creature in the area. A successful Reflex save halves this
damage. After the third cone of flame, the spell ends.
