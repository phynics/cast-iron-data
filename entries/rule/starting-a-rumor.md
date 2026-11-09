+++
id = "ref/rule/starting-a-rumor"
kind = "rule"
title = "Starting a Rumor"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "starting_a_rumor", path = "json/rules_adv_pc01.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "14"

[fields]
kind = "none"
+++

Planting a rumor requires carefully spreading and cultivating it. A PC can plant a rumor in a
settlement by spending 1 week (or 1d4 days if the settlement is smaller than a town) and succeeding
at a Propaganda check. This check can be a [Bluff](ref/skill/bluff),
[Diplomacy](ref/skill/diplomacy), or [Perform](ref/skill/perform-any) (act, oratory, or sing) check,
or another skill check at the GM's discretion (see
[Spreading Propaganda](ref/rule/alternate-goals)). The base DC of a Propaganda check is 15. If a
true rumor is particularly believable or unbelievable, the DC may decrease by up to 5 or increase by
up to 20, respectively. If a rumor is false, the PC must succeed at an additional Bluff check to
avoid being caught in a lie, applying plausibility modifiers as normal. If a PC fails that Bluff
check by 5 or more, she takes a -4 penalty on all Bluff and Diplomacy checks she attempts in the
settlement for 1d4 weeks.

Because rumors are difficult to plant in large settlements, PCs should apply the modifier based on
settlement size listed in the table below to all Propaganda checks as well as to Bluff checks to
avoid being caught in a lie. In a large settlement, such as a city, a PC can instead plant a rumor
in a single district. In this case, use the modifier for a settlement with approximately the same
population as the district. If the GM is using
[settlement modifiers](ref/rule/settlement-modifiers), the settlement's Lore modifier applies to
Propaganda checks and the settlement's Corruption modifier applies to Bluff checks to avoid being
caught in a lie.

|Settlement Type|Propaganda and Bluff Check DC Modifier|
| --- | --- |
|Village or smaller|+0|
|Small town|+3|
|Large town|+5|
|Small city|+10|
|Large city|+15|
|Metropolis|+20|

Multiple characters can work together to plant a rumor. Choose one character to attempt the
Propaganda check. Each character who wishes to assist can attempt a separate skill check whose DC is
10 less than the Propaganda check's DC. A character who knows that the rumor is false must also
succeed at a DC 15 Bluff check. Each character who successfully assists provides a +2 bonus (up to a
maximum bonus equal to 4 + the settlement's Propaganda modifier). A character with a class feature,
feat, or other ability that grants her followers gains a +5 bonus on Propaganda checks and checks to
assist in spreading rumors.

If a PC succeeds at the Propaganda check (and the Bluff check, if necessary), her rumor takes hold
as an obscure rumor. If she exceeds the Propaganda check's DC by 5 or more, the rumor is more
prevalent, as indicated on the table below. A character with the
[rumormonger](ref/talent/rumormonger) advanced rogue talent creates a common rumor if she succeeds
at the Propaganda check, and a widely known rumor if she succeeds by 5 or more. Anyone who gathers
information related to a rumor learns the rumor if she succeeds at a Diplomacy check at the listed
DC.

|Propaganda Check Result|Rumor Prevalence|Diplomacy DC to Learn|
| --- | --- | --- |
|Success by less than 5|Obscure rumor|25|
|Success by 5 or more|Recurring rumor|20|
|Success by 10 or more|Common rumor|15|
|Success by 15 or more|Widely known rumor|10|
