+++
id = "ref/spell/burst-of-radiance"
kind = "spell"
title = "Burst of Radiance"
source_ids = ["champions-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burst_of_radiance", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good", "light"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of flint and a pinch of silver dust)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "10-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of flint and a pinch of silver dust)
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Reflex partial
Spell resistance: yes
Area: 10-ft.-radius burst
Descriptors: good, light
:::

**Sources:** Champions of Purity pg 29

This spell fills the area with a brilliant flash of shimmering light. Creatures in the area are
blinded for 1d4 rounds, or dazzled for 1d4 rounds if they succeed at a Reflex save. Evil creatures
in the area of the burst take 1d4 points of damage per caster level (max 5d4), whether they succeed
at the Reflex save or not.
