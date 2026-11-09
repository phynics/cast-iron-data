+++
id = "ref/feat/ice-climber"
kind = "feat"
title = "Ice Climber"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ice_climber", path = "json/feat08.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/arctic-adaptation", label = "or" },
  { kind = "prerequisite", target = "ref/feat/mountaineer", label = "or" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "113"

[fields]
kind = "feat"
prerequisites = "Arctic Adaptation or Mountaineer; Climb 2 ranks."
prerequisite_feats = ["ref/feat/arctic-adaptation", "ref/feat/mountaineer"]
benefit = "When moving across a slippery surface (including but not limited to icy surfaces), you gain a +5 bonus on Climb checks and on Acrobatics checks to maintain your balance. If you fail a Climb check, you fall only if you fail the check by 10 or more. You also gain a +5 bonus on Perception checks to notice an avalanche and a +2 circumstance bonus on Reflex saves to avoid an avalanche."
+++

You can move or clamber across slippery surfaces with great skill.\
**Prerequisites:** [Arctic Adaptation](ref/feat/arctic-adaptation) or
[Mountaineer](ref/feat/mountaineer); Climb 2 ranks.\
**Benefit:** When moving across a slippery surface (including but not limited to icy surfaces), you
gain a +5 bonus on Climb checks and on Acrobatics checks to maintain your balance. If you fail a
Climb check, you fall only if you fail the check by 10 or more. You also gain a +5 bonus on
Perception checks to notice an [avalanche](ref/rule/avalanches) and a +2 circumstance bonus on
Reflex saves to avoid an avalanche.
