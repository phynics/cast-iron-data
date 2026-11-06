+++
id = "ref/spell/litany-of-thunder"
kind = "spell"
title = "Litany of Thunder"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_thunder", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["language-dependant", "sonic"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Inquisitor", level = 5 },
  { class = "Paladin", level = 4 },
]
casting_time = "1 swift action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Antipaladin, Paladin\
5: Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: language-dependant, sonic
:::

**Sources:** Ultimate Combat pg 235

You call down a thunderous boom upon your enemy. The target becomes deafened until the condition is
removed, and is confused for 1 round.

While subject to this spell, the target cannot be the target of another spell that has the word
"litany" in the title.
