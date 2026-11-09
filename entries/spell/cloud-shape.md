+++
id = "ref/spell/cloud-shape"
kind = "spell"
title = "Cloud Shape"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloud_shape", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/gaseous-form" },
]
[[sources]]
publication = "advanced-race-guide"
page = "160"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S, M/DF (a bit of gauze and a wisp of smoke)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Druid, Hunter, Ranger, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: S, M/DF (a bit of gauze and a wisp of smoke)
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: air
:::

> _[Sylphs](ref/race/sylph) have access to the following spell._

This spell functions like [gaseous form](ref/spell/gaseous-form), except you assume the shape of a
Colossal cloud with a space of 30 feet. You choose the general appearance of the cloud (white,
stormy, fluffy, flat, and so on), after which your appearance cannot be changed. Even the closest
inspection cannot reveal that the cloud in question is actually a magically concealed creature. To
all normal tests you are, in fact, a cloud, although a detect magic spell reveals a moderate
transmutation aura on the cloud. Your fly speed in cloud form is 30 feet.
