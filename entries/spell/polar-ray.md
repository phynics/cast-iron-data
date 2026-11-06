+++
id = "ref/spell/polar-ray"
kind = "spell"
title = "Polar Ray"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "polar_ray", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, F (a white ceramic cone or prism)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 8: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a white ceramic cone or prism)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Effect: ray
Descriptors: cold
:::

**Sources:** PRPG Core Rulebook pg 323

A blue-white ray of freezing air and ice springs from your hand. You must succeed on a ranged touch
attack with the ray to deal damage to a target. The ray deals 1d6 points of cold damage per caster
level (maximum 25d6) and 1d4 points of Dexterity drain.

### Mythic Polar Ray

**Sources:** Mythic Adventures pg 103\
The damage dealt increases to 1d8 points of cold damage per caster level (maximum 25d8) and 1d6
points of Dexterity drain. If the target takes damage from this spell, it becomes partially encased
in ice, reducing its speed by half. Creatures with the cold or incorporeal subtypes or immunity to
being grappled are immune to this effect. The reduced movement lasts until the ice is destroyed.
Destroying the ice requires a successful Strength or dispel check against the spell's DC or dealing
1 point of bludgeoning or fire damage per caster level to the target.
