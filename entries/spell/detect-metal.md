+++
id = "ref/spell/detect-metal"
kind = "spell"
title = "Detect Metal"
aon = "SpellDisplay.aspx?ItemName=Detect%20Metal"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_metal", path = "json/spells3.json" },
]
[[sources]]
publication = "people-of-the-river"
page = "26"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F (a magnetized nail or nugget of ore)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Bard, Investigator, Skald, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F (a magnetized nail or nugget of ore)
Range: 60 ft.
Duration: concentration, up to 1 minute/level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

You detect any metal objects or creatures within a 60-foot cone. You can specify all metal objects
or one or more specific types of metal (such as silver, cold iron, or a type of
[skymetal](ref/eq-material/skymetal)) when you cast this spell; in the case of the latter, you
detect only objects or creatures made of the specified metal.
