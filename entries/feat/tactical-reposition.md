+++
id = "ref/feat/tactical-reposition"
kind = "feat"
title = "Tactical Reposition"
aon = "FeatDisplay.aspx?ItemName=Tactical%20Reposition"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tactical_reposition", path = "json/feat15.json" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "8"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Int 13, Combat Expertise, Improved Reposition."
prerequisite_feats = ["ref/feat/combat-expertise", "ref/feat/improved-reposition"]
benefit = "When making a reposition combat maneuver, you can move an enemy into a trap or other hazardous area, such as a pit, wall scythe, or blade barrier. When you do so, the moved enemy is treated as though it had activated the trap or triggered the hazard, and it takes a -2 penalty to AC and on saving throws to mitigate the trap or hazard's effects."
normal = "You cannot reposition a foe into an intrinsically dangerous space such as a pit or *blade barrier."
+++

## Tactical Reposition (Combat)

You excel at moving foes right where you want them.\
**Prerequisites:** Int 13, [Combat Expertise](ref/feat/combat-expertise),
[Improved Reposition](ref/feat/improved-reposition).\
**Benefit:** When making a [reposition](ref/rule/reposition) combat maneuver, you can move an enemy
into a trap or other hazardous area, such as a [pit](ref/trap/pit-trap),
[wall scythe](ref/trap/wall-scythe-trap), or [blade barrier](ref/spell/blade-barrier). When you do
so, the moved enemy is treated as though it had activated the trap or triggered the hazard, and it
takes a -2 penalty to AC and on saving throws to mitigate the trap or hazard's effects.\
**Normal:** You cannot reposition a foe into an intrinsically dangerous space such as a pit or
_[blade barrier](ref/spell/blade-barrier)._
