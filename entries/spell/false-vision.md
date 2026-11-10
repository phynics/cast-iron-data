+++
id = "ref/spell/false-vision"
kind = "spell"
title = "False Vision"
aon = "SpellDisplay.aspx?ItemName=False%20Vision"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_vision", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "280"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (crushed jade worth 250 gp)"
range = "touch"
effects = [
  { label = "Area", value = "40-ft.-radius emanation" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium\
5: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (crushed jade worth 250 gp)
Range: touch
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Area: 40-ft.-radius emanation
Subschool: Glamer
Descriptors: glamer
:::

This spell creates a subtle illusion, causing any divination (scrying) spell used to view anything
within the area of this spell to instead receive a false image (as the
[major image](ref/spell/major-image) spell), as defined by you at the time of casting. As long as
the duration lasts, you can concentrate to change the image as desired. While you aren't
concentrating, the image remains static.
