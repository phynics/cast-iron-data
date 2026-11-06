+++
id = "ref/spell/warp-metal"
kind = "spell"
title = "Warp Metal"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warp_metal", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a twisted wire)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 Small metal object/level, all within a 20-ft. radius; see text" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Bloodrager, Cleric, Druid, Hunter, Medium, Occultist, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a twisted wire)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: 1 Small metal object/level, all within a 20-ft. radius; see text
Descriptors: earth
:::

**Sources:** Magic Tactics Toolbox pg 6

You cause metal to bend and warp, permanently destroying its straightness, form, and strength. A
warped door springs open (or becomes stuck, requiring a successful Strength check to open, at your
option). A vehicle grinds to a halt and ceases to operate. Warped ranged weapons are useless. A
warped melee weapon imposes a -4 penalty on attack rolls.

You can warp one Small or smaller object or its equivalent per caster level. A Medium object counts
as two Small objects, a Large object as four, a Huge object as eight, a Gargantuan object as 16, and
a Colossal object as 32.

Alternatively, you can unwarp metal (effectively warping it back to normal) with this spell.
[Make whole](ref/spell/make-whole), on the other hand, does nothing to repair a warped item.

You can combine multiple consecutive castings of warp metal to warp (or unwarp) an object that is
too large for you to warp with a single casting. Until the object is completely warped, it suffers
no ill effects.
