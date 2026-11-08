+++
id = "ref/spell/blasphemy"
kind = "spell"
title = "Blasphemy"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blasphemy", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil", "sonic"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "40 ft."
effects = [
  { label = "Area", value = "nonevil creatures in a 40-ft.-radius spread centered on you" },
]
duration = "instantaneous"
saving_throw = "Will partial"
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
Saving throw: Will partial
Spell resistance: yes
Area: nonevil creatures in a 40-ft.-radius spread centered on you
Descriptors: evil, sonic
:::

**Sources:** PRPG Core Rulebook pg 249

Any nonevil creature within the area of a blasphemy spell suffers the following ill effects.

|HD|Effect|
| --- | --- |
|Equal to caster level|Dazed|
|Up to caster level - 1|Weakened, dazed|
|Up to caster level - 5|Paralyzed, weakened, dazed|
|Up to caster level - 10|Killed, paralyzed, weakened, dazed|

The effects are cumulative and concurrent. A successful Will save reduces or eliminates these
effects. Creatures affected by multiple effects make only one save and apply the result to all the
effects.

_Dazed:_ The creature can take no actions for 1 round, though it defends itself normally. Save
negates.

_Weakened:_ The creature's Strength score decreases by 2d6 points for 2d4 rounds. Save for half.

_Paralyzed:_ The creature is paralyzed and helpless for 1d10 minutes. Save reduces the paralyzed
effect to 1 round.

_Killed:_ Living creatures die. Undead creatures are destroyed. Save negates. If the save is
successful, the creature instead takes 3d6 points of damage + 1 point per caster level (maximum
+25).

Furthermore, if you are on your home plane when you cast this spell, nonevil extraplanar creatures
within the area are instantly banished back to their home planes. Creatures so banished cannot
return for at least 24 hours. This effect takes place regardless of whether the creatures hear the
blasphemy or not. The [banishment](ref/spell/banishment) effect allows a Will save (at a -4 penalty)
to negate.

Creatures whose Hit Dice exceed your caster level are unaffected by blasphemy.
