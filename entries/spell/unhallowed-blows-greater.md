+++
id = "ref/spell/unhallowed-blows-greater"
kind = "spell"
title = "Greater Unhallowed Blows"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unhallowed_blows_greater", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of dust from a destroyed undead creature)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one undead creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Antipaladin, Arcanist, Cleric, Inquisitor, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of dust from a destroyed undead creature)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one undead creature/level, no two of which can be more than 30 ft. apart
Descriptors: evil
:::

## Unhallowed Blows

**Sources:** People of the Wastes pg 29

This spell empowers the natural attacks or unarmed strikes of undead creatures, granting a +1
enhancement bonus on attack and damage rolls made by the target with its unarmed strikes or attacks
with one natural attack. This spell can cause an undead creature's unarmed strike to deal lethal
damage, but in this case, the attack does not gain an enhancement bonus.

Unhallowed blows can be made permanent with a [permanency](ref/spell/permanency) spell. In this
case, the caster must be at least 9th level and must expend 2,500 gp worth of diamond dust as a
material component.

### Greater Unhallowed Blows

**Sources:** People of the Wastes pg 29

This spell functions as unhallowed blows, except the enhancement bonus is +1 per 4 caster levels
(maximum +5). Alternatively, you can imbue all of a creature's natural weapons with a +1 enhancement
bonus (regardless of your caster level).

Greater unhallowed blows can be made permanent with a [permanency](ref/spell/permanency) spell. In
this case, the caster must be at least 11th level and must expend 7,500 gp worth of diamond dust as
a material component.
