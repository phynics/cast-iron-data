+++
id = "ref/spell/tectonic-communion"
kind = "spell"
title = "Tectonic Communion"
aon = "SpellDisplay.aspx?ItemName=Tectonic%20Communion"
source_ids = ["core-rulebook", "ultimate-wilderness", "faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tectonic_communion", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/commune" },
]
[[sources]]
publication = "faiths-and-philosophies"
page = "29"

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

### Tectonic Communion

Tectonic communion functions as [commune](ref/spell/commune) with nature with an even greater range.
In outdoor or natural underground settings, the spell operates on a radius of 100 miles per caster
level, extending even underground without penalty.

For every 2 caster levels above 13th, you may glean an additional fact from the list presented in
commune with nature. Communities, dungeons, and signs of civilization (such as roads, farms or other
constructions and settlements) exist as dark and unknowable blots in your perception of the spell's
area; you're aware of their location and existence, but can't discern any information regarding
them.
