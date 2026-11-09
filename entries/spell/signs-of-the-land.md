+++
id = "ref/spell/signs-of-the-land"
kind = "spell"
title = "Signs of the Land"
source_ids = ["core-rulebook", "ultimate-wilderness", "faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "signs_of_the_land", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/commune" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "235"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 5 },
]
casting_time = "10 minutes"
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
School: divination
Level: 4: Hunter, Ranger\
5: Druid, Psychic, Shaman
Casting time: 10 minutes
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

### Signs of the Land

This spell functions as [commune](ref/spell/commune) with nature except it reveals up to three
details about the territory you currently occupy from the following list: bodies of water, features,
minerals, or plants. For each feature you learn about, you automatically know the skills you can use
to discover that feature and you gain 1d6 [Discovery Points](ref/rule/discovery-and-exploration)
toward finding it.
