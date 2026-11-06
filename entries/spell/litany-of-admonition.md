+++
id = "ref/spell/litany-of-admonition"
kind = "spell"
title = "Litany of Admonition"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_admonition", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["language-dependant"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Paladin", level = 3 },
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
School: necromancy
Level: 3: Antipaladin, Paladin\
4: Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: language-dependant
:::

**Sources:** Disciple's Doctrine pg 13

You point out your target's faults and failures, staggering the target for 1 round. While subject to
this spell, the target cannot be the target of another spell that has the word "litany" in the
title.
