+++
id = "ref/spell/burst-of-insight"
kind = "spell"
title = "Burst of Insight"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burst_of_insight", path = "json/spells2.json" },
]
[[sources]]
publication = "occult-adventures"
page = "160"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Spiritualist", level = 1 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Medium, Mesmerist, Psychic, Spiritualist
Casting time: 1 immediate action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

You plumb the depths of your mind for insight, leaving you momentarily frazzled. When you are about
to make a d20 roll based on Intelligence, Wisdom, or Charisma, you can cast this spell to gain a +8
enhancement bonus to Intelligence, Wisdom, or Charisma for that roll, but you are dazed for 1 round
afterward.
