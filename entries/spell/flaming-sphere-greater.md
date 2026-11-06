+++
id = "ref/spell/flaming-sphere-greater"
kind = "spell"
title = "Greater Flaming Sphere"
source_ids = ["core-rulebook", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flaming_sphere_greater", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (tallow, brimstone, and powdered iron)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "5-ft.-diameter sphere" },
]
duration = "1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bloodrager, Druid, Hunter, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (tallow, brimstone, and powdered iron)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Reflex negates
Spell resistance: yes
Effect: 5-ft.-diameter sphere
Descriptors: fire
:::

## Flaming Sphere

**Sources:** PRPG Core Rulebook pg 283

A burning globe of fire rolls in whichever direction you point and burns those it strikes. It moves
30 feet per round. As part of this movement, it can ascend or jump up to 30 feet to strike a target.
If it enters a space with a creature, it stops moving for the round and deals 3d6 points of fire
damage to that creature, though a successful Reflex save negates that damage. A flaming sphere rolls
over barriers less than 4 feet tall. It ignites flammable substances it touches and illuminates the
same area as a torch would.

The sphere moves as long as you actively direct it (a move action for you); otherwise, it merely
stays at rest and burns. It can be extinguished by any means that would put out a normal fire of its
size. The surface of the sphere has a spongy, yielding consistency and so does not cause damage
except by its flame. It cannot push aside unwilling creatures or batter down large obstacles. A
flaming sphere winks out if it exceeds the spell's range.

### Greater Flaming Sphere

**Sources:** Advanced Class Guide pg 182

This spell functions as flaming sphere, except that it deals 6d6 points of fire damage to any
creature it strikes. Any creature that fails its save against the sphere
[catches on fire](ref/rule/catching-on-fire). If a creature catches on fire, the DC to extinguish
the flames is equal to the DC of this spell.
