+++
id = "ref/spell/tectonic-communion"
kind = "spell"
title = "Tectonic Communion"
source_ids = ["core-rulebook", "ultimate-wilderness", "faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tectonic_communion", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/commune" },
]

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

## Commune with Nature

**Sources:** PRPG Core Rulebook pg 258

You become one with nature, attaining knowledge of the surrounding territory. You instantly gain
knowledge of as many as three facts from among the following subjects: the ground or terrain,
plants, minerals, bodies of water, people, general animal population, presence of woodland
creatures, presence of powerful unnatural creatures, or even the general state of the natural
setting.

In outdoor settings, the spell operates in a radius of 1 mile per caster level. In natural
underground settings - caves, caverns, and the like - the spell is less powerful, and its radius is
limited to 100 feet per caster level. The spell does not function where nature has been replaced by
construction or settlement, such as in dungeons and towns.

### Signs of the Land

**Sources:** Ultimate Wilderness pg 235

This spell functions as [commune](ref/spell/commune) with nature except it reveals up to three
details about the territory you currently occupy from the following list: bodies of water, features,
minerals, or plants. For each feature you learn about, you automatically know the skills you can use
to discover that feature and you gain 1d6 [Discovery Points](ref/rule/discovery-and-exploration)
toward finding it.

### Tectonic Communion

**Sources:** Faiths and Philosophies pg 29

Tectonic communion functions as commune with nature with an even greater range. In outdoor or
natural underground settings, the spell operates on a radius of 100 miles per caster level,
extending even underground without penalty.

For every 2 caster levels above 13th, you may glean an additional fact from the list presented in
commune with nature. Communities, dungeons, and signs of civilization (such as roads, farms or other
constructions and settlements) exist as dark and unknowable blots in your perception of the spell's
area; you're aware of their location and existence, but can't discern any information regarding
them.
