+++
id = "ref/spell/bards-escape"
kind = "spell"
title = "Bard's Escape"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bards_escape", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (pieces of a smashed fiddle)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "you and up to 1 willing creature/2 caster levels, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Bard, Skald
Casting time: 1 standard action
Components: V, S, M (pieces of a smashed fiddle)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you and up to 1 willing creature/2 caster levels, no two of which can be more than 30 ft. apart
Subschool: Teleportation
:::

**Sources:** Advanced Player's Guide pg 204

You whisk yourself and willing allies out of a tight jam, or instantly transfer yourselves to
another location to achieve greater strategic positioning. You can move any allies within range to
any other space of your choosing within range. Those spaces need not be in line of sight or line of
effect from your original position, but must be open locations on surfaces able to support the
creatures teleported. Except as noted above, this spell otherwise functions as
[dimension door](ref/spell/dimension-door).
