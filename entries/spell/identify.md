+++
id = "ref/spell/identify"
kind = "spell"
title = "Identify"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "identify", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (wine stirred with an owl's feather)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "3 rounds/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Bard, Investigator, Medium, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (wine stirred with an owl's feather)
Range: 60 ft.
Duration: 3 rounds/level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

**Sources:** PRPG Core Rulebook pg 299

This spell functions as [detect magic](ref/spell/detect-magic), except that it gives you a +10
enhancement bonus on Spellcraft checks made to identify the properties and command words of magic
items in your possession. This spell does not allow you to identify artifacts.
