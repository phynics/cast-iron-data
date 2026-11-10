+++
id = "ref/rule/events"
kind = "rule"
title = "Events"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "events", path = "json/rules_campaign_types05.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "220"

[fields]
kind = "none"
+++

Listed below are unusual events that can happen during a kingdom's Event phase. Most events occur
immediately and are instantaneous or terminate at the end of the Event phase.

Some events impact the whole kingdom, while others are centered on a specific settlement or hex.
Roll on Table 4-7: Event Type and Danger Level to determine the type of event and whether it is
beneficial or harmful. Then roll on the appropriate beneficial or dangerous settlement or kingdom
event table. If this results in an invalid event (such as a pilgrimage when there are no Cathedrals,
Shrines, or Temples in the kingdom), roll again.

**Continuous Events:** A continuous event's effects continue each turn during the Event phase until
you resolve the event (as explained in the event description, usually by succeeding at a kingdom
check).

**Localized Events:** Some events are listed as "settlement" or "hex." The effect of these events
are localized to a single settlement or hex. Randomly select a settlement or hex for the location of
that event. Some events (such as a feud) could be confined to a settlement or start in one
settlement and spread to affect the entire kingdom, depending on whether they're rolled on one of
the Kingdom Events tables or one of the Settlement Events tables.

**Settlement Modifiers:** Some events adjust settlement modifiers (Crime, Lore, etc.). If an event
is localized to 1 settlement, its settlement modifier adjustments apply only to that settlement; if
it's localized to a hex, it affects only settlements in that hex. If the GM is using settlement
modifiers for the entire kingdom (see
[Expanding Settlement Modifiers](ref/rule/expanding-settlement-modifiers)) and the event is not
localized, its adjustments apply to the final modifier for the entire kingdom. For example, the new
subjects event increases Society and Stability for the entire kingdom by 1.

**Hiring Adventurers:** Once per Event phase, you can hire NPC adventurers to help deal with an
event, gaining a bonus on one Economy, Loyalty, or Stability check made as part of that event.
Adventurers of levels 1-2 grant a +2 bonus on the check and cost 4 BP; adventurers of levels 3-5
grant a +5 bonus on the check and cost 8 BP; adventurers of level 6+ (but never higher than your
APL) grant a +10 bonus on the check and cost 16 BP.

### Table 4-7: Event Type and Danger Level

|d%|Event|
| --- | --- |
|01-02|Natural blessing and roll again^[1](ref/rule/events#footnote-1)^|
|03-04|Good weather and roll again^[1](ref/rule/events#footnote-1)^|
|05-25|Beneficial kingdom event (Table 4-8)|
|26-50|Dangerous kingdom event (Table 4-9)|
|51-75|Beneficial settlement event (Table 4-10)|
|76-96|Dangerous settlement event (Table 4-11)|
|97|Bandit activity and roll again^[2](ref/rule/events#footnote-2)^|
|98|Squatters and roll again^[2](ref/rule/events#footnote-2)^|
|99|Monster attack and roll again^[2](ref/rule/events#footnote-2)^|
|100|Vandals and roll again^[2](ref/rule/events#footnote-2)^|

### Table 4-8: Beneficial Kingdom Events

|d%|Event|
| --- | --- |
|01-07|Archaeological find|
|08-12|Diplomatic overture|
|13-20|Discovery|
|21-31|Economic boom|
|32-39|Festive invitation|
|40-53|Food surplus|
|54-66|Good weather|
|67-75|Land rush|
|76-85|Natural blessing|
|86-90|New subjects|
|91-100|Political calm|

### Table 4-9: Dangerous Kingdom Events

|d%|Event|
| --- | --- |
|01-05|Assassination attempt|
|06-18|Bandit activity|
|19-28|Feud|
|29-41|Food shortage|
|42-51|Improvement demand|
|52-59|Inquisition|
|60-64|Large disaster|
|65-76|Monster attack|
|77-84|Plague|
|85-92|Public scandal|
|93-100|Smugglers|

### Table 4-10: Beneficial Settlement Events

|d%|Event|
| --- | --- |
|01-14|Boomtown|
|15-26|Discovery|
|27-40|Justice prevails|
|41-46|Noblesse oblige|
|47-58|Outstanding success|
|59-66|Pilgrimage|
|67-72|Remarkable treasure|
|73-81|Unexpected find|
|82-93|Visiting celebrity|
|94-100|Wealthy immigrant|

### Table 4-11: Dangerous Settlement Events

|d%|Event|
| --- | --- |
|01-10|Building demand|
|11-17|Crop failure|
|18-25|Cult activity|
|26-33|Drug den|
|34-41|Feud|
|42-49|Inquisition|
|50-54|Localized disaster|
|55-61|Monster attack|
|62-66|Plague|
|67-74|Sensational crime|
|75-80|Slavers|
|81-90|Squatters|
|91-100|Vandals|

###### ^1^ {#footnote-1}

If the reroll indicates the same event, ignore the duplicate event and do not reroll again.

###### ^2^ {#footnote-2}

If the reroll indicates the same event, the second event occurs elsewhere in the kingdom.
