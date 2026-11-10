+++
id = "ref/spell/fear"
kind = "spell"
title = "Fear"
aon = "SpellDisplay.aspx?ItemName=Fear"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fear", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "252"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (the heart of a hen or a white feather)"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "1 round/level or 1 round; see text"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Bard, Mesmerist, Skald\
4: Antipaladin, Arcanist, Bloodrager, Inquisitor, Medium, Occultist, Psychic, Shaman, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (the heart of a hen or a white feather)
Range: 30 ft.
Duration: 1 round/level or 1 round; see text
Saving throw: Will partial
Spell resistance: yes
Area: cone-shaped burst
Descriptors: emotion, fear, mind-affecting
:::

An invisible cone of terror causes each living creature in the area to become
[panicked](ref/misc/panicked) unless it succeeds on a Will save. If cornered, a panicked creature
begins [cowering](ref/misc/cowering). If the Will save succeeds, the creature is
[shaken](ref/misc/shaken) for 1 round.
