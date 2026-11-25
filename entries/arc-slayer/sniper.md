+++
id = "ref/arc-slayer/sniper"
kind = "archetype"
title = "Sniper"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Sniper"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sniper", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "120"

[fields]
kind = "archetype"
features = [
  { anchor = "accuracy", level = 1 },
  { anchor = "deadly-sniper", level = 2 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["accuracy"] },
]
+++

Whether it's with a bullet from a sling, a quarrel from a crossbow, or even an expertly thrown
dagger, the sniper ensures that a single shot disables his targets.

## Accuracy (Ex) {#accuracy}

At 1st level, a sniper halves all range increment penalties when making ranged attacks with a bow,
crossbow, or firearm. This ability replaces track.

## Deadly Sniper (Ex) {#deadly-sniper}

At 2nd level, when the sniper makes an attack against a target who is within his weapon's first
range increment and completely unaware of his presence, that attack ignores the 30 foot range limit
on ranged sneak attacks, and if it is a sneak attack, he adds his sniper level as a bonus on his
sneak attack damage roll. After this first attack, the target is aware of the sniper's presence.

## Slayer Talents {#slayer-talents}

The following slayer talents (and rogue talents) complement the sniper archetype: camouflage, snap
shot, sniper's eye, and weapon training.

## Advanced Slayer Talents {#advanced-slayer-talents}

The following advanced slayer talents (which are also available to rogues) complement the sniper
archetype: deadly sneak, master of disguise, and stealthy sniper.
