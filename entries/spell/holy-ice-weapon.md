+++
id = "ref/spell/holy-ice-weapon"
kind = "spell"
title = "Holy Ice Weapon"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_ice_weapon", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["cold", "good", "water"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a flask of holy water, or 5 pounds of powdered silver worth 25 gp)"
range = "0 ft."
effects = [
  { label = "Effect", value = "one ice weapon" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (a flask of holy water, or 5 pounds of powdered silver worth 25 gp)
Range: 0 ft.
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Effect: one ice weapon
Descriptors: cold, good, water
:::

**Sources:** Advanced Class Guide pg 185

You create a masterwork weapon that has the qualities of ice and holy water. This weapon must be a
simple weapon or your deity's favored weapon. The weapon deals normal damage for a weapon of that
type, plus 1 point of cold damage per caster level (maximum 10). In addition, any creature struck by
the weapon is also hit by holy water, dealing 1d4 points of damage if the creature is susceptible to
holy water. If the weapon leaves your hands for more than 1 round, it melts and the spell ends.

At caster level 6th, the weapon gains the returning weapon special ability when thrown, melting away
after an attack and re-forming in your hand just before your next turn.

### Unholy Ice Weapon

**Sources:** Advanced Class Guide pg 198

This spell functions as holy ice weapon, except the weapon is made of frozen unholy water, and
instead deals additional damage to creatures that are susceptible to unholy water.
