+++
id = "ref/rule/reputation-mt"
kind = "rule"
title = "Reputation"
source_ids = ["lands-of-conflict"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reputation_mt", path = "json/rules_campaign_types01.json" },
]
[[sources]]
publication = "lands-of-conflict"
page = "50"

[fields]
kind = "none"
+++

**Reputation:** The militia's reputation represents how the militia (and the PCs) are viewed in
different cities - many cities will be indifferent toward it, while others may be friendly,
unfriendly, or even hostile. The effects of each reputation step are presented in Table 6-2 below.
All bonuses are cumulative, as are all penalties. A militia is considered to be operating out of any
settlement in which it is taking actions during the [Activity phase](ref/rule/activity-phase-m). The
players and GM should keep track of any settlements in which the militia operates and record its
reputation there, as well as whether those settlements are secured by an enemy organization. A
secured settlement is a town with any fortifications, such as a barracks or a training facility,
that a rival organization uses. How to remove such fortifications from a settlement is up to the GM.

The [Reduce Danger](ref/rule/reduce-danger) action can improve the PCs' reputation in a secured
settlement; otherwise, changes in reputation are at the GM's discretion.

### Table 6-2: Reputation

|Reputation|Advantages and Disadvantages|
| --- | --- |
|Hostile|The militia is disliked. If the PCs or militia team members are seen here publicly, the citizens inform the local authorities of their presence in 1d4 days. Any items purchased here cost 5% more than normal. The DCs of Bluff, Diplomacy, and Intimidate checks in a hostile settlement increase by 5. (This is cumulative with the base DCs for [Diplomacy](ref/skill/diplomacy) checks to influence an NPC's attitude.)|
|Unfriendly|People are unhelpful and don't easily trust the PCs or others in their militia. The DCs for Bluff, Diplomacy, and Intimidate checks increase by 2. (This is cumulative with the base DCs for Diplomacy checks to influence an NPC's attitude.) If the militia is operating out of an unfriendly settlement, the GM adds 5 to the result when rolling to determine whether an event occurs during the [Event phase](ref/rule/event-phase-m).|
|Indifferent|None.|
|Friendly|The militia has a benevolent reputation in this settlement, and the DCs of any Bluff, Diplomacy, and Intimidate checks attempted here decrease by 2. If the militia is operating out of a friendly settlement, during the Event phase, the GM subtracts 5 from the percentile roll to determine whether an event occurs.|
|Helpful|The PCs' militia is very well known and most people here agree with its ideals. Any items purchased here cost 5% less than normal. During the [Activity phase](ref/rule/activity-phase-m), while the militia is operating out of a helpful settlement, the PCs can add a +2 bonus to one Loyalty, Secrecy, or Security check.|
