+++
id = "ref/rule/shop-events"
kind = "rule"
title = "Shop Events"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shop_events", path = "json/rules_subsystems03.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 123

|d%|Events|
| --- | --- |
|01-30|Busy day|
|31-45|Slow day|
|46-60|Shoplifter|
|61-75|Embezzler|
|76-90|Burglary|
|91-95|Protection racket|
|96-100|Robbery|

**Burglary:** Thieves have attempted to break into your Shop to steal your items. You can
immediately spend 1d6 points of Influence to negate this attempt. Otherwise, attempt a DC 25
Intimidate or Perception check. On a success, your building's defenses work, the thieves are caught,
and you gain 1d2 points of Influence. On a failure, you lose 1d4 points of Goods. The GM may allow
you to pursue or track down the thieves as an adventure hook.

**Busy Day:** For whatever reason, your Shop is particularly busy today. If you spend the day at the
Shop helping customers, the building gains a +10 bonus on its next check to generate capital.

**Embezzler:** One of your employees is skimming your profits. You can attempt a DC 25 Perception or
Sense Motive check to catch the employee in the act. If you catch and fire the employee, you lose 1
point of Labor. If you don't catch the employee, you lose 1 point of Influence and the building's
next check to generate capital takes a -10 penalty. The dishonest employee waits 1d6 days before
acting again. You can attempt a new Perception or Sense Motive check each time the embezzler acts,
with the DC decreasing by 1 each time until you catch the employee as he becomes more brazen. If for
some reason you catch the employee and don't fire him, he waits 2d6 days to embezzle again unless
you somehow force him to stop.

**Protection Racket:** Thugs attempt to extort money from your Shop for "protection." You can pay
their demand (an amount equal to the building's maximum possible gp earned in a day) or attempt to
scare them off with a DC 25 Intimidate check. If you fail to run them off, they steal an amount of
merchandise and cash equal to twice their initial demand plus 1d4 points of Goods.

**Robbery:** Someone has targeted your store or employees for a quick robbery. There is a 75% chance
this is just a crime of opportunity and a 25% chance that this is a planned attack on your Shop.
Treat the event as the criminal activity event from
[Generic Building Events](ref/rule/generic-building-events); if it is a planned attack, increase the
Influence needed to prevent the attack to 2d6, the Intimidate DC to 25, and the cost of the robbery
to 2d6 points of Goods.

**Shoplifter:** A customer tries to walk out of your Shop with a valuable item. Attempt a DC 20
Perception check. If you fail, you lose 1d3 points of Goods.

**Slow Day:** For some reason, no one's coming to the Shop today. If you don't spend the day at the
Shop, it earns no capital for the day.
