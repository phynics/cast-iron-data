+++
id = "ref/spell/chains-of-fire"
kind = "spell"
title = "Chains of Fire"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chains_of_fire", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F (a drop of oil and a small piece of flint)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one primary target, plus one secondary target/level (each of which must be within 30 ft. of the primary target)" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a drop of oil and a small piece of flint)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Targets: one primary target, plus one secondary target/level (each of which must be within 30 ft. of the primary target)
Descriptors: fire
:::

**Sources:** Advanced Race Guide pg 131

> _[Ifrits](ref/race/ifrit) have access to the following spell._

This spell functions like chain lightning, except as noted above, and the spell deals fire damage
instead of electricity damage.
