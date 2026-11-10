+++
id = "ref/spell/stoke-the-inner-fire"
kind = "spell"
title = "Stoke the Inner Fire"
source_ids = ["pathfinder-95-anvil-of-fire"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stoke_the_inner_fire", path = "json/spells9.json" },
]
[[sources]]
publication = "pathfinder-95-anvil-of-fire"
page = "66"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: fire
:::

> _Priests of [Zursvaater](ref/faith/zursvaater) have access to the following spell._

You increase the natural heat within your body, transferring it to your weapons and armor. As a
swift action, you may grant one of your natural or manufactured weapons the flaming special ability
for 1 round. If you have the fire subtype, your weapon instead gains the flaming burst special
ability. If the weapon leaves your hand for any reason, it loses the flaming (or flaming burst)
special ability until you spend a swift action to activate it again. You can only have stoke the
inner fire active on one weapon at a time, and spending a swift action to imbue a second weapon with
the spell's power immediately ends its effect on the first weapon.

The spell also builds a wall of searing heat between your armor and your flesh. Anyone striking you
with a natural weapon or unarmed strike takes 1 point of fire damage. A creature that grapples you
or is grappled by you takes 1 point of fire damage each round the grapple persists. If you have the
fire subtype, these damage values increase to 1d6 points of fire damage each. Removing your armor
causes this wall of heat to dissipate and ends these effects.
