+++
id = "ref/rule/ss-fire"
kind = "rule"
title = "Fire"
source_ids = ["skull-and-shackles-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ss_fire", path = "json/rules_campaign_types10.json" },
]

[fields]
kind = "none"
+++

**Sources:** Skull and Shackles Player's Guide pg 16\
Fire is an ever-present danger on every wooden ship, but while most ships are not in danger of going
up in flames from a dropped torch or lantern, alchemical or magical fires can be much more
dangerous. Note that many instantaneous fire spells do not automatically catch a ship on fire, but
those that deal fire damage over multiple rounds have a better chance of causing a fire on board a
ship (see [Magic](ref/rule/ss-magic)).

When a ship takes fire damage (such as from [alchemist's fire](ref/eq-weapon/alchemists-fire),
flaming arrows, certain spells, and other effects at the GM's discretion), it must immediately make
a Fortitude save (DC 10 + damage dealt) or catch fire. Unless an attack specifically targets a
ship's means of propulsion (such as sails), it is assumed that such attacks affect the structure of
a ship itself.

Once a ship has caught fire, it automatically takes 2d6 points of fire damage per round (ignoring
[hardness](ref/umr/hardness)) as the fire spreads. The ship's crew can attempt to extinguish the
flames as a full-round action for the entire crew, allowing the ship to make a Reflex save (DC 15 +
the number of rounds the ship has been on fire). A successful saving throw means the fire has been
put out. A failed saving throw results in the ship taking the normal 2d6 points of fire damage for
the round.

A ship must take the ["uncontrolled" action](ref/rule/ss-movement) each round that its crew attempts
to put out a fire, as they are not sailing the ship at this time.

Those who would like more detailed rules for fires, spreading flames, and fighting fires can use the
[Fire](ref/rule/fire) system presented in the [Catastrophes](ref/rule/catastrophes) section.
