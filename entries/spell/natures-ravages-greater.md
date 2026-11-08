+++
id = "ref/spell/natures-ravages-greater"
kind = "spell"
title = "Greater Nature's Ravages"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "natures_ravages_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/natures-ravages" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Witch", level = 7 },
]
casting_time = "10 minute/HD of target"
components = "V, S, M/DF (dried maggots)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "corpse of creature whose total number of HD does not exceed your caster level" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Witch\
8: Cleric, Oracle
Casting time: 10 minute/HD of target
Components: V, S, M/DF (dried maggots)
Range: close (25 ft. + 5 ft./2 levels)
Target: corpse of creature whose total number of HD does not exceed your caster level
Duration: instantaneous
Saving throw: none
Spell resistance: no
:::

## Nature's Ravages

**Sources:** Dungeoneer's Handbook pg 31

You greatly speed up the decomposition process of a nearby corpse and warp the fibers of time that
permeate it, aging the corpse an additional amount of time equal to up to 1 day per 2 caster levels
(maximum 10 days at 20th level). This spell prompts all the natural effects of the intended
decomposition period, including crumbled clothing, rotted or liquefied flesh, maggot infestations,
and the infiltration of any surrounding vegetation.

In addition to hindering mundane autopsies and investigations, this spell may effectively prohibit
the use of [raise dead](ref/spell/raise-dead) on the target, though more powerful magic such as
[resurrection](ref/spell/resurrection) or [true resurrection](ref/spell/true-resurrection) may still
work.

### Greater Nature's Ravages

**Sources:** Dungeoneer's Handbook pg 31

This spell functions like [nature's ravages](ref/spell/natures-ravages), except the target corpse
ages a number of years equal to up to 1 year per caster level (maximum 20 years at 20th level).
