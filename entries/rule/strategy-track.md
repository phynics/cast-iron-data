+++
id = "ref/rule/strategy-track"
kind = "rule"
title = "Strategy Track"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "strategy_track", path = "json/rules_campaign_types05.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 239

On the first Melee phase, the commander selects a strategy from one of five options on the strategy
track. Strategies adjust the army's DV, OM, and damage modifier.

Once each Melee phase after the first, the commander can alter the army's strategy. Adjusting the
strategy 1 step up or down does is automatically successful and doesn't require a check. If the
commander wants to adjust strategy more than 1 step, the army attempts a DC 20 Morale check. Success
means the strategy changes to the desired level. Otherwise, the army's current strategy doesn't
change.

|Strategy|DV|OM|Damage|
| --- | --- | --- | --- |
|Defensive|+4|-4|-6|
|Cautious|+2|-2|-3|
|Standard|+0|+0|+0|
|Aggressive|-2|+2|+3|
|Reckless|-4|+4|+6|
