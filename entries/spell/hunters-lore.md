+++
id = "ref/spell/hunters-lore"
kind = "spell"
title = "Hunter's Lore"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunters_lore", path = "json/spells5.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "56"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a scrap of paper torn from a book about monsters)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Hunter, Inquisitor, Ranger
Casting time: 1 standard action
Components: V, S, M (a scrap of paper torn from a book about monsters)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

Inquisitors and rangers alike learned long ago that knowledge of an enemy grants power over that
enemy. This spell was created so that almost any enemy could have its vulnerabilities known and
exploited.

For the duration of this spell you may spend a full-round action to take 20 on any Knowledge skill
checks made to identify a foe's weaknesses, provided the foe in question is within line of sight and
provided that you have at least one rank in that particular Knowledge skill. This spell allows you
to make untrained Knowledge checks to determine a monster's weaknesses as if you had ranks in that
skill, but you cannot take 20 on these checks.
