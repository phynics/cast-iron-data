+++
id = "ref/spell/blurred-movement"
kind = "spell"
title = "Blurred Movement"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blurred_movement", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/blur" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Alchemist, Arcanist, Bloodrager, Bard, Investigator, Magus, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Advanced Class Guide pg 176

This spell functions as [blur](ref/spell/blur), except that the blurring occurs only when you move
at least 10 feet on your turn and ceases at the end of your movement. It is therefore mainly used to
thwart attacks on your turn, such as attacks of opportunity. If you move at least twice your speed
on your turn, the blurring lasts until the start of your next turn.
