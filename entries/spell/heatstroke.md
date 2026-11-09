+++
id = "ref/spell/heatstroke"
kind = "spell"
title = "Heatstroke"
source_ids = ["sargava-the-lost-colony"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heatstroke", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ray-of-exhaustion" },
]
[[sources]]
publication = "sargava-the-lost-colony"
page = "28"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of sweat)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "1 minute/level"
saving_throw = "Fortitude partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of sweat)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Fortitude partial, see text
Spell resistance: yes
Effect: ray
Descriptors: fire
:::

A wavering red ray projects from your finger. You must succeed on a ranged touch attack with the ray
to hit your target.

The ray inflicts 1d4 points of nonlethal damage, causing the target to suffer from heatstroke as its
body temperature dramatically increases. Except as noted above, this spell otherwise functions as
[ray of exhaustion](ref/spell/ray-of-exhaustion).

Characters wearing heavy clothing or armor of any sort take a -4 penalty on their saves.
