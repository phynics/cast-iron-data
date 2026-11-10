+++
id = "ref/spell/goodberry"
kind = "spell"
title = "Goodberry"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "goodberry", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "291"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "2d4 fresh berries touched" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 day/level
Saving throw: none
Spell resistance: yes
Targets: 2d4 fresh berries touched
:::

Casting goodberry makes 2d4 freshly picked berries magical. You (as well as any other druid of 3rd
or higher level) can immediately discern which berries are affected. Each transmuted berry provides
nourishment as if it were a normal meal for a Medium creature. The berry also cures 1 point of
damage when eaten, subject to a maximum of 8 points of such curing in any 24-hour period.
