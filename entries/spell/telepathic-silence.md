+++
id = "ref/spell/telepathic-silence"
kind = "spell"
title = "Telepathic Silence"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telepathic_silence", path = "json/spells10.json" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "31"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Spiritualist", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "60-ft.-radius emanation centered on a point in space" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium, Mesmerist, Occultist, Psychic, Spiritualist
Casting time: 1 round
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: 60-ft.-radius emanation centered on a point in space
Subschool: Glamer
Descriptors: glamer
:::

Creatures within the area cannot send or receive telepathic messages, and anyone in the area casting
a spell with a thought component must succeed at a [concentration](ref/rule/concentration) check (DC
= 20 + twice the spell's level; this includes the increased concentration DC for casting spells with
a thought component) or lose the spell. Furthermore, the thoughts of creatures within the area
cannot be detected, located, or read with thoughtsense, detect thoughts, or similar effects.
Telepathic silence does not hinder spells that target a creature's mind or that do not rely on
communication, such as mind thrust.
