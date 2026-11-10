+++
id = "ref/spell/burning-sands"
kind = "spell"
title = "Burning Sands"
aon = "SpellDisplay.aspx?ItemName=Burning%20Sands"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burning_sands", path = "json/spells2.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "16"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["earth", "fire"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a handful of sand)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft. radius" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Druid, Hunter, Ranger, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a handful of sand)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Area: 20-ft. radius
Subschool: Creation
Descriptors: earth, fire
:::

You cause sheets of hot sand to spread over the ground in the area of effect. This layer of sand is
1 foot deep and constantly shifts and churns, transforming the ground in the area into difficult
terrain. The sand itself burns, and periodic flames rise from the grit. While these flames cannot
ignite objects, they deal 1d4 points of fire damage to any creature that ends its turn in contact
with the ground within the area of effect. At the end of the duration, the sand vanishes, leaving no
after-effects (other than damage dealt).
