+++
id = "ref/spell/reveal-emotions"
kind = "spell"
title = "Reveal Emotions"
aon = "SpellDisplay.aspx?ItemName=Reveal%20Emotions"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reveal_emotions", path = "json/spells8.json" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "10"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Spiritualist", level = 4 },
]
casting_time = "1 minute"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "40-ft.-radius spread" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium\
4: Mesmerist, Occultist, Psychic, Spiritualist
Casting time: 1 minute
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: yes
Area: 40-ft.-radius spread
:::

You create an area that draws out a creature's emotion aura. Creatures within this area constantly
glow with colors that represent their current overall emotional state and continue to do so for 1d4
rounds after leaving the area. This glow is clearly visible to any creature that can see the
creature. Emotionless creatures or creatures unaffected by this spell glow with a dull purple hue
while within the area.
