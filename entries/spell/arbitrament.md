+++
id = "ref/spell/arbitrament"
kind = "spell"
title = "Arbitrament"
aon = "SpellDisplay.aspx?ItemName=Arbitrament"
source_ids = ["planar-adventures", "champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arbitrament", path = "json/spells.json" },
]
[[sources]]
publication = "planar-adventures"
page = "39"
[[sources]]
publication = "champions-of-balance"
page = "26"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "40 ft."
effects = [
  { label = "Target", value = "non-neutral creatures in a 40-ft.-radius spread centered on you" },
]
duration = "instantaneous"
saving_throw = "Will partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Inquisitor\
7: Cleric, Oracle
Casting time: 1 standard action
Components: V
Range: 40 ft.
Duration: instantaneous
Saving throw: Will partial, see text
Spell resistance: yes
Target: non-neutral creatures in a 40-ft.-radius spread centered on you
Descriptors: sonic
:::

All chaotic evil, chaotic good, lawful evil, and lawful good creatures within the area of this spell
suffer the following conditions, based on their Hit Dice.

|Hit Dice|Effect|
| --- | --- |
|Equal to caster level|Sickened|
|Up to caster level - 1|Sickened, staggered|
|Up to caster level - 5|Nauseated, sickened, staggered|
|Up to caster level - 10|Killed, nauseated, sickened, staggered|

The effects are concurrent. A creature can attempt a Will save to reduce or negate the effects. If
subject to multiple effects, the creature rolls once and applies the result to each effect.

_Sickened:_ The creature is sickened for 1d4 rounds (Will negates).

_Staggered:_ The creature is staggered for 2d4 rounds, or for 1d4 rounds on a successful Will save.

_Nauseated:_ The creature is nauseated for 1d10 minutes, or for 1d4 rounds on a successful Will
save.

_Killed:_ Living creatures die, and undead creatures are destroyed. On a successful Will save, the
creature instead takes 3d6 points of damage + 1 point per caster level (maximum +25).

Furthermore, if you are on your home plane when you cast this spell, all chaotic evil, chaotic good,
lawful evil, and lawful good extraplanar creatures within the area are banished to their home planes
(Will negates, at a -4 penalty). Creatures so banished cannot return for at least 24 hours. This
effect takes place regardless of whether the creatures hear the arbitrament.

Creatures whose Hit Dice exceed your caster level are unaffected by arbitrament.
