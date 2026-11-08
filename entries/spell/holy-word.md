+++
id = "ref/spell/holy-word"
kind = "spell"
title = "Holy Word"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_word", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good", "sonic"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "40 ft."
effects = [
  { label = "Area", value = "nongood creatures in a 40-ft.-radius spread centered on you" },
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
Area: nongood creatures in a 40-ft.-radius spread centered on you
Descriptors: good, sonic
:::

**Sources:** PRPG Core Rulebook pg 297

Any nongood creature within the area of a holy word spell suffers the following ill effects.

|HD|Effect|
| --- | --- |
|Equal to caster level|Deafened|
|Up to caster level - 1|Blinded, deafened|
|Up to caster level - 5|Paralyzed, blinded, deafened|
|Up to caster level - 10|Killed, paralyzed, blinded, deafened|

The effects are cumulative and concurrent. A successful Will save reduces or eliminates these
effects. Creatures affected by multiple effects make only one save and apply the result to all the
effects.

_Deafened:_ The creature is deafened for 1d4 rounds. Save negates.

_Blinded:_ The creature is blinded for 2d4 rounds. Save reduces the blinded effect to 1d4 rounds.

_Paralyzed:_ The creature is paralyzed and helpless for 1d10 minutes. Save reduces the paralyzed
effect to 1 round.

_Killed:_ Living creatures die. Undead creatures are destroyed. Save negates. If the save is
successful, the creature instead takes 3d6 points of damage + 1 point per caster level (maximum
+25).

Furthermore, if you are on your home plane when you cast this spell, nongood extraplanar creatures
within the area are instantly banished back to their home planes. Creatures so banished cannot
return for at least 24 hours. This effect takes place regardless of whether the creatures hear the
holy word or not. The banishment effect allows a Will save (at a -4 penalty) to negate.

Creatures whose HD exceed your caster level are unaffected by holy word.
