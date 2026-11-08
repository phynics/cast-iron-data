+++
id = "ref/spell/shout"
kind = "spell"
title = "Shout"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shout", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial or Reflex negates (object); see text"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Bloodrager, Bard, Magus, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: 30 ft.
Duration: instantaneous
Saving throw: Fortitude partial or Reflex negates (object); see text
Spell resistance: yes (object)
Area: cone-shaped burst
Descriptors: sonic
:::

**Sources:** PRPG Core Rulebook pg 343

You emit an ear-splitting yell that deafens and damages creatures in its path. Any creature within
the area is deafened for 2d6 rounds and takes 5d6 points of sonic damage. A successful save negates
the deafness and reduces the damage by half. Any exposed brittle or crystalline object or
crystalline creature takes 1d6 points of sonic damage per caster level (maximum 15d6). An affected
creature is allowed a Fortitude save to reduce the damage by half, and a creature holding fragile
objects can negate damage to them with a successful Reflex save. A shout spell cannot penetrate a
silence spell.
