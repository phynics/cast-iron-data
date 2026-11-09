+++
id = "ref/spell/detoxify"
kind = "spell"
title = "Detoxify"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detoxify", path = "json/spells3.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "115"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a dandelion stem)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Hunter, Ranger\
3: Cleric, Druid, Inquisitor, Oracle, Paladin, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M (a dandelion stem)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
:::

You remove a creature's ability to poison others, whether inherent or via poisoned weapons. Whenever
an affected creature would inflict poison with an attack, spell, or other method (including auras
and other constant methods), that poison is automatically neutralized. This does not grant the
subject of the spell any resistance to poison itself.
