+++
id = "ref/spell/fools-forbiddance"
kind = "spell"
title = "Fool's Forbiddance"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fools_forbiddance", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "224"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Skald", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a ring of keys)"
range = "10 ft."
effects = [
  { label = "Area", value = "10-ft.-radius spherical emanation centered on you" },
]
duration = "concentration"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Bard, Skald\
8: Psychic
Casting time: 1 standard action
Components: V, S, M (a ring of keys)
Range: 10 ft.
Duration: concentration
Saving throw: Will partial
Spell resistance: yes
Area: 10-ft.-radius spherical emanation centered on you
Descriptors: mind-affecting
:::

Through your antics and performance, you create an area of warding that adversely affects all
enemies that dare enter it. When an enemy creature enters the area it must make an immediate Will
saving throw. If it fails, the creature is confused as long as it is in the area and for 1 round
after it leaves. If it succeeds on the saving throw, the creature is staggered as long as it is in
the area and for 1 round after it leaves.
