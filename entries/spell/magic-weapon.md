+++
id = "ref/spell/magic-weapon"
kind = "spell"
title = "Magic Weapon"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_weapon", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
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
Level: 1: Antipaladin, Arcanist, Bloodrager, Cleric, Inquisitor, Magus, Occultist, Oracle, Paladin, Red Mantis Assassin, Shaman, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: weapon touched
:::

**Sources:** PRPG Core Rulebook pg 310

Magic weapon gives a weapon a +1 enhancement bonus on attack and damage rolls. An enhancement bonus
does not stack with a masterwork weapon's +1 bonus on attack rolls.

You can't cast this spell on a natural weapon, such as an unarmed strike (instead, see magic fang).
A monk's unarmed strike is considered a weapon, and thus it can be enhanced by this spell.

### Greater Mythic Magic Weapon

**Sources:** Mythic Adventures pg 100

You can add one of the following weapon special abilities to the weapon: flaming, frost, keen,
merciful, shock, or thundering.

_Augmented (5th):_ If you expend two uses of mythic power, you can reduce the granted enhancement
bonus by 1 to add two of the above abilities or one of the following abilities: anarchic, axiomatic,
flaming burst, holy, icy burst, shocking burst, or unholy.
