+++
id = "ref/spell/hobbling-bomb-admixture"
kind = "spell"
title = "Hobbling Bomb Admixture"
source_ids = ["pathfinder-117-assault-on-longshadow"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hobbling_bomb_admixture", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Investigator", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Investigator
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Pathfinder \#117: Assault on Longshadow pg 76

> _[Hobgoblin](ref/race/hobgoblin) alchemists devoted to [Hadregash](ref/faith/hadregash) have
> developed the following extract to empower themselves and their allies or to make prey easier to
> catch and enslave._

Upon drinking an extract created with this formula, you make a significant change to your magical
reserve that modifies the nature of all bombs you create and throw during this extract's duration.
This effect on your magical reserve has no effect on any discoveries that you use to modify your
bombs, but you can have only one admixture effect (formula with the words "bomb admixture" in its
title) active at a time. If you drink another bomb admixture, the effects of the former bomb
admixture end and the new one becomes active.

When you throw a bomb and hit a target directly, it affects up to three targets - the creature the
bomb hit directly, and up to two other creatures that take damage from the splash damage
(alchemist's choice). Each targeted creature must succeed at a Fortitude saving throw or have its
speed reduced by 20 feet (minimum 0 feet).
