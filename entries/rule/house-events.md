+++
id = "ref/rule/house-events"
kind = "rule"
title = "House Events"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "house_events", path = "json/rules_subsystems03.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 119

|d%|Events|
| --- | --- |
|01-10|Buried relic|
|11-35|Roll on the [Inn Events](ref/rule/inn-events) table|
|36-55|Neighbor rivalry|
|56-65|Haunting|
|66-80|Fussy neighbor|
|81-95|Unstable foundation|
|96-100|Arson|

**Arson:** Someone sets your House on fire to send you a message. Treat this as the
[fire generic building event](ref/rule/generic-building-events).

**Buried Relic:** You find an unusual object on your property - a gem, piece of jewelry, or magic
item worth 300 gp or less. There's a 5% chance that the item is cursed or in some way faulty. Each
time you roll this event, the chance of a cursed item increases by 5% (maximum 30% chance).

**Fussy Neighbor:** A highly influential neighbor insists that you remodel some of your House's
rooms. Choose 1d3 random rooms in your House to renovate, and pay an amount of gp equal to 20% of
the cost of those rooms. For every 2 points of Influence you own, the gp cost decreases by 5%; if
this reduces the cost to 0, you don't have to remodel. If you refuse to remodel, you lose 1d4 points
of Influence.

**Haunting:** A supernatural presence enters your home. Roll d%; on a 01-20, the presence is
harmful, on a 21-80, it's mischievous, and on an 81-100 it's helpful. A harmful presence increases
[capital attrition](ref/rule/upkeep-phase) of 1 point of Goods, Influence, Labor, and Magic per
week, and has a 10% chance per night of attacking one overnight guest with a nightmare. A
mischievous presence might bring bad luck (50%) or good luck (50%) to one roll for anyone who sleeps
in your home; bad luck functions as if the subject were affected by the touch of chaos granted power
from the Chaos domain, and good luck functions as if the subject were affected by the
[bit of luck granted power from the Luck domain](ref/domain/luck). A helpful presence must be
appeased once every 7 days with a successful DC 15 Diplomacy check. If you succeed at the check, you
also gain 1 point of Influence or Labor (your choice). If you fail, the presence leaves on its own.
Getting rid of any variety of supernatural presence requires appropriate spells or spending 2d6
points of Magic.

**Neighbor Rivalry:** You have a disagreement with a neighbor. Attempt a DC 15 Diplomacy or
Intimidate check. If you succeed, the event ends. If you fail, you lose 1 point of Influence and
must attempt another check each day, increasing the DC by 2 each time. At any time you can bury the
hatchet and spend Goods or Labor (1 + 1 for each time you failed the check to end this event) to end
the event by doing something nice for the neighbor.

**Unstable Foundation:** The foundation of your House is sinking. The building gains the broken
condition, and you lose 1d2 points of Influence due to the embarrassment. It costs 1d2 points of
Goods and 1d6 points of Labor to bolster the foundation and remove the broken condition.
