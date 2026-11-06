+++
id = "ref/spell/true-appraisal"
kind = "spell"
title = "True Appraisal"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_appraisal", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, F (gold coin)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "8 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Bard, Cleric, Inquisitor, Occultist, Oracle, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, F (gold coin)
Range: personal
Duration: 8 hours
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Inner Sea Temples pg 33

You gain temporary insight into the value of objects. You gain a +5 competence bonus on Appraise
checks, can attempt an Appraise check to determine an object's value as a move action, and can take
10 on an Appraise check even if stress or distractions would normally prevent you from doing so. You
know if you fail an Appraise check, and you never determine a wildly inaccurate price.
