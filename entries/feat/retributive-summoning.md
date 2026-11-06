+++
id = "ref/feat/retributive-summoning"
kind = "feat"
title = "Retributive Summoning"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "retributive_summoning", path = "json/feat13.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/spell-focus", label = "or" },
]

[fields]
kind = "feat"
prerequisites = "Spell Focus (conjuration) or counter summons class feature."
prerequisite_feats = ["ref/feat/spell-focus"]
+++

**Sources:** Plane-Hopper's Handbook pg 6

Your training in counterspelling summons is so extensive that you can redirect some of your foes'
power to call forth your own allies.\
**Prerequisites:** [Spell Focus](ref/feat/spell-focus) (conjuration) or counter summons class
feature.

When you successfully [counter](ref/rule/counterspells) a summoning spell with
[dispel magic](ref/spell/dispel-magic) or your own [summon monster](ref/spell/summon-monster) spell,
you can immediately summon nonevil creatures as if you had just finished casting a summon monster
spell of 2 levels lower than the countered summoning spell.
