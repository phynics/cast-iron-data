+++
id = "ref/spell/sundered-serpent-coil"
kind = "spell"
title = "Sundered Serpent Coil"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sundered_serpent_coil", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/black-tentacles" },
]
[[sources]]
publication = "monster-codex"
page = "200"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a snake scale)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "one 5-foot square" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Magus, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a snake scale)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: one 5-foot square
Subschool: Creation
:::

This spell functions like [black tentacles](ref/spell/black-tentacles), except it creates a Large
decapitated snake, which erupts from the ground and grapples a creature you specify within its
5-foot reach. As a standard action, you can command the snake to release its grappled target and
direct it to attack a different creature.
