+++
id = "ref/rule/mercenary-company-events"
kind = "rule"
title = "Mercenary Company Events"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mercenary_company_events", path = "json/rules_subsystems03.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 128

|d%|Events|
| --- | --- |
|01-15|Impressive results|
|16-25|Windfall|
|26-50|Brawl|
|51-70|Rivalry|
|71-80|Scandal|
|81-85|Duel|
|86-95|Schism|
|96-100|Mutiny|

**Brawl:** This functions like the [bar brawl in Tavern Events](ref/rule/tavern-events), except you
may attempt a Profession (soldier) check instead of an Intimidate check, and a failed check causes a
loss of Influence and Labor.

**Duel:** This functions like the
[duel event from the Military Academy Events section](ref/rule/military-academy-events), except you
may attempt a Profession (soldier) check instead of a Diplomacy or Intimidate check.

**Impressive Results:** Your mercenaries perform admirably, eliminating a problem quickly or
defeating a more powerful opponent with ease. You gain 1d4 points of Influence and 1d2 points of
Labor, and for 1d6 days the organization gains a +10 bonus on its first check to generate capital
each day.

**Mutiny:** A member tries to take over the group, either by challenging you to a fight or by an
underhanded method like attacking you while you sleep. You may handle this as a combat encounter or
attempt a DC 25 Bluff, Intimidate, or Profession (soldier) check. If you succeed, the instigator
leaves and you lose 1 point of Labor but gain 1d2 points of Influence. If you fail, you lose control
of the Mercenary Company as if from [business attrition](ref/rule/upkeep-phase).

**Rivalry:** Another mercenary group is stealing jobs from your organization. Treat this as the
[rivalry event from Generic Building Events](ref/rule/generic-building-events)), except you can also
end the rivalry and gain 1d4 points of Influence by beating the leader in a duel (as the
[duel Military Academy event](ref/rule/military-academy-events), but not necessarily to the death).

**Scandal:** Some sort of scandal strikes your company - a member is accused of murder or one of
your teams injures locals in a bar fight. For 2d4 days you lose 1d2 points of Influence each day and
the organization takes a -5 penalty on checks to generate capital. Once per day, you can attempt to
repair the damage to your reputation and end the event with a DC 20 Bluff or Diplomacy check.
Failure extends the duration of the scandal's fallout by another 1d4 days.

**Schism:** This functions as the [schism from the Cult Events section](ref/rule/cult-events),
except that the skills you can use to attempt to end it are Bluff, Diplomacy, Intimidate, and
Profession (soldier), and that succeeding at the check means you lose 1 point of Labor and the event
ends.

**Windfall:** Your organization is rewarded handsomely for its recent efforts, either with payment
from a grateful employer or rich spoils from looting an enemy. You gain 1d10 × 10 gp, 1d6 points of
Goods, and 1 point of Magic.
