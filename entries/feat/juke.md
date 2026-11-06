+++
id = "ref/feat/juke"
kind = "feat"
title = "Juke"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "juke", path = "json/feat09.json" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Dex 13, Dodge, Mobility, Sidestep."
prerequisite_feats = ["ref/feat/dodge", "ref/feat/mobility", "ref/feat/sidestep"]
benefit = "When an opponent charges you, you gain a +4 dodge bonus to your AC. If the charger's attack roll misses you and his movement ends while he is adjacent to you, you can switch places with the opponent as an immediate action, and he is considered to be flanked by you until the end of your next turn. You can't use the benefits of Juke if you ready an action to set a weapon with the brace special quality against a charging foe."
+++

## Juke (Combat)

**Sources:** Melee Tactics Toolbox pg 15

You can avoid a charge, leaving your opponent vulnerable to attacks by you or your allies.\
**Prerequisites:** Dex 13, [Dodge](ref/feat/dodge), [Mobility](ref/feat/mobility),
[Sidestep](ref/feat/sidestep).\
**Benefit:** When an opponent [charges](ref/rule/charge) you, you gain a +4 dodge bonus to your AC.
If the charger's attack roll misses you and his movement ends while he is adjacent to you, you can
switch places with the opponent as an immediate action, and he is considered to be
[flanked](ref/rule/flanking) by you until the end of your next turn. You can't use the benefits of
Juke if you [ready an action](ref/rule/ready) to set a weapon with the [brace](ref/misc/brace)
special quality against a charging foe.
