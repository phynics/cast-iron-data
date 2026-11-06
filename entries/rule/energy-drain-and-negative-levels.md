+++
id = "ref/rule/energy-drain-and-negative-levels"
kind = "rule"
title = "Energy Drain and Negative Levels"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "energy_drain_and_negative_levels", path = "json/rules_combat01.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 562

Some spells and a number of undead creatures have the ability to drain away life and energy; this
dreadful attack results in "negative levels." These cause a character to take a number of penalties.

For each negative level a creature has, it takes a cumulative -1 penalty on all ability checks,
attack rolls, combat maneuver checks, Combat Maneuver Defense, saving throws, and skill checks. In
addition, the creature reduces its current and total hit points by 5 for each negative level it
possesses. The creature is also treated as one level lower for the purpose of level-dependent
variables (such as spellcasting) for each negative level possessed. Spellcasters do not lose any
prepared spells or slots as a result of negative levels. If a creature's negative levels equal or
exceed its total Hit Dice, it dies.

A creature with temporary negative levels receives a new saving throw to remove the negative level
each day. The DC of this save is the same as the effect that caused the negative levels.

Some abilities and spells (such as [raise dead](ref/spell/raise-dead)) bestow permanent level drain
on a creature. These are treated just like temporary negative levels, but they do not allow a new
save each day to remove them. Level drain can be removed through spells like
[restoration](ref/spell/restoration). Permanent negative levels remain after a dead creature is
restored to life. A creature whose permanent negative levels equal its Hit Dice cannot be brought
back to life through spells like _[raise dead](ref/spell/raise-dead)_ and
[resurrection](ref/spell/resurrection) without also receiving a restoration spell, cast the round
after it is restored to life.
