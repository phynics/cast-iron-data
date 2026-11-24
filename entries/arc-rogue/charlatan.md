+++
id = "ref/arc-rogue/charlatan"
kind = "archetype"
title = "Charlatan"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Charlatan"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charlatan", path = "json/archetypes_rogue.json" },
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
  { anchor = "natural-born-liar", level = 1 },
  { anchor = "grand-hoax", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["natural-born-liar"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["grand-hoax"] },
]
+++

A charlatan is a master of lies and deception. Whether creating simple cons or elaborately woven
hoaxes capable of swaying the masses and those in positions of power, a charlatan is often a
purveyor of snake-oil, forgeries, and rumormongering.

## Natural Born Liar (Ex) {#natural-born-liar}

At 1st level, when a charlatan successfully deceives a creature with a Bluff, that creature takes a
-2 penalty on the charlatan's Bluff checks for the next 24 hours. This ability does not stack with
itself. This ability replaces trapfinding.

## Grand Hoax (Ex) {#grand-hoax}

At 3rd level, the charlatan begins to master the art of the grand hoax and learns to create
deceptions designed to bestow harm upon her foes. She gains the
[rumormonger](ref/talent/rumormonger) advanced talent, even though she is not yet 10th level. This
ability takes the place of trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the charlatan archetype: black market connections, coax
information\*, convincing lie, honeyed words\*, and underhanded.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the charlatan archetype: hard to fool, skill
mastery, and unwitting ally.
