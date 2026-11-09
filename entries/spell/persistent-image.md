+++
id = "ref/spell/persistent-image"
kind = "spell"
title = "Persistent Image"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "persistent_image", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/silent-image" },
]
[[sources]]
publication = "core-rulebook"
page = "319"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a bit of fleece)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "visual figment that cannot extend beyond four 10-ft. cubes + one 10-ft. cube/level (S)" },
]
duration = "1 minute/level (D)"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium\
5: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a bit of fleece)
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level (D)
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Effect: visual figment that cannot extend beyond four 10-ft. cubes + one 10-ft. cube/level (S)
Subschool: Figment
:::

This spell functions like [silent image](ref/spell/silent-image), except that the figment includes
visual, auditory, olfactory, and thermal components, and the figment follows a script determined by
you. The figment follows that script without your having to concentrate on it. The illusion can
include intelligible speech if you wish.
