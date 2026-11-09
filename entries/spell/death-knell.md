+++
id = "ref/spell/death-knell"
kind = "spell"
title = "Death Knell"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_knell", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "264"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous/10 minutes per hd of subject; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin\
2: Cleric, Inquisitor, Oracle, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous/10 minutes per hd of subject; see text
Saving throw: Will negates
Spell resistance: yes
Target: living creature touched
Descriptors: death, evil
:::

You draw forth the ebbing life force of a creature and use it to fuel your own power. Upon casting
this spell, you touch a living creature that has -1 or fewer hit points. If the subject fails its
saving throw, it dies, and you gain 1d8 temporary hit points and a +2 enhancement bonus to Strength.
Additionally, your effective caster level goes up by +1, improving spell effects dependent on caster
level. This increase in effective caster level does not grant you access to more spells. These
effects last for 10 minutes per HD of the subject creature.
