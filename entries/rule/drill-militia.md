+++
id = "ref/rule/drill-militia"
kind = "rule"
title = "Drill Militia"
source_ids = ["lands-of-conflict"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drill_militia", path = "json/rules_campaign_types01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Lands of Conflict pg 55

**Drill Militia** **(No Team Required):** This check can be made only once per Activity phase. By
spending an amount of gold equal to the militia's minimum [treasury](ref/rule/treasury-mt) value,
the PCs can attempt to increase their militia's [training](ref/rule/training-mt) score. To do so,
they must attempt a Loyalty check. The DC of this check is equal to 10 + the militia's
[rank](ref/rule/rank-mt). On a success, increase the militia's training score by 2d6 + any bonuses
granted by Commandant [officers](ref/rule/officers). If they roll a natural 1, the check doesn't
automatically fail, but the militia's Notoriety score increases by 1d6. The militia can't take this
action if it is at its current maximum rank.
