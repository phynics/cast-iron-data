+++
id = "ref/spell/entropic-shield"
kind = "spell"
title = "Entropic Shield"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "entropic_shield", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Cleric, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** PRPG Core Rulebook pg 278

A magical field appears around you, glowing with a chaotic blast of multicolored hues. This field
deflects incoming arrows, rays, and other ranged attacks. Each ranged attack directed at you for
which the attacker must make an attack roll has a 20% miss chance (similar to the effects of
concealment). Other attacks that simply work at a distance are not affected.
