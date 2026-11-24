+++
id = "ref/arc-rogue/driver"
kind = "archetype"
title = "Driver"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Driver"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "driver", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-combat"
page = "72"

[fields]
kind = "archetype"
features = [
  { anchor = "hard-drive", level = 1 },
  { anchor = "driver-s-fortitude", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["hard-drive"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["driver-s-fortitude"] },
]
+++

A driver makes her living driving vehicles in the service of those who can pay for her considerable
talents. She may be a wagon-driver practiced at smuggling contraband, an accomplished musher blazing
arctic trails, or a seemingly refined coach driver placing her roguish talents in the service of a
wealthy patron. This archetype works best with the vehicle combat rules in Chapter 4.

## Hard Drive (Ex) {#hard-drive}

When driving a vehicle that uses a group of animals or magical beasts as muscle propulsion, the DCs
of all driving checks are reduced by 2, the maximum speed of the vehicle increases by 10 feet, and
the acceleration increases by 5 feet. This ability takes the place of trapfinding.

## Driver's Fortitude (Ex) {#driver-s-fortitude}

At 3rd level, the driver learns to keep driving and maintain control of her vehicle, even when
mortally wounded. If the driver drops below 0 hit points but is not dead, she can attempt a DC 15
Fortitude save each round to remain conscious and in control of her vehicle, though she may take no
other actions. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the driver archetype: firearm training and getaway artist.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the driver archetype: feat and getaway master.
