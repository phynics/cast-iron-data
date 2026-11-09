+++
id = "ref/spell/invisibility-bubble-giant"
kind = "spell"
title = "Giant Invisibility Bubble"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_bubble_giant", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/invisibility-bubble" },
]
[[sources]]
publication = "aquatic-adventures"
page = "60"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (needle from a sea urchin)"
range = "touch"
effects = [
  { label = "Area", value = "touched creature's space, up to one 5-foot-cube" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Investigator, Magus, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (needle from a sea urchin)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: touched creature's space, up to one 5-foot-cube
Subschool: Glamer
Descriptors: glamer
:::

### Giant Invisibility Bubble

This functions as per [invisibility bubble](ref/spell/invisibility-bubble), but the bubble is
larger, which allows you to target a creature of up to size Gargantuan, or allows more creatures
into the bubble.
