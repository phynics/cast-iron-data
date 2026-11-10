+++
id = "ref/feat/enhanced-coven"
kind = "feat"
title = "Enhanced Coven"
aon = "FeatDisplay.aspx?ItemName=Enhanced%20Coven"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enhanced_coven", path = "json/feat05.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/coven-touched", label = "or" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "13"

[fields]
kind = "feat"
prerequisites = "Changeling, coven hex or Coven-Touched."
prerequisite_feats = ["ref/feat/coven-touched"]
benefit = "Your changeling coven can cast three more spells each day from its list of spell-like abilities. If multiple members of your coven take this feat, the benefits stack."
+++

By deepening your connection with your coven members, you have made your coven capable of casting
more spells each day.\
**Prerequisites:** [Changeling](ref/race/changeling), [coven](ref/hex/coven) hex or
[Coven-Touched](ref/feat/coven-touched).\
**Benefit:** Your changeling coven can cast three more spells each day from its list of
[spell-like abilities](ref/umr/spell-like-abilities). If multiple members of your coven take this
feat, the benefits stack.
