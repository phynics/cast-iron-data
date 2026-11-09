+++
id = "ref/spell/enemy-hammer"
kind = "spell"
title = "Enemy Hammer"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enemy_hammer", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "219"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (puppet strings)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Occultist, Psychic, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (puppet strings)
Range: long (400 ft. + 40 ft./level)
Duration: 1 round/level (D)
Saving throw: Fortitude partial
Spell resistance: yes
Target: one creature
:::

You grab a creature with telekinesis and use it to batter nearby opponents or objects. You must
target a specific creature when casting this spell and once you select that creature you cannot
switch to another. Each round, as a standard action, you can attempt to hurl the target at any
creature or object within 30 feet of it. You must make an attack roll whenever you use the target as
a weapon. The attack bonus for this attack is equal to your caster level plus either your
Intelligence or Charisma modifier (whichever is higher). If you successfully hit the new target with
the creature both it and the creature take damage based on the creature's size.

|Creature Size|Damage Dealt|
| --- | --- |
|Fine|1d4|
|Diminutive|1d6|
|Tiny|1d8|
|Small|1d10|
|Medium|2d6|
|Large|2d8|
|Huge|2d10|
|Gargantuan|3d6|
|Colossal|3d8|

The target creature can make a Fortitude saving throw each time you attempt to use it as a weapon.
If it makes its saving throw it can act normally, but if it fails its save it loses all actions for
the round and ends its turn prone in a square adjacent to the target of your attack. However, if the
creature chooses to resist your efforts to move it, taking no other actions for the round, it gets a
+4 circumstance bonus on its saving throw. The spell ends immediately if the target creature dies or
is destroyed.
