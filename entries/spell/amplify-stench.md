+++
id = "ref/spell/amplify-stench"
kind = "spell"
title = "Amplify Stench"
aon = "SpellDisplay.aspx?ItemName=Amplify%20Stench"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "amplify_stench", path = "json/spells.json" },
]
[[sources]]
publication = "monster-codex"
page = "213"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Cleric, Druid, Hunter, Oracle, Psychic, Shaman, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: you
:::

You amplify your natural stench special ability-its save DC increases by 2, and creatures that fail
their saving throws against your stench become nauseated rather than sickened. If your stench
ability normally causes a creature to become nauseated (such as with the foul stench ability), the
radius of your stench doubles instead. This spell has no effect if you don't possess the stench
special ability.
