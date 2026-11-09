+++
id = "ref/rule/damaging-a-ship"
kind = "rule"
title = "Damaging a Ship"
source_ids = ["skull-and-shackles-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "damaging_a_ship", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "skull-and-shackles-players-guide"
page = "16"

[fields]
kind = "none"
+++

Ships have hit points and [hardness](ref/umr/hardness) based on their primary components. Most ships
are made of wood (15 hit points per 5-foot-square, hardness 5). When a ship is reduced to below half
its hit points, it gains the broken condition. When it reaches 0 hit points, it gains the sinking
condition.

**Broken Condition:** Ships - and sometimes their means of propulsion - are objects, and like any
other object, when they take damage in excess of half their hit points, they gain the **broken**
condition. When a ship gains the broken condition, it takes a -2 penalty to AC, on sailing checks,
saving throws, and on combat maneuver checks. If a ship or its means of propulsion becomes broken,
the ship's maximum speed is halved and the ship can no longer gain the upper hand until repaired. If
the ship is in motion and traveling faster than its new maximum speed, it automatically decelerates
to its new maximum speed.

**Sinking Condition:** A ship that is reduced to 0 or fewer hit points gains the **sinking**
condition. A sinking ship cannot move or attack, and it sinks completely 10 rounds after it gains
the sinking condition. Each additional hit on a sinking ship that deals more than 25 points of
damage reduces the remaining time for it to sink by 1 round. A ship that sinks completely drops to
the bottom of the body of water and is considered **destroyed.** A destroyed ship cannot be
repaired - it is so significantly damaged it cannot even be used for scrap material. Magic (such as
[make whole](ref/spell/make-whole)) can repair a sinking ship if the ship's hit points are raised
above 0, at which point the ship loses the sinking condition. Generally, nonmagical repairs take too
long to save a ship from sinking once it begins to go down.
