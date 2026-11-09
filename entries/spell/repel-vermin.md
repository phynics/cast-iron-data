+++
id = "ref/spell/repel-vermin"
kind = "spell"
title = "Repel Vermin"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "repel_vermin", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "333"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["pain"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "10 ft."
effects = [
  { label = "Area", value = "10-ft.-radius emanation centered on you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none or Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Hunter, Ranger\
4: Bard, Cleric, Druid, Oracle, Shaman, Skald, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 10 ft.
Duration: 10 minutes/level (D)
Saving throw: none or Will negates; see text
Spell resistance: yes
Area: 10-ft.-radius emanation centered on you
Descriptors: pain
:::

An invisible barrier holds back vermin. A vermin with HD of less than one-third your level cannot
penetrate the barrier.

A vermin with HD of one-third your level or more can penetrate the barrier if it succeeds on a Will
save. Even so, crossing the barrier deals the vermin 2d6 points of damage, and pressing against the
barrier causes pain, which deters most vermin.
