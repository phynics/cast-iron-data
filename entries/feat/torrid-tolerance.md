+++
id = "ref/feat/torrid-tolerance"
kind = "feat"
title = "Torrid Tolerance"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "torrid_tolerance", path = "json/feat16.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/desert-dweller", label = "or" },
  { kind = "prerequisite", target = "ref/feat/jungle-survivalist", label = "or" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "118"

[fields]
kind = "feat"
prerequisites = "Desert Dweller or Jungle Survivalist."
prerequisite_feats = ["ref/feat/desert-dweller", "ref/feat/jungle-survivalist"]
benefit = "You treat [hot environments](ref/rule/heat-dangers) as though they were one step less severe; if you have a similar ability from another feat (like Desert Dweller), the benefits stack and you treat hot conditions as if they were two steps less severe. You do not take a penalty on Constitution checks for wearing armor in hot climates."
+++

You relish hot climates, as the equatorial heat does not sap your strength.\
**Prerequisites:** [Desert Dweller](ref/feat/desert-dweller) or
[Jungle Survivalist](ref/feat/jungle-survivalist).\
**Benefit:** You treat [hot environments](ref/rule/heat-dangers) as though they were one step less
severe; if you have a similar ability from another feat (like Desert Dweller), the benefits stack
and you treat hot conditions as if they were two steps less severe. You do not take a penalty on
Constitution checks for wearing armor in hot climates.
