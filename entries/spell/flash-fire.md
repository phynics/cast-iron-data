+++
id = "ref/spell/flash-fire"
kind = "spell"
title = "Flash Fire"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flash_fire", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of powdered fool's gold)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 firearm" },
]
duration = "instantaneous"
saving_throw = "Will negates (object), see text"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of powdered fool's gold)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object), see text
Spell resistance: yes (object)
Target: 1 firearm
:::

**Sources:** Ultimate Combat pg 230

The firearm fires with a blinding flash, even if the firearm is not currently loaded. Every creature
within 15 feet of the creature carrying the weapon must succeed at a Fortitude save or be blinded
for 1d4 rounds. The creature carrying the firearm takes a -4 penalty on this saving throw. If the
firearm is loaded, the ammunition is wasted.
