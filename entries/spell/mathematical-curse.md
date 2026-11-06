+++
id = "ref/spell/mathematical-curse"
kind = "spell"
title = "Mathematical Curse"
source_ids = ["occult-mysteries"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mathematical_curse", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a full set of 10 fingernails)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Arcanist, Bard, Skald, Sorcerer, Witch, Wizard\
3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (a full set of 10 fingernails)
Range: touch
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Descriptors: curse
:::

**Sources:** Occult Mysteries pg 51

Using the Path of Numbers, you are able to influence the seemingly random elements in the
environment around a creature, reducing that creature's efficacy. Roll 3d8 and choose one of the
dice-this die's result is the penalty mathematical curse imparts. Next, choose either of the two
remaining dice; the d20 roll corresponding to that result on the
[Eight Basic Energies table](ref/rule/mathematical-spellcasting) is the roll the spell's penalty
applies to. The result of the final die represents the number of rounds that mathematical curse
lasts. A creature can be under the influence of only one mathematical curse at a time. If
mathematical curse is cast on a creature already affected by that spell, the new curse replaces the
previous one.
