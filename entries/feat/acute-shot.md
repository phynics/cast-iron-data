+++
id = "ref/feat/acute-shot"
kind = "feat"
title = "Acute Shot"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acute_shot", path = "json/feat01.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "5"

[fields]
kind = "feat"
prerequisites = "Far Shot, Precise Shot."
prerequisite_feats = ["ref/feat/far-shot", "ref/feat/precise-shot"]
benefit = "Whenever you gain a magic bonus on an attack roll with a ranged weapon, you can deduct any range penalties from your damage roll, instead of your attack roll."
+++

When magic aids your ranged attacks, you rarely miss.\
**Prerequisites:** [Far Shot](ref/feat/far-shot), [Precise Shot](ref/feat/precise-shot).\
**Benefit:** Whenever you gain a magic bonus on an attack roll with a ranged weapon, you can deduct
any range penalties from your damage roll, instead of your attack roll.

Additionally, when you gain a magic bonus on a ranged attack roll, you can deal
[sneak attack](ref/ability/sneak-attack) damage to a target that has
[concealment](ref/rule/concealment) (but not total concealment) as long as the attack otherwise
qualifies to deal sneak attack damage. The maximum number of sneak attack dice you can use in this
way is equal to the value of your magic bonus on attack rolls.
