+++
id = "ref/spell/ray-of-enfeeblement"
kind = "spell"
title = "Ray of Enfeeblement"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ray_of_enfeeblement", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "1 round/level"
saving_throw = "Fortitude half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Bloodrager, Magus, Mesmerist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude half
Spell resistance: yes
Effect: ray
:::

**Sources:** PRPG Core Rulebook pg 329

A coruscating ray springs from your hand. You must succeed on a ranged touch attack to strike a
target. The subject takes a penalty to Strength equal to 1d6+1 per two caster levels (maximum
1d6+5). The subject's Strength score cannot drop below 1. A successful Fortitude save reduces this
penalty by half. This penalty does not stack with itself. Apply the highest penalty instead.
