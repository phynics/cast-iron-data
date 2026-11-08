+++
id = "ref/spell/blade-barrier"
kind = "spell"
title = "Blade Barrier"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blade_barrier", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "wall of whirling blades up to 20 ft. long/level, or a ringed wall of whirling blades with a radius of up to 5 ft. per two levels; either form is 20 ft. high" },
]
duration = "1 minute/level (D)"
saving_throw = "Reflex half or Reflex negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Cleric, Inquisitor, Occultist, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: Reflex half or Reflex negates; see text
Spell resistance: yes
Effect: wall of whirling blades up to 20 ft. long/level, or a ringed wall of whirling blades with a radius of up to 5 ft. per two levels; either form is 20 ft. high
Descriptors: force
:::

**Sources:** PRPG Core Rulebook pg 249

An immobile, vertical curtain of whirling blades shaped of pure force springs into existence. Any
creature passing through the wall takes 1d6 points of damage per caster level (maximum 15d6), with a
Reflex save for half damage.

If you evoke the barrier so that it appears where creatures are, each creature takes damage as if
passing through the wall. Each such creature can avoid the wall (ending up on the side of its
choice) and thus take no damage by making a successful Reflex save.

A blade barrier provides cover (+4 bonus to AC, +2 bonus on Reflex saves) against attacks made
through it.
