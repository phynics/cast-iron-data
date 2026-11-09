+++
id = "ref/spell/crushing-despair"
kind = "spell"
title = "Crushing Despair"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crushing_despair", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "262"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Skald\
4: Arcanist, Bloodrager, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M
Range: 30 ft.
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Area: cone-shaped burst
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

An invisible cone of despair causes great sadness in the subjects. Each affected creature takes a -2
penalty on attack rolls, saving throws, ability checks, skill checks, and weapon damage rolls.

Crushing despair counters and dispels [good hope](ref/spell/good-hope).
