+++
id = "ref/carried/ultimate-combat/spells/named-bullet/greater"
kind = "spell"
title = "Named Bullet, Greater"
source_ids = ["ultimate-combat"]
section = ["Spells", "Named Bullet"]
tags = ["divination"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Named Bullet/Greater", path = "ultimate_combat/spell/named_bullet_greater.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 6 },
  { class = "Ranger", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (an item from the selected creature or creature type)"
range = "touch"
effects = [
  { label = "Target", value = "one piece of ammunition or one thrown weapon" },
]
duration = "10 minutes/level or until discharged"
saving_throw = "Will negates (harmless, object)"
spell_resistance = "yes (harmless, object)"
+++

::: statblock
School: divination
Level: 4: Hunter, Hunter, Hunter, Ranger\
6: Arcanist, Inquisitor, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S, M/DF (an item from the selected creature or creature type)
Range: touch
Target: one piece of ammunition or one thrown weapon
Duration: 10 minutes/level or until discharged
Saving Throw: Will negates (harmless, object)
Spell Resistance: yes (harmless, object)
:::

_As named bullet, but deals 2 points of damage for every caster level._

This spell functions like _[named bullet](ref/spell/named-bullet)_, except it deals 2 extra points
of damage per caster level (maximum 40).
