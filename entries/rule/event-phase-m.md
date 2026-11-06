+++
id = "ref/rule/event-phase-m"
kind = "rule"
title = "Event Phase"
source_ids = ["lands-of-conflict"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "event_phase_m", path = "json/rules_campaign_types01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Lands of Conflict pg 57

Once all militia actions during the Activity phase are resolved, the GM rolls percentile dice to see
whether any special events occur that week. The percentage chance of an event occurring is equal to
the militia's [Notoriety](ref/rule/notoriety-mt) Score plus any modifiers from previous event phases
or settlement [reputation](ref/rule/reputation-mt) modifiers. During any Event phase following an
uneventful week (a week other than the militia's first week in which no new events occur), add the
militia's [rank](ref/rule/rank-mt) to the chance an event occurs. There is always at least a 10%
chance but never more than a 95% chance of an event occurring. If an event occurs, the GM must roll
percentile dice and consult Table 6-3: Militia Events to see what happens.

When the GM rolls on the Militia Events table, she adds any modifiers from settlements in which the
militia currently operates. Events listed with an asterisk (\*) can become persistent events (see
Persistent Events below). Some negative events have a mitigation listed; these allow officers to
attempt skill checks or other actions to lessen the event's effects. If the GM rolls an event that
can't occur, roll again until the table generates one that makes sense. There is a chance the GM
will need to roll on the table twice and run both events. Getting the same event during a double
roll may have a special effect; such events have a "Twice" subsection in their descriptions. Events
are resolved in the order in which they began; thus, the oldest persistent event is resolved first.

### Table 6-3: Militia Events

|d%|Result|
| --- | --- |
|1-4|Week of Serenity|
|5-12|War Games|
|13-16|Night Ops|
|17-20|Broke the Code|
|21-24|Found Fire|
|25-28|High Morale|
|29-32|Turn Around|
|33-36|Festival|
|37-40|Market Day|
|41-44|Hidden Agenda|
|45-48|All Is Calm|
|49-52|Roll Twice|
|53-56|Calm before the Storm|
|57-60|Turncoat|
|61-64|Cache Discovered|
|65-68|Rivalry|
|69-72|Missing in Action|
|73-76|Theft|
|77-80|Raid|
|81-84|Invasion|
|85-88|Low Morale|
|89-96|Sickness|
|97-99|Double Agent|
|100|Week of Pain|

### Persistent Events

Sometimes, an event becomes persistent. In this case, the event does not go away after 1 week, but
continues to affect the militia week after week. If the PCs can mitigate the event, mitigation lasts
only 1 week, forcing the militia to attempt new mitigations every week. Once every 4 weeks, the PCs
can end a persistent event by spending money equal to twice the militia's current minimum
[treasury](ref/rule/treasury-mt) value. Once this cost is paid, the event ends immediately.
