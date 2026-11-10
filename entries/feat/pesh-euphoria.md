+++
id = "ref/feat/pesh-euphoria"
kind = "feat"
title = "Pesh Euphoria"
source_ids = ["black-markets", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pesh_euphoria", path = "json/feat12.json" },
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
benefit = "When you take a dose of pesh, in addition to its normal initial effect, you gain a +2 bonus on saves against emotion and fear effects. Once per day, if you fail a saving throw against an emotion or fear effect while you are under the initial effect of pesh, you can attempt another saving throw 1 round later at the same DC."
+++

The calming effects of pesh make you difficult to disturb.\
**Prerequisites:** [Sahir-Afiyun](ref/feat/sahir-afiyun) or [pesh](ref/drug/pesh) addict.\
**Benefit:** When you take a dose of pesh, in addition to its normal initial effect, you gain a +2
bonus on saves against emotion and fear effects. Once per day, if you fail a saving throw against an
emotion or fear effect while you are under the initial effect of pesh, you can attempt another
saving throw 1 round later at the same DC.
