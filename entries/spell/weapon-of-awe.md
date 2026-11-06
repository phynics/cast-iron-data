+++
id = "ref/spell/weapon-of-awe"
kind = "spell"
title = "Weapon of Awe"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weapon_of_awe", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["emotion"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Inquisitor, Occultist, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: weapon touched
Descriptors: emotion
:::

**Sources:** Advanced Player's Guide pg 256

You transform a single weapon into an awe-inspiring instrument. The weapon gains a +2 sacred bonus
on damage rolls, and if the weapon scores a critical hit, the target of that critical hit becomes
shaken for 1 round with no saving throw. This is a mind-affecting fear effect. A ranged weapon
affected by this spell applies these effects to its ammunition.

You can't cast this spell on a natural weapon, but you can cast it on an unarmed strike.
