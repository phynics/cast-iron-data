+++
id = "ref/spell/major-image"
kind = "spell"
title = "Major Image"
aon = "SpellDisplay.aspx?ItemName=Major%20Image"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "major_image", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/silent-image" },
]
[[sources]]
publication = "core-rulebook"
page = "311"

[fields]
kind = "spell"
school = "illusion"
subschools = ["figment"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F (a bit of fleece)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "visual figment that cannot extend beyond four 10 ft. cubes + one 10 ft. cube/level (S)" },
]
duration = "concentration+ 3 rounds"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Magus, Medium, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a bit of fleece)
Range: long (400 ft. + 40 ft./level)
Duration: concentration+ 3 rounds
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Effect: visual figment that cannot extend beyond four 10 ft. cubes + one 10 ft. cube/level (S)
Subschool: figment
:::

### Major Image

This spell functions like [silent image](ref/spell/silent-image), except that sound, smell, and
thermal illusions are included in the spell effect. While concentrating, you can move the image
within the range.

The image disappears when struck by an opponent unless you cause the illusion to react
appropriately.
