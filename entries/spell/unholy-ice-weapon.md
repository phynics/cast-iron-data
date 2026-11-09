+++
id = "ref/spell/unholy-ice-weapon"
kind = "spell"
title = "Unholy Ice Weapon"
aon = "SpellDisplay.aspx?ItemName=Unholy%20Ice%20Weapon"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unholy_ice_weapon", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/holy-ice-weapon" },
]
[[sources]]
publication = "advanced-class-guide"
page = "198"

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

### Unholy Ice Weapon

This spell functions as [holy ice weapon](ref/spell/holy-ice-weapon), except the weapon is made of
frozen unholy water, and instead deals additional damage to creatures that are susceptible to unholy
water.
