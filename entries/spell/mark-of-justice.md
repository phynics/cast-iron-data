+++
id = "ref/spell/mark-of-justice"
kind = "spell"
title = "Mark of Justice"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mark_of_justice", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent; see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Paladin\
5: Cleric, Inquisitor, Oracle, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, DF
Range: touch
Duration: permanent; see text
Saving throw: none
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

**Sources:** PRPG Core Rulebook pg 312

You mark a subject and state some behavior on the part of the subject that will activate the mark.
When activated, the mark curses the subject. Typically, you designate some sort of undesirable
behavior that activates the mark, but you can pick any act you please. The effect of the mark is
identical with the effect of [bestow curse](ref/spell/bestow-curse).

Since this spell takes 10 minutes to cast and involves writing on the target, you can cast it only
on a creature that is willing or restrained.

Like the effect of bestow curse, a mark of justice cannot be dispelled, but it can be removed with a
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish)
spell. Remove curse works only if its caster level is equal to or higher than your mark of justice
caster level. These restrictions apply regardless of whether the mark has activated.
