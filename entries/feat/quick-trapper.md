+++
id = "ref/feat/quick-trapper"
kind = "feat"
title = "Quick Trapper"
source_ids = ["pathfinder-116-fangs-of-war"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "quick_trapper", path = "json/feat12.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/learn-ranger-trap", label = "or" },
]
[[sources]]
publication = "pathfinder-116-fangs-of-war"
page = "67"

[fields]
kind = "feat"
prerequisites = "Learn Ranger Trap or trap class feature, Survival 5 ranks."
prerequisite_feats = ["ref/feat/learn-ranger-trap"]
benefit = "When setting a ranger trap, you can do so as a standard action rather than a full-round action. If you do so, the trap DC is reduced by 5."
+++

Your trap-making proficiency improves greatly.\
**Prerequisites:** [Learn Ranger Trap](ref/feat/learn-ranger-trap) or trap class feature, Survival 5
ranks.\
**Benefit:** When setting a ranger trap, you can do so as a standard action rather than a full-round
action. If you do so, the trap DC is reduced by 5.
