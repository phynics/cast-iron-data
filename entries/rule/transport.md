+++
id = "ref/rule/transport"
kind = "rule"
title = "Transport"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transport", path = "json/rules_rulesets01.json" },
]
[[sources]]
publication = "black-markets"
page = "11"

[fields]
kind = "none"
+++

You dispatch a team to move specific items, people, or capital from one place or organization to
another. The team becomes unavailable for the duration of the trip (minimum 1 day). At the end of
its journey, a successful downtime activity check by the assigned team (DC = 5 + days traveled)
means their goods arrived safely and intact. On a failure, the team is robbed or skims off the top,
losing half the cargo's value. If its check fails by 5 or more, the team breaks up or goes rogue,
and you lose both the team and the valuables it was transporting.
