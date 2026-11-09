+++
id = "ref/feat/master-combat-performer"
kind = "feat"
title = "Master Combat Performer"
aon = "FeatDisplay.aspx?ItemName=Master%20Combat%20Performer"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "master_combat_performer", path = "json/feat10.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/performing-combatant", label = "or" },
]
[[sources]]
publication = "ultimate-combat"
page = "109"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Performing Combatant or at least three performance feats, base attack bonus +6."
prerequisite_feats = ["ref/feat/performing-combatant"]
benefit = "You can make performance combat checks as a free action. You are proficient in all weapons with the performance special quality."
+++

## Master Combat Performer (Combat)

You are a master of the techniques and weapons of the arena and the stage.\
**Prerequisites:** [Performing Combatant](ref/feat/performing-combatant) or at least three
performance feats, base attack bonus +6.\
**Benefit:** You can make [performance combat](ref/rule/performance-combat) checks as a free action.
You are proficient in all weapons with the [performance](ref/misc/performance) special quality.
