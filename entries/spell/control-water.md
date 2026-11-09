+++
id = "ref/spell/control-water"
kind = "spell"
title = "Control Water"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "control_water", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "260"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of dust for lower water or a drop of water for raise water)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "water in a volume of 10 ft./level by 10 ft./level by 2 ft./level (S)" },
]
duration = "10 minutes/level (D)"
saving_throw = "none; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Druid, Hunter, Oracle, Shaman, Warpriest\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of dust for lower water or a drop of water for raise water)
Range: long (400 ft. + 40 ft./level)
Duration: 10 minutes/level (D)
Saving throw: none; see text
Spell resistance: no
Area: water in a volume of 10 ft./level by 10 ft./level by 2 ft./level (S)
Descriptors: water
:::

This spell has two different applications, both of which control water in different ways. The first
version of this spell causes water in the area to swiftly evaporate or to sink into the ground
below, lowering the water's depth. The second version causes the water to surge and rise, increasing
its overall depth and possibly flooding nearby areas.

_Lower Water:_ This causes water or similar liquid to reduce its depth by as much as 2 feet per
caster level (to a minimum depth of 1 inch). The water is lowered within a squarish depression whose
sides are up to caster level × 10 feet long. In extremely large and deep bodies of water, such as a
deep ocean, the spell creates a whirlpool that sweeps ships and similar craft downward, putting them
at risk and rendering them unable to leave by normal movement for the duration of the spell. When
cast on water elementals and other water-based creatures, this spell acts as a
[slow](ref/spell/slow) spell (Will negates). The spell has no effect on other creatures.

_Raise Water:_ This causes water or similar liquid to rise in height, just as the lower water
version causes it to lower. Boats raised in this way slide down the sides of the hump that the spell
creates. If the area affected by the spell includes riverbanks, a beach, or other land nearby, the
water can spill over onto dry land.

With either version of this spell, you may reduce one horizontal dimension by half and double the
other horizontal dimension to change the overall area of effect.
