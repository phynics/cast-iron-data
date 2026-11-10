+++
id = "ref/feat/marked-for-glory"
kind = "feat"
title = "Marked for Glory"
aon = "FeatDisplay.aspx?ItemName=Marked%20for%20Glory"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "marked_for_glory", path = "json/feat10.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/great-fortitude", label = "or" },
  { kind = "prerequisite", target = "ref/feat/iron-will", label = "or" },
  { kind = "prerequisite", target = "ref/feat/lightning-reflexes", label = "or" },
]
[[sources]]
publication = "mythic-adventures"
page = "69"

[fields]
kind = "feat"
prerequisites = "Great Fortitude, Iron Will, or Lightning Reflexes."
prerequisite_feats = ["ref/feat/great-fortitude", "ref/feat/iron-will", "ref/feat/lightning-reflexes"]
benefit = "You can use the surge ability once per day (adding 1d6). If you are or become mythic, you can use your surge one additional time per day."
+++

You're destined for glory beyond the ken of ordinary adventurers and mere mortals.\
**Prerequisites:** [Great Fortitude](ref/feat/great-fortitude), [Iron Will](ref/feat/iron-will), or
[Lightning Reflexes](ref/feat/lightning-reflexes).\
**Benefit:** You can use the surge ability once per day (adding 1d6). If you are or become mythic,
you can use your surge one additional time per day.
