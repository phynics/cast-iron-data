+++
id = "ref/spell/thanatotic-fury"
kind = "spell"
title = "Thanatotic Fury"
source_ids = ["pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thanatotic_fury", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (shavings from a holy symbol)"
range = "personal"
effects = [
  { label = "Target", value = "you (see text)" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (shavings from a holy symbol)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you (see text)
:::

**Sources:** Pathfinder \#91: Battle of Bloodmarch Hills pg 71

You may cast this spell only if you have the giant subtype. When casting this spell, you channel the
fury and the abilities of thanatotic titans, gaining some of their abilities for a short period of
time. When you hit a creature capable of casting divine spells, that creature must succeed at a Will
saving throw or be unable to cast divine spells for 1d4 rounds and be shaken for the same duration.
If the save is successful, the target is instead shaken for only 1 round.

Additionally, your attacks are treated as epic and evil for the purposes of overcoming
[damage reduction](ref/rule/damage-reduction).
