+++
id = "ref/spell/scribes-binding"
kind = "spell"
title = "Scribe's Binding"
source_ids = ["spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scribes_binding", path = "json/spells15.json" },
]
[[sources]]
publication = "spymasters-handbook"
page = "29"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Occultist", level = 6 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, F (a book bound in precious metals and treated with rare oils, worth 1,000 gp per HD of the target)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Occultist\
9: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a book bound in precious metals and treated with rare oils, worth 1,000 gp per HD of the target)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Subschool: Polymorph
:::

Hermea's benevolent Council of Enlightenment uses this spell to humanely preserve their society's
greatest minds from the ravages of time, though it has seen far more sinister employment when put to
use by other organizations that have since discovered its utility. This spell binds a single
creature into a prepared book, sustaining it in suspended animation and filling the book with its
experience and knowledge. The tome weighs 10 pounds and has one page for every day of the subject's
life. The cover and binding transform to reflect the subject's appearance, interests, and tastes.
Every thought and memory - including those the target may have forgotten long ago - are perfectly
transcribed within the enchanted pages, penned in excruciating detail in the language that the
creature was thinking or speaking in when the event occurred. If a memory includes dialogue in a
language the subject didn't understand, that dialogue is reproduced phonetically, and must be
translated by a reader who knows that language. Any alterations to a subject's memories - such as by
a [modify memory](ref/spell/modify-memory) spell - appear in a subtly different script; a successful
DC 35 Linguistics check is needed to identify this.

Spells that modify or remove text - such as [erase](ref/spell/erase) or
[secret page](ref/spell/secret-page) - also affect the target's memory if they persist after its
release. _[Modify memory](ref/spell/modify-memory)_ can be used to repair any changes to its
original state, or alter the accounts recorded within the book. A creature imprisoned by scribe's
binding automatically fails any saving throws against effects to change or modify its memories.

A target bound by this spell can be freed by only [freedom](ref/spell/freedom),
[miracle](ref/spell/miracle), or [wish](ref/spell/wish).
[Polymorph any object](ref/spell/polymorph-any-object) restores the target's normal form for 24
hours. Scribe's binding makes the imprisoning tome supernaturally durable
([hardness](ref/umr/hardness) 20, 10 hp per HD the imprisoned creature had). Destroying the tome
immediately slays the creature imprisoned within.
