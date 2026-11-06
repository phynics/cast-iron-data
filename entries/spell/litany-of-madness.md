+++
id = "ref/spell/litany-of-madness"
kind = "spell"
title = "Litany of Madness"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_madness", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Inquisitor", level = 6 },
]
casting_time = "1 swift action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 or more rounds (see below)"
saving_throw = "no, see below"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Antipaladin\
6: Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 or more rounds (see below)
Saving throw: no, see below
Spell resistance: yes
Target: one creature
Subschool: Charm
Descriptors: language-dependant, mind-affecting
:::

**Sources:** Ultimate Combat pg 234

This litany is a sermon of madness. The target is confused. At the start of each of its turns, it
can make a Will saving throw against the confused effect (DC of the spell). If the target fails the
save, it continues to be confused. If it makes the save, the effect ends.

While subject to this spell, the target cannot be the target of another spell that has the word
"litany" in the title.
