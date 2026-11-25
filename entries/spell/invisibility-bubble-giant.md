+++
id = "ref/spell/invisibility-bubble-giant"
kind = "spell"
title = "Giant Invisibility Bubble"
aon = "SpellDisplay.aspx?ItemName=Invisibility%20Bubble%2C%20Giant"
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
subschools = ["glamer"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (needle from a sea urchin)"
range = "touch"
effects = [
  { label = "Area", value = "10-ft.-radius emanation centered on the touched creature's space" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (needle from a sea urchin)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: 10-ft.-radius emanation centered on the touched creature's space
Subschool: glamer
:::

### Giant Invisibility Bubble

This functions as per [invisibility bubble](ref/spell/invisibility-bubble), but the bubble is
larger, which allows you to target a creature of up to size Gargantuan, or allows more creatures
into the bubble.
