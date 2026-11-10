+++
id = "ref/spell/distracting-cacophony"
kind = "spell"
title = "Distracting Cacophony"
aon = "SpellDisplay.aspx?ItemName=Distracting%20Cacophony"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "distracting_cacophony", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "217"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft. spread" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Bard, Skald\
3: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Area: 20-ft. spread
Descriptors: sonic
:::

The air fills with loud and discordant noise, making concentration difficult. Casting a spell in
this area of cacophony requires a [concentration](ref/rule/concentration) check (DC 15 + the level
of the spell being cast). Any other concentration checks in the area have their DCs increased by 5.
The DC of Perception checks involving hearing is likewise increased by 5.
