+++
id = "ref/arc-barbarian/elemental-kin"
kind = "archetype"
title = "Elemental Kin"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Elemental%20Kin"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_kin", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-players-guide"
page = "78"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-fury", level = 3 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["elemental-fury"] },
]
+++

Some barbarian tribes have strong ties to the elemental forces of nature. Their shamans anoint the
warriors at birth, tying them to the patron element of the tribe and granting them lasting boons
against such forces. An elemental kin has the following class feature.

## Elemental Fury (Ex) {#elemental-fury}

At 3rd level, whenever the elemental kin takes an amount of energy damage equal to or greater than
her barbarian level while raging, she adds 1 to the total number of rounds that she can rage that
day. At 6th level, and every three levels thereafter, the number of extra rounds per energy attack
increases by +1, to a maximum of +6 rounds per energy attack at 18th level. This ability replaces
trap sense.

## Rage Powers {#rage-powers}

The following rage powers complement the elemental kin archetype:
[elemental rage](ref/ragepower/elemental-rage),
[energy absorption](ref/ragepower/energy-absorption),
[energy eruption](ref/ragepower/energy-eruption),
[energy resistance](ref/ragepower/energy-resistance),
[greater elemental rage](ref/ragepower/greater-elemental-rage),
[greater energy resistance](ref/ragepower/greater-energy-resistance), and
[lesser elemental rage](ref/ragepower/lesser-elemental-rage).
