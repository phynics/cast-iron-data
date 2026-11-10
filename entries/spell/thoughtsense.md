+++
id = "ref/spell/thoughtsense"
kind = "spell"
title = "Thoughtsense"
aon = "SpellDisplay.aspx?ItemName=Thoughtsense"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thoughtsense", path = "json/spells10.json" },
]
[[sources]]
publication = "occult-adventures"
page = "190"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, M (a bit of dried brain tissue)"
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
School: divination
Level: 4: Medium, Mesmerist, Psychic, Spiritualist\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, M (a bit of dried brain tissue)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: mind-affecting
:::

You automatically detect and locate conscious creatures within 60 feet, as if you possessed the
[blindsight](ref/rule/blindsight-and-blindsense) ability. Nondetection, mind blank, and similar
effects can block this effect. Thoughtsense can distinguish between sentient (Intelligence 3 or
greater) and non-sentient (Intelligence 1-2) creatures, but otherwise provides no information about
the creatures it detects.
