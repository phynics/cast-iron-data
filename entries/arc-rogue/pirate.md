+++
id = "ref/arc-rogue/pirate"
kind = "archetype"
title = "Pirate"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Pirate"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pirate", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-combat"
page = "73"

[fields]
kind = "archetype"
features = [
  { anchor = "sea-legs", level = 1 },
  { anchor = "swinging-reposition", level = 2 },
  { anchor = "unflinching", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["sea-legs"] },
  { replaces = "2nd-level rogue talent", feature = "rogue-talents", levels = [2], by = ["swinging-reposition"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["unflinching"] },
]
+++

A pirate breaks from the confines of country and king to commit her crimes upon the high seas. She
holds allegiance only to her ship and its captain (if even that much is true), and lives a lawless
life upon the waves, plundering ships and shorelines as suits her whim.

## Sea Legs (Ex) {#sea-legs}

At 1st level, a pirate becomes adept at moving on ships, boats, and similar vessels. She gains the
[Sea Legs](ref/feat/sea-legs) feat (page 117) as a bonus feat, even if she does not meet the
prerequisites. This ability replaces trapfinding.

## Swinging Reposition (Ex) {#swinging-reposition}

At 2nd level, a pirate incorporates a ship's masts, rigging, ropes, sails, and other such structures
into her combat style. Provided she is wearing light armor or no armor, when fighting in an
environment where such structures exist, the rogue incorporates them into her movement, and does not
have to move in a straight line when making either a [charge](ref/rule/charge) attack or a
[bull rush](ref/rule/bull-rush) combat maneuver. Once she completes her attack or maneuver, she can
reposition herself. Immediately after making the charge or bull rush, she can move 5 feet as a free
action, even if the charge ends her turn. This movement does not provoke attacks of opportunity.
This ability replaces the 2nd-level rogue talent.

## Unflinching (Ex) {#unflinching}

Pirates are a salty and steadfast lot. At 3rd level, a pirate gains a +1 bonus on saving throws
against fear and mind-affecting effects. This bonus increases by +1 for every three levels, to a
maximum of +6 at 18th level. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the pirate archetype: black market connections, combat trick,
finesse rogue, firearm training, hold breath, rope master, and strong stroke.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the pirate archetype: getaway master, hard to fool,
and unwitting ally.
