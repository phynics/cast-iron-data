+++
id = "ref/spell/path-of-glory-greater"
kind = "spell"
title = "Greater Path of Glory"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "path_of_glory_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/path-of-glory" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch (see text)"
effects = [
  { label = "Area", value = "four 5-ft. squares/level (see text)" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Bard, Cleric, Oracle, Skald, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch (see text)
Area: four 5-ft. squares/level (see text)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Subschool: Healing
:::

### Greater Path of Glory

**Sources:** Advanced Class Guide pg 189

This spell functions as [path of glory](ref/spell/path-of-glory), except as noted above, and a
square provides 5 points of healing instead of 1.
