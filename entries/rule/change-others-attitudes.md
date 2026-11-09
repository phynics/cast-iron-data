+++
id = "ref/rule/change-others-attitudes"
kind = "rule"
title = "Change Others' Attitudes"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "change_others_attitudes", path = "json/rules_opt_skills01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "58"

[fields]
kind = "none"
+++

You can use Influence to change the attitudes of NPCs. The DC is determined by the target's starting
attitude plus its Charisma modifier. If you succeed, you improve the target's attitude toward you by
one step, plus one more step if you beat the DC by 5 or more. You can't shift an attitude by more
than two steps with a single check. If you fail by 4 or less, the target's attitude is unchanged,
and if you fail by 5 or more, the target's attitude decreases by one step. An attitude shift
typically lasts 1d4 hours. You can use Influence to make a request of a creature whose attitude
toward you is indifferent or better.

You can't change the attitude of a creature that doesn't understand you or that has an Intelligence
score of 3 or lower. This function of Influence is generally ineffective in combat.

|Starting Attitude|Influence DC|
| --- | --- |
|Hostile|25 + target's Cha modifier|
|Unfriendly|20 + target's Cha modifier|
|Indifferent|15 + target's Cha modifier|
|Friendly|10 + target's Cha modifier|
|Helpful|0 + target's Cha modifier|

**Action:** 1 minute of continuous interaction.

**Try Again:** You can't attempt to change a creature's attitude more than once per 24-hour period.
