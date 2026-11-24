+++
id = "ref/arc-rogue/sniper"
kind = "archetype"
title = "Sniper"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Sniper"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sniper", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "134"

[fields]
kind = "archetype"
features = [
  { anchor = "accuracy", level = 1 },
  { anchor = "deadly-range", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["accuracy"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["deadly-range"] },
]
+++

Some say that the sniper is the worst kind of assassin: a killer who waits silently in the shadows
and then strikes from a distance without remorse. Snipers, of course, understand that such
protestations about "cowardice" and "honor" regarding their profession are in fact merely the
bleatings of sheep fearing the slaughter and pay them no heed. Most snipers take pride in their
formidable abilities, which allow them to take life quickly, quietly, and efficiently, then
disappear into their surroundings without a trace.

## Accuracy (Ex) {#accuracy}

At 1st level, a sniper halves all range increment penalties when making ranged attacks with a bow or
crossbow. This ability replaces trapfinding.

## Deadly Range (Ex) {#deadly-range}

At 3rd level, a sniper increases the range at which she can apply her sneak attack damage by 10
feet. This range increases by 10 feet for every 3 levels after 3rd. This ability replaces trap
sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the sniper archetype: camouflage, snap shot, sniper's eye,
and weapon training\*.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the sniper archetype: defensive roll\*, master of
disguise, and stealthy sniper.
