+++
id = "ref/carried/ultimate-combat/spells/returning-weapon/communal"
kind = "spell"
title = "Returning Weapon, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Returning Weapon"]
tags = ["conjuration", "teleportation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Returning Weapon/Communal", path = "ultimate_combat/spell/returning_weapon_communal.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["teleportation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "weapons that can be thrown" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless, object)"
spell_resistance = "yes (harmless, object)"
+++

::: statblock
School: conjuration (teleportation)
Level: 2: Hunter, Hunter, Hunter, Inquisitor, Magus, Ranger\
3: Arcanist, Bard, Cleric, Oracle, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: weapons that can be thrown
Duration: 1 minute/level
Saving Throw: Will negates (harmless, object)
Spell Resistance: yes (harmless, object)
:::

_As returning weapon, but you may divide the duration among weapons touched._

This spell functions like _[returning weapon](ref/spell/returning-weapon)_, except you divide the
duration in 1-minute intervals among the targeted weapons.
