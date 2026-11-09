+++
id = "ref/rule/c-unrest-and-mutiny"
kind = "rule"
title = "Unrest and Mutiny"
source_ids = ["jade-regent-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "c_unrest_and_mutiny", path = "json/rules_campaign_types01.json" },
]
[[sources]]
publication = "jade-regent-players-guide"
page = "24"

[fields]
kind = "none"
+++

On long and arduous journeys such as those faced by the PCs and their caravan, disputes between a
caravan's travelers are unavoidable. As unrest grows, members of the caravan may turn on one
another, question leadership decisions, want to turn back or take a different path, or otherwise
disrupt the caravan. As a result, caravans also have a fifth statistic: Unrest.

Provisions can be purchased in any settlement by buying stores - a single cargo unit of stores
grants 10 units of provisions. Units of provisions can also be gathered by scouts at the rate of 2
per day. They can also be supplied by the spells [goodberry](ref/spell/goodberry),
[create food and water](ref/spell/create-food-and-water), or
[heroes' feast](ref/spell/heroes-feast). A single casting of _[goodberry](ref/spell/goodberry)_
creates 1 unit of provisions. A single casting of
_[create food and water](ref/spell/create-food-and-water)_ generates 3 units of provisions. A single
casting of _[heroes' feast](ref/spell/heroes-feast)_ is enough to generate 1 unit of provisions per
caster level. All provisions magically created in this manner must be consumed on the same day they
are created.

A mutiny can occur whenever a caravan's Unrest score exceeds its Morale score. Whenever this is the
case, the caravan takes a -1 penalty to its AC and on Attack, Security, and Resolve checks for every
point by which Unrest exceeds Morale. In addition, a caravan in mutiny must make a Resolve check (DC
= 20 + the caravan's current Unrest score) each day. If it fails this check, the caravan moves at
half its base speed that day. If the caravan fails this check by 5 or more, the caravan either
refuses to move or moves at half its base speed in a random direction (other than the direction
desired by the PCs) that day.

A caravan can offset its Unrest score by increasing its Morale statistic when it gains a level.
Unrest has no upper limit, but it cannot be reduced below 0.

**Gaining Unrest:** When any of the following events occurs, a caravan must succeed at a Resolve
check (DC = 20 + the caravan's current Unrest score) or gain 1 point of Unrest: a wagon or horse
train is lost (whether it is abandoned or destroyed), a traveler is killed (even if subsequently
brought back to life), the caravan is reduced to 25% of its hit points or fewer, or the caravan
makes no progress during a 12-hour travel day because of an adverse event.

**Reducing Unrest:** A caravan's Unrest score is reduced by 1 whenever the caravan gains a level. In
addition, a caravan can attempt a DC 20 Resolve check with a penalty equal to its current Unrest
score whenever the caravan performs one of the following actions: adding a wagon to the caravan,
adding a wagon improvement, spending a day resting (this does not include days spent making repairs
or otherwise working, nor days spent unable to move because of adverse events or conditions), or
consuming double the caravan's consumption for 1 day. If any of these actions are performed while
camped at a settlement, the caravan gains a +5 bonus on its Resolve check. A success on this check
reduces the caravan's Unrest score by 1 point. A failure results in no change.

In addition, certain situations throughout the Adventure Path may increase or decrease a caravan's
Unrest score.

Giving away 1 cargo unit of trade goods to the caravan crew also reduces Unrest by 1, and giving
away 1 cargo unit of party treasure decreases Unrest by 3. However, buying loyalty in this way has
diminishing returns, requiring 1 additional cargo unit to provide the same reduction in Unrest each
time it is done. Cargo units used in this way are effectively expended, and no longer count toward a
caravan's total cargo capacity.
