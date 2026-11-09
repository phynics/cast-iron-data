+++
id = "ref/spell/ray-of-exhaustion"
kind = "spell"
title = "Ray of Exhaustion"
source_ids = ["core-rulebook", "ultimate-magic", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ray_of_exhaustion", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "330"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of sweat)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "1 minute/level"
saving_throw = "Fortitude partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Bloodrager, Magus, Mesmerist, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of sweat)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Fortitude partial; see text
Spell resistance: yes
Effect: ray
:::

A black ray projects from your pointing finger. You must succeed on a ranged touch attack with the
ray to strike a target.

The subject is immediately exhausted for the spell's duration. A successful Fortitude save means the
creature is only fatigued.

A character that is already fatigued instead becomes exhausted.

This spell has no effect on a creature that is already exhausted. Unlike normal exhaustion or
fatigue, the effect ends as soon as the spell's duration expires.
