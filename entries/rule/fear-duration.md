+++
id = "ref/rule/fear-duration"
kind = "rule"
title = "Fear Duration"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fear_duration", path = "json/rules_campaign_types02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Adventures pg 10

Using this system can make the tracking of your overall fear level a bit more complicated. Track
each fear effect separately, evaluating your current fear level whenever an effect is added or
removed, starting with the most severe effect and adding levels on top of that for each new effect.
Remember that lesser fear effects cannot add up to a greater fear effect, regardless of their
number, and the staggered condition that can result from being scared and then suffering another
lesser fear effect applies at the moment when the new fear effect begins (not when it expires).

For example, Ezren becomes subject to an effect that causes him to be shaken for 1 minute and
another that causes him to be panicked for 1 round. On the 1st round, his fear increases to
panicked. On the following 9 rounds, he is shaken. If, on the 3rd round, he becomes spooked for 1
minute, he becomes scared for 7 rounds (the overlap between the spooked condition and the remaining
rounds of the shaken condition), then spooked for 3 rounds.
