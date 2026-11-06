+++
id = "ref/spell/air-geyser"
kind = "spell"
title = "Air Geyser"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "air_geyser", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or object up to Large size" },
]
duration = "instantaneous"
saving_throw = "Reflex partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Druid, Hunter, Magus, Sorcerer, Witch, Wizard\
4: Shaman
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex partial (see text)
Spell resistance: yes
Target: one creature or object up to Large size
Descriptors: air
:::

**Sources:** Advanced Class Guide pg 173

You create a powerful blast of air capable of flinging an opponent upward. If the target fails its
Reflex save, the force of the air deals 2d6 points of bludgeoning damage and hurls the target upward
a number of feet equal to 5 × your caster level. If a solid object (such as a ceiling) is
encountered, the target strikes the object in the same manner as it would during a normal fall.
After this blast of air ceases, the target falls down (unless it was flying), taking falling damage
as normal. A successful save means the target takes half damage from the air blast but is not moved
by it.
