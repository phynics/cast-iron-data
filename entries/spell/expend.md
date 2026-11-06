+++
id = "ref/spell/expend"
kind = "spell"
title = "Expend"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "expend", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (miniature broken hourglass)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (miniature broken hourglass)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Area: 20-ft.-radius burst
:::

**Sources:** Advanced Player's Guide pg 220

You cause all creatures in the affected area to use up one or more of their limited-use magical
abilities without any actual effect. A limited-use magical ability is any supernatural or
[spell-like ability](ref/umr/spell-like-abilities) which a creature can only activate a certain
number of times during a set interval (3/day, 1/hour, etc.). The spell does not affect abilities
which the creature can use at will or which are constant. It also does not apply to magical items or
anything else external to a creature. A creature in the spell's area must make a Will saving throw
or expend a single use of one of its abilities. Abilities with the greatest number of uses per day
are affected first; if more than one ability has the same number of uses, randomly determine which
one is affected first. Creatures must continue making Will saves, expending an additional use of an
ability for each failed save, until they succeed, at which point the spell has no further effect.
