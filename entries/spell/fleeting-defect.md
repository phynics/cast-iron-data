+++
id = "ref/spell/fleeting-defect"
kind = "spell"
title = "Fleeting Defect"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fleeting_defect", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one solid object that does not have the broken condition, or one construct" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates (harmless, object), see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bloodrager, Bard, Magus, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Fortitude negates (harmless, object), see text
Spell resistance: no
Target: one solid object that does not have the broken condition, or one construct
:::

**Sources:** Black Markets pg 31

You cause a single object to temporarily gain the broken condition. The target must be a single
solid object, regardless of its composition, weighing up to 10 pounds per caster level. Attended
objects are allowed a Fortitude save. When this spell ends, the object reverts to its original
quality. An item destroyed while under the effects of this spell remains destroyed when this spell
ends.

This spell can be cast on a single construct to disrupt its animating force. A construct that fails
its saving throw takes a -2 circumstance penalty on attack rolls, saving throws, skill checks, and
ability checks for the duration of the spell.
