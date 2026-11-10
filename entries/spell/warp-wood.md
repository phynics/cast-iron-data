+++
id = "ref/spell/warp-wood"
kind = "spell"
title = "Warp Wood"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warp_wood", path = "json/spells11.json" },
]
[[sources]]
publication = "core-rulebook"
page = "368"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Shaman", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 Small wooden object/level, all within a 20-ft. radius" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Occultist, Shaman
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: 1 Small wooden object/level, all within a 20-ft. radius
:::

You cause wood to bend and warp, permanently destroying its straightness, form, and strength. A
warped door springs open (or becomes stuck, requiring a Strength check to open, at your option). A
boat or ship springs a leak. Warped ranged weapons are useless. A warped melee weapon causes a -4
penalty on attack rolls.

You may warp one Small or smaller object or its equivalent per caster level. A Medium object counts
as two Small objects, a Large object as four, a Huge object as eight, a Gargantuan object as 16, and
a Colossal object as 32.

Alternatively, you can unwarp wood (effectively warping it back to normal) with this spell.
[Make whole](ref/spell/make-whole), on the other hand, does no good in repairing a warped item.

You can combine multiple consecutive warp wood spells to warp (or unwarp) an object that is too
large for you to warp with a single spell. Until the object is completely warped, it suffers no ill
effects.
