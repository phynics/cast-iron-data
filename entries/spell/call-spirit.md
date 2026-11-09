+++
id = "ref/spell/call-spirit"
kind = "spell"
title = "Call Spirit"
aon = "SpellDisplay.aspx?ItemName=Call%20Spirit"
source_ids = ["occult-adventures", "occult-mysteries"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "call_spirit", path = "json/spells2.json" },
]
[[sources]]
publication = "occult-adventures"
page = "160"
[[sources]]
publication = "occult-mysteries"
page = "54"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Calling"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "10 minutes"
components = "V, S"
range = "10 ft."
effects = [
  { label = "Effect", value = "call the spirit of a single deceased humanoid creature" },
]
duration = "concentration"
saving_throw = "Will negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Medium\
5: Cleric, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 10 minutes
Components: V, S
Range: 10 ft.
Duration: concentration
Saving throw: Will negates, see text
Spell resistance: no
Effect: call the spirit of a single deceased humanoid creature
Subschool: Calling
:::

You attempt to cause the spirit of a specific individual to manifest from its final resting place.
You must request the spirit's presence by speaking its name.

Unwilling spirits can resist the summons by succeeding at a Will save. If the chosen spirit resists
your call, another spirit with malevolent intent almost always takes its place, intent on deceiving
you. The difficulty of the save depends on how well you know the subject and what sort of physical
connection (if any) you have to the creature whose spirit you wish to call.

|Knowledge|Will Save Modifier|
| --- | --- |
|Name only^[1](ref/spell/call-spirit#footnote-n)^|+15|
|Secondhand (you have heard of the subject)|+10|
|Firsthand (you met the subject in life)|+5|
|Familiar (you knew the subject well)|+0|

|Connection|Will Save Modifier|
| --- | --- |
|Likeness or picture|-2|
|Possession or garment|-4|
|Body part, lock of hair, nail clipping, etc.|-10|
|Different alignment|+4|

A successfully called spirit manifests as a wispy, vaporous form that vaguely resembles the form the
deceased creature had in life. The spirit has the physical attributes of an unseen servant and is
capable of minor physical manipulations, with the ability to speak in quiet, ghostly whispers in
whatever languages the creature knew while it was alive. The spirit isn't an undead creature, and
isn't beholden to its caller. Whether you summoned the chosen spirit or a deceitful replacement, the
spirit can refuse to answer your questions or attempt to deceive you using Bluff, though in either
case these spirits can speak about only what they knew in life and have no knowledge of events that
occurred after their deaths. Malevolent spirits might take advantage of their limited physical
abilities to cause terrifying spectacles designed to scare the caster.

You must concentrate on maintaining the spell (as a standard action) in order to ask questions at
the rate of one per round. You can ask a total of one question per caster level; the spirit answers
each during the same round. When the spell ends, the spirit's ectoplasmic form fades and the soul
returns to its rest. This spell can't call the spirits of creatures that are currently undead.

###### ^1^ {#footnote-n}

You must have at least a name the creature was called in life.
