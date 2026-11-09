+++
id = "ref/spell/oasis"
kind = "spell"
title = "Oasis"
source_ids = ["heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oasis", path = "json/spells7.json" },
]
[[sources]]
publication = "heroes-of-the-wild"
page = "31"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "30 minutes"
components = "V, S, M/DF (1 gallon of water)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "water source similar to a natural spring" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Druid, Hunter\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 30 minutes
Components: V, S, M/DF (1 gallon of water)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: water source similar to a natural spring
:::

This spell functions in any natural terrain on the Material Plane. It redirects the flow of water in
the ground toward the surface at the designated point, creating a permanent water source similar to
a natural spring. The spring discharges 5 gallons of pure drinking water per caster level each hour.
If the shape of the terrain is suitable, a pond forms around the spring. If there is already a
natural spring within 1 mile, its water output is reduced by an amount equal to the water produced
by this spell's spring. A spring that has its water output reduced to 0 gallons per hour dries up
and ceases to be a spring.

This spell functions differently depending on the terrain in which it's cast. In a desert, you must
succeed at a DC 25 caster level check to actually create the spring, and its output is 1 gallon of
drinking water per caster level each day. Furthermore, in dry areas, erosion may cause the flow of
water to be blocked if the affected area is left untended before a sufficient amount of vegetation
has grown around it to keep the soil in place. In an arctic environment, low temperatures may cause
the water to freeze. In a tropical environment, parasites may contaminate the water if the spring is
created in a place where the water stands in a stagnant pool.
