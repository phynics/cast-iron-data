+++
id = "ref/spell/recoil-fire"
kind = "spell"
title = "Recoil Fire"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "recoil_fire", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (hoof shavings from a mule)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 firearm" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (hoof shavings from a mule)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: 1 firearm
:::

**Sources:** Ultimate Combat pg 241

The target firearm suddenly fires of its own volition, even if it is unloaded, generating a recoil
so great that the wielder or carrier of the firearm must scramble to hold onto it and becomes
flat-footed until the start of his next turn. If the wielder is already flat-footed, he is instead
knocked prone. If the firearm was loaded, that ammunition is wasted.
