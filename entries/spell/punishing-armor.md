+++
id = "ref/spell/punishing-armor"
kind = "spell"
title = "Punishing Armor"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "punishing_armor", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "Fortitude negates, see below"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Shaman, Sorcerer, Spiritualist, Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 10 minutes/level (D)
Saving throw: Fortitude negates, see below
Spell resistance: no
Target: you
:::

**Sources:** Agents of Evil pg 19

You coat yourself with a thin layer of shimmering energy. Any creature dealing nonlethal damage to
you immediately takes half the amount of nonlethal damage dealt. A successful Fortitude save made by
the attacking creature negates this damage.
