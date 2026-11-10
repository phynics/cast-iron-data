+++
id = "ref/spell/bleeding-strike"
kind = "spell"
title = "Bleeding Strike"
source_ids = ["pathfinder-77-herald-of-the-ivory-labyrinth"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bleeding_strike", path = "json/spells12.json" },
]
[[sources]]
publication = "pathfinder-77-herald-of-the-ivory-labyrinth"
page = "75"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Effect", value = "one slashing melee weapon touched" },
]
duration = "1 round/level or until discharged"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Cleric, Hunter, Oracle, Ranger, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Effect: one slashing melee weapon touched
:::

> _Priests of [Baphomet](ref/faith/baphomet) have access to the following spell._

You imbue a slashing melee weapon with the ability to create a bleeding wound. As a free action when
the weapon hits a living creature, the wielder can discharge this spell to add 1 point of bleed
damage to the weapon's base damage. This bleeding is difficult to stop; add your spellcasting
ability modifier (Wisdom for clerics, and so on) to the DC to stop the bleeding.
