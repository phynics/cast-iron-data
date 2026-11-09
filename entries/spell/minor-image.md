+++
id = "ref/spell/minor-image"
kind = "spell"
title = "Minor Image"
aon = "SpellDisplay.aspx?ItemName=Minor%20Image"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "minor_image", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/silent-image" },
]
[[sources]]
publication = "core-rulebook"
page = "314"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (a bit of fleece)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "visual figment that cannot extend beyond four 10 ft. cubes + one 10 ft. cube/level (S)" },
]
duration = "concentration+ 2 rounds"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Bard, Magus, Medium, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a bit of fleece)
Range: long (400 ft. + 40 ft./level)
Duration: concentration+ 2 rounds
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Effect: visual figment that cannot extend beyond four 10 ft. cubes + one 10 ft. cube/level (S)
Subschool: Figment
:::

This spell functions like [silent image](ref/spell/silent-image), except that minor image includes
some minor sounds but not understandable speech.
