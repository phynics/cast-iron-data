+++
id = "ref/spell/shadow-claws"
kind = "spell"
title = "Shadow Claws"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_claws", path = "json/spells15.json" },
]
[[sources]]
publication = "villain-codex"
page = "81"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Antipaladin\
2: Arcanist, Bloodrager, Bard, Magus, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Shadow
Descriptors: shadow
:::

You summon a pair of claws over your hands formed from semi-real material. This grants you two
primary claw attacks dealing 1d4 points of damage if you are Medium (1d3 if Small) plus 1 point of
Strength damage. A successful Fortitude saving throw negates the Strength damage (DC = this spell's
DC).
