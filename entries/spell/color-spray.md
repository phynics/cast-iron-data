+++
id = "ref/spell/color-spray"
kind = "spell"
title = "Color Spray"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "color_spray", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "256"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Pattern"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (red, yellow, and blue powder or colored sand)"
range = "15 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bloodrager, Magus, Mesmerist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (red, yellow, and blue powder or colored sand)
Range: 15 ft.
Duration: instantaneous; see text
Saving throw: Will negates
Spell resistance: yes
Area: cone-shaped burst
Subschool: Pattern
Descriptors: mind-affecting
:::

A vivid cone of clashing colors springs forth from your hand, causing creatures to become stunned,
perhaps also blinded, and possibly knocking them unconscious. Each creature within the cone is
affected according to its HD.

_2 HD or less:_ The creature is unconscious, blinded, and stunned for 2d4 rounds, then blinded and
stunned for 1d4 rounds, and then stunned for 1 round. (Only living creatures are knocked
unconscious.)

_3 or 4 HD:_ The creature is blinded and stunned for 1d4 rounds, then stunned for 1 round.

_5 or more HD:_ The creature is stunned for 1 round.

Sightless creatures are not affected by color spray.
