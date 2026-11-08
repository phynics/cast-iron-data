+++
id = "ref/spell/nightmare"
kind = "spell"
title = "Nightmare"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nightmare", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S"
range = "unlimited"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium\
5: Alchemist, Arcanist, Bard, Investigator, Mesmerist, Psychic, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 10 minutes
Components: V, S
Range: unlimited
Duration: instantaneous
Saving throw: Will negates; see text
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 316

You send a hideous and unsettling phantasmal vision to a specific creature that you name or
otherwise specifically designate.

The nightmare prevents restful sleep and causes 1d10 points of damage. The nightmare leaves the
subject fatigued and unable to regain arcane spells for the next 24 hours.

The difficulty of the save depends on your knowledge the subject and the physical connection (if
any) you have to that creature.

|Knowledge|Will Save Modifier|
| --- | --- |
|None^[1](ref/spell/nightmare#footnote-n)^|+10|
|Secondhand (you have heard of the subject)|+5|
|Firsthand (you have met the subject)|+0|
|Familiar (you know the subject well)|-5|

|Connection|Will Save Modifier|
| --- | --- |
|Likeness or picture|-2|
|Possession or garment|-4|
|Body part, lock of hair, bit of nail, etc.|-10|

[Dispel evil](ref/spell/dispel-evil) cast on the subject while you are casting the spell dispels the
nightmare and causes you to be stunned for 10 minutes per caster level of the dispel evil.

If the recipient is awake when the spell begins, you can choose to cease casting (ending the spell)
or to enter a trance until the recipient goes to sleep, whereupon you become alert again and
complete the casting. If you are disturbed during the trance, you must succeed on a
[concentration](ref/rule/concentration) check as if you were in the midst of casting a spell or the
spell ends.

If you choose to enter a trance, you are not aware of your surroundings or the activities around you
while in the trance.

You are defenseless, both physically and mentally, while in the trance. (You always fail Reflex and
Will saving throws, for example.)

Creatures who don't sleep (such as outsiders) or dream are immune to this spell.

###### ^1^ {#footnote-n}

You must have some sort of connection to a creature of which you have no knowledge.
