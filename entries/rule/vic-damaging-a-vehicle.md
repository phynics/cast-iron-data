+++
id = "ref/rule/vic-damaging-a-vehicle"
kind = "rule"
title = "Damaging and Repairing a Vehicle"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vic_damaging_a_vehicle", path = "json/rules_rulesets02.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "174"

[fields]
kind = "none"
+++

### Damaging a Vehicle

Vehicles have hit points and [hardness](ref/umr/hardness) based on their primary components. Most
vehicles are made of wood. Heavier construction materials are possible, but they at least double the
number of squares of propulsion a vehicle requires. Materials like stone or heavy metals quadruple
the number of squares of propulsion needed.

A vehicle has a total number of hit points equal to its base material hit point value times its
vehicle's number of squares (see Table 4-4). When it is reduced to below half hit points, it becomes
broken. When it reaches 0 hit points, it becomes wrecked. When it reaches negative hit points equal
to its number of squares, it is destroyed - it is so damaged it cannot even be used for scrap
material.

### Table 4-4: Vehicle Hit Points by Material

|Material|hp|Hardness|
| --- | --- | --- |
|Leather|10|0|
|Wood|15|5|
|Stone|20|8|
|Metal|20|10|
|Magically treated|×2|×2|

> **Broken Condition:** Vehicles, and sometimes their methods of propulsion, are objects, and like
> any other object, when they take damage in excess of half their hit points, they gain the broken
> condition. When a vehicle gains the broken condition, it takes a -2 penalty to AC, on saving
> throws, and on combat maneuver checks, and the DC to drive the vehicle increases by 2. If a
> vehicle or its means of propulsion becomes broken, both the maximum speed and the acceleration of
> the vehicle are halved until repaired. If the vehicle is in motion, and is traveling faster than
> its new maximum speed, it automatically decelerates to its new maximum speed.
>
> **Wrecked Condition:** A vehicle gains the wrecked condition if its hit points are reduced to 0 or
> fewer. A wrecked vehicle cannot be driven and gains the sinking condition (if in the water) or
> falls (if in the air). An air vehicle that begins to fall does so at a rate of half its maximum
> speed each round.
>
> If a means of propulsion is reduced to 0 or fewer hit points, it does not gain the wrecked
> condition. It is instead destroyed.
>
> **Sinking:** A water vehicle that is reduced to 0 or fewer hit points or a vehicle that is not
> seaworthy that is plunged into water gains the sinking condition. For a water vehicle, this
> condition ends when a vehicle is brought to 1 or more hit points, but other vehicles must be
> removed from the water. A sinking ship fully sinks and is destroyed 10 rounds after gaining the
> sinking condition. Each additional hit on a sinking ship reduces the remaining time for it to sink
> by 1 round. Alternatively, when a water vehicle is reduced to a negative number of hit points
> equal to its number of squares, it sinks immediately.
>
> **Destroyed:** A vehicle is destroyed when it is reduced to a number of negative hit points equal
> to its number of squares. A destroyed vehicle cannot be repaired, and is nothing more than junk.
>
> If a vehicle's means of propulsion is an object, it is destroyed when it reaches 0 hit points.
>
> If either the means of propulsion or the vehicle is destroyed, it comes to a sudden stop if it is
> not stopped already. Water vehicles sink and drop to the bottom of the body of water. Air vehicles
> fall.

### Repairing a Vehicle

The fastest and easiest way to repair a vehicle is with the [mending](ref/spell/mending) and
[make whole](ref/spell/make-whole) spells, but more mundane methods can also be used. Craft
(carpentry) can be used to repair most vehicles made of wood; because of their specialized
construction, water vehicles require Craft (ships) to repair. Depending on the nature of the damage,
such skills like Craft (cloth), Craft (alchemy), Knowledge (engineering), and even various
professions can be used to repair vehicles, if the GM approves. In general, a day's worth of work by
a single person using the appropriate skill to repair a vehicle requires 10 gp of raw material and a
DC 10 skill check, and repairs 10 points of damage on a success, or 5 hit points on a failure.
