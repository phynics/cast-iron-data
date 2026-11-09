+++
id = "ref/spell/envious-urge"
kind = "spell"
title = "Envious Urge"
aon = "SpellDisplay.aspx?ItemName=Envious%20Urge"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "envious_urge", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "218"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Mesmerist, Skald\
6: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You fill creatures with feelings of seething envy. Affected targets turn upon the nearest creature
(whether an ally or enemy) and attempt to disarm it of a valuable weapon, steal something it is
holding, or grapple it and strip it of something it prizes (your choice). Affected targets can
attempt a new Will save each round as a free action to end this effect.
