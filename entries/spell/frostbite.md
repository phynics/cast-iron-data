+++
id = "ref/spell/frostbite"
kind = "spell"
title = "Frostbite"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frostbite", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["cold"]
levels = [
  { class = "Bloodrager", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Targets", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Bloodrager, Druid, Hunter, Magus, Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Targets: creature touched
Descriptors: cold
:::

**Sources:** Ultimate Magic pg 221

Your melee touch attack deals 1d6 points of nonlethal cold damage + 1 point per level, and the
target is fatigued. The fatigued condition ends when the target recovers from the nonlethal damage.
This spell cannot make a creature exhausted even if it is already fatigued. You can use this melee
touch attack up to one time per level.
