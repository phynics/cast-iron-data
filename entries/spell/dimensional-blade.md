+++
id = "ref/spell/dimensional-blade"
kind = "spell"
title = "Dimensional Blade"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dimensional_blade", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 6 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Paladin", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 swift action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Antipaladin, Bloodrager, Paladin\
5: Inquisitor, Magus\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 swift action
Components: V, S
Range: personal
Duration: 1 round
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Melee Tactics Toolbox pg 30

This spell gives you the power to turn one melee weapon in your hand into a two-dimensional object
with length and height but no width. A sword becomes a flat image of a sword, a mace is reduced to a
flat outline, and so on. The magic of the spell allows the weapon to be wielded by you normally,
creating just enough depth to grasp it.

Attacks made with the weapon are melee touch attacks that ignore all armor. Force effects, such as
mage armor and shield, still apply their AC against attacks made with a dimensional blade.
Bludgeoning weapons used to make attacks with this spell deal half damage and are treated as
slashing weapons. If the weapon leaves your hand before the end of the spell, the effect ends.
