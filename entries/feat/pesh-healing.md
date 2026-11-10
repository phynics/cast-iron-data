+++
id = "ref/feat/pesh-healing"
kind = "feat"
title = "Pesh Healing"
aon = "FeatDisplay.aspx?ItemName=Pesh%20Healing"
source_ids = ["black-markets", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pesh_healing", path = "json/feat12.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/sahir-afiyun", label = "or" },
]
[[sources]]
publication = "black-markets"
page = "18"
[[sources]]
publication = "dark-markets-a-guide-to-katapesh"
page = "56"

[fields]
kind = "feat"
prerequisites = "Sahir-Afiyun or pesh addict."
prerequisite_feats = ["ref/feat/sahir-afiyun"]
benefit = "When you take a dose of pesh, in addition to its normal initial effect, you gain a number of temporary hit points equal to your total Hit Dice for 1 hour. Temporary hit points gained from additional doses of pesh do not stack."
+++

Consuming pesh makes you feel healthier.\
**Prerequisites:** [Sahir-Afiyun](ref/feat/sahir-afiyun) or [pesh](ref/drug/pesh) addict.\
**Benefit:** When you take a dose of pesh, in addition to its normal initial effect, you gain a
number of [temporary hit points](ref/rule/temporary-hit-points) equal to your total Hit Dice for 1
hour. Temporary hit points gained from additional doses of pesh do not stack.
