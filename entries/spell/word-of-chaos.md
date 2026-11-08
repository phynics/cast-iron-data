+++
id = "ref/spell/word-of-chaos"
kind = "spell"
title = "Word of Chaos"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "word_of_chaos", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["chaotic", "sonic"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "40 ft."
effects = [
  { label = "Area", value = "nonchaotic creatures in a 40-ft. radius spread centered on you" },
]
duration = "instantaneous"
saving_throw = "none or Will negates; see text"
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
Saving throw: none or Will negates; see text
Spell resistance: yes
Area: nonchaotic creatures in a 40-ft. radius spread centered on you
Descriptors: chaotic, sonic
:::

**Sources:** PRPG Core Rulebook pg 371

Any nonchaotic creature within the area of a word of chaos spell suffers the following ill effects,
depending on their HD.

|HD|Effect|
| --- | --- |
|Equal to caster level|Deafened|
|Up to caster level - 1|Stunned, deafened|
|Up to caster level - 5|Confused, stunned, deafened|
|Up to caster level - 10|Killed, confused, stunned, deafened|

The effects are cumulative and concurrent. A successful Will save reduces or eliminates these
effects. Creatures affected by multiple effects make only one save and apply the result to all the
effects.

_Deafened:_ The creature is deafened for 1d4 rounds. Save negates.

_Stunned:_ The creature is stunned for 1 round. Save negates.

_Confused:_ The creature is confused for 1d10 minutes. This is a mind-affecting enchantment effect.
Save reduces the confused effect to 1 round.

_Killed:_ Living creatures die. Undead creatures are destroyed. Save negates. If the save is
successful, the creature instead takes 3d6 points of damage + 1 point per caster level (maximum
+25).

Furthermore, if you are on your home plane when you cast this spell, nonchaotic extraplanar
creatures within the area are instantly banished back to their home planes. Creatures so banished
cannot return for at least 24 hours. This effect takes place regardless of whether the creatures
hear the word of chaos or not. The banishment effect allows a Will save (at a -4 penalty) to negate.

Creatures whose HD exceed your caster level are unaffected by word of chaos.
