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

## Sand Whirlwind

**Sources:** Taldor, Echoes of Glory pg 25

A whirling cloud of sand strikes the target, blinding it and hampering its ability to speak. To
speak while affected by the spell, the target must make a [concentration](ref/rule/concentration)
check (DC equal to the DC of this spell). If the target tries to cast a spell, the Concentration DC
increases by the level of the spell being cast. A successful Will save negates the blindness but not
the speechhampering effect.

### Greater Sand Whirlwind

**Sources:** Taldor, Echoes of Glory pg 25

This spell functions as [sand whirlwind](ref/spell/sand-whirlwind) except as noted above.
