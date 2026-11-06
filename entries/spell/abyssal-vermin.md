+++
id = "ref/spell/abyssal-vermin"
kind = "spell"
title = "Abyssal Vermin"
source_ids = ["pathfinder-78-city-of-locusts"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "abyssal_vermin", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one vermin or vermin swarm" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Antipaladin\
4: Arcanist, Cleric, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Target: one vermin or vermin swarm
:::

**Sources:** Pathfinder \#78: City of Locusts pg 75

> _Priests of [Deskari](ref/faith/deskari) have access to the following spell._

You infuse the target with power from the Abyss, granting it the fiendish creature simple template.
The swarm gains DR 5/good if it has at least 5 Hit Dice, or DR 10/good it if has at least 11 HD. It
gains cold resistance 5 and fire resistance 5 if it has at least 5 HD, or cold resistance 10 and
fire resistance 10 if it has at least 11 HD. It gains [spell resistance](ref/rule/spell-resistance)
equal to its CR + 6. Once per day, it can smite good (as a swift action against a good opponent, the
vermin adds its Charisma bonus to its attack rolls and its HD to its damage rolls until the opponent
is dead). If the targeted vermin is under your command, it automatically fails its saving throw
against this spell. This spell has no effect on vermin that already have the fiendish creature
simple template.
