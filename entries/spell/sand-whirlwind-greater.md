+++
id = "ref/spell/sand-whirlwind-greater"
kind = "spell"
title = "Greater Sand Whirlwind"
source_ids = ["taldor-echoes-of-glory"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sand_whirlwind_greater", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/sand-whirlwind" },
]
[[sources]]
publication = "taldor-echoes-of-glory"
page = "25"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of sand, dust, or fine powder)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "10-ft.-radius spread" },
]
duration = "1 round/level"
saving_throw = "Will negates (blinding only)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (a handful of sand, dust, or fine powder)
Range: medium (100 ft. + 10 ft./level)
Area: 10-ft.-radius spread
Duration: 1 round/level
Saving throw: Will negates (blinding only)
Spell resistance: no
Subschool: Creation
:::

### Greater Sand Whirlwind

This spell functions as [sand whirlwind](ref/spell/sand-whirlwind) except as noted above.
