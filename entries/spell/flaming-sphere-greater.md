+++
id = "ref/spell/flaming-sphere-greater"
kind = "spell"
title = "Greater Flaming Sphere"
source_ids = ["core-rulebook", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flaming_sphere_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/flaming-sphere" },
]
[[sources]]
publication = "advanced-class-guide"
page = "182"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (tallow, brimstone, and powdered iron)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "5-ft.-diameter sphere" },
]
duration = "1 round/level"
saving_throw = "Reflex negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Bloodrager, Druid, Hunter, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (tallow, brimstone, and powdered iron)
Range: medium (100 ft. + 10 ft./level)
Effect: 5-ft.-diameter sphere
Duration: 1 round/level
Saving throw: Reflex negates (see text)
Spell resistance: yes
Descriptors: fire
:::

### Greater Flaming Sphere

This spell functions as [flaming sphere](ref/spell/flaming-sphere), except that it deals 6d6 points
of fire damage to any creature it strikes. Any creature that fails its save against the sphere
[catches on fire](ref/rule/catching-on-fire). If a creature catches on fire, the DC to extinguish
the flames is equal to the DC of this spell.
