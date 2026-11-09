+++
id = "ref/rule/rout-phase"
kind = "rule"
title = "Rout Phase"
source_ids = ["pathfinder-59-the-price-of-infamy"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rout_phase", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "pathfinder-59-the-price-of-infamy"
page = "68"

[fields]
kind = "none"
+++

A rout phase occurs after each battle phase. At this point, each surviving squadron must succeed at
a DC 10 morale check by rolling 1d20 and adding its morale check modifier. Failure indicates that
the squadron takes 1d4 points of damage to its morale score. A squadron whose morale score is
reduced to 0 immediately mutinies and is removed from play.

**Fleeing a Battle:** At the end of a rout phase, an admiral can attempt to flee the battle
entirely. When he does so, the other fleet immediately gets one free attack using any one of its
squadrons and can target any one of the fleeing fleet's squadrons. The fleeing admiral makes a
[Profession (sailor)](ref/skill/profession-any) check at a -4 penalty, opposed by the other
admiral's Profession (sailor) check. If the fleeing admiral's check result is higher, his fleet
escapes; otherwise, every squadron in the fleeing admiral's fleet takes 1 point of morale damage and
the battle continues into a new round.
