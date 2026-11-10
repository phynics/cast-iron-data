+++
id = "ref/feat/pesh-rejuvenation"
kind = "feat"
title = "Pesh Rejuvenation"
aon = "FeatDisplay.aspx?ItemName=Pesh%20Rejuvenation"
source_ids = ["black-markets", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pesh_rejuvenation", path = "json/feat12.json" },
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
benefit = "If you are brought to 0 or fewer hit points while under the initial effect of pesh, you can end the drug's initial effect as an immediate action. If you do, you gain a number of temporary hit points equal to your Constitution score. These temporary hit points last 1 hour. Upon using this feat, you are sickened for 1d6 hours."
+++

When you are close to death, your body can convert pesh into lifesaving medicine.\
**Prerequisites:** [Sahir-Afiyun](ref/feat/sahir-afiyun) or [pesh](ref/drug/pesh) addict.\
**Benefit:** If you are brought to 0 or fewer hit points while under the initial effect of pesh, you
can end the drug's initial effect as an immediate action. If you do, you gain a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to your Constitution score. These
temporary hit points last 1 hour. Upon using this feat, you are [sickened](ref/misc/sickened) for
1d6 hours.
