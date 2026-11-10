+++
id = "ref/spell/hymn-of-peace"
kind = "spell"
title = "Hymn of Peace"
source_ids = ["champions-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hymn_of_peace", path = "json/spells5.json" },
]
[[sources]]
publication = "champions-of-purity"
page = "29"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Skald", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "40 ft."
effects = [
  { label = "Area", value = "40-ft.-radius burst centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Bard, Skald\
7: Cleric, Oracle
Casting time: 1 standard action
Components: V, S
Range: 40 ft.
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: 40-ft.-radius burst centered on you
Descriptors: good
:::

Each time a subject of this spell attempts to attack another creature or object, or otherwise
perform an aggressive or damaging action toward a creature or object, it must attempt a Will save.
If the save succeeds, the subject can attack normally. If the save fails, the subject cannot follow
through with the attack and loses that part of its action. Creatures not taking violent actions are
unaffected by this spell.
