+++
id = "ref/spell/winter-grasp"
kind = "spell"
title = "Winter Grasp"
aon = "SpellDisplay.aspx?ItemName=Winter%20Grasp"
source_ids = ["ultimate-wilderness", "people-of-the-north"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "winter_grasp", path = "json/spells16.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "237"
[[sources]]
publication = "people-of-the-north"
page = "26"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["cold", "water"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (ground glass)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius spread" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Druid, Hunter, Shaman, Witch
Casting time: 1 standard action
Components: V, S, M/DF (ground glass)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Area: 20-ft.-radius spread
Subschool: Creation
Descriptors: cold, water
:::

Ice encrusts the ground, radiating supernatural cold and making it hard for creatures to maintain
their balance. This icy ground is treated as normal ice, forcing creatures to spend 2 squares of
movement to enter an icy square and increasing the DC of Acrobatics checks in the area by 5. A
creature that begins its turn in the affected area takes 1d6 points of cold damage and takes a -2
penalty on saving throws against spells with the cold descriptor for 1 round.
