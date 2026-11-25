+++
id = "ref/arc-slayer/woodland-sniper"
kind = "archetype"
title = "Woodland Sniper"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Woodland%20Sniper"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "woodland_sniper", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "87"

[fields]
kind = "archetype"
features = [
  { anchor = "tree-climber", level = 1 },
  { anchor = "ranged-sneak-attack", level = 3 },
  { anchor = "still-shot", level = 7 },
  { anchor = "branchwalking", level = 11 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["tree-climber"] },
  { replaces = "Stalker", feature = "stalker", by = ["still-shot"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["branchwalking"] },
  { replaces = "slayer's advance", feature = "slayer-s-advance", by = ["branchwalking"] },
  { alters = "Sneak attack", feature = "sneak-attack", by = ["ranged-sneak-attack"] },
]
+++

Woodland snipers are guardians of forest and grove, keeping vigil on their borders and hunting
bounties and trespassers from the shelter of sturdy branches.

## Tree Climber (Ex) {#tree-climber}

A woodland sniper adds half his level to Acrobatics and Climb checks to move between, through, or up
trees. With a successful DC 15 Acrobatics check, he can make ranged attacks with bows while
balancing on branches.

This replaces track.

## Ranged Sneak Attack (Ex) {#ranged-sneak-attack}

At 3rd level, whenever a woodland sniper makes a ranged attack against a creature within 30 feet
that is denied its Dexterity bonus to AC (whether the target actually has a Dexterity bonus or not),
he deals an additional 1d6 points of damage. This damage increases by 1d6 every 3 levels thereafter.
Should the woodland sniper score a critical hit with his ranged attack, this additional damage is
not multiplied. A woodland sniper cannot use sneak attack with a melee attack.

At 6th level and every 3rd level thereafter, the range at which he can make a sneak attack increases
by 10 feet.

This alters sneak attack.

## Still Shot (Ex) {#still-shot}

At 7th level, when he has [cover](ref/rule/cover) provided by one or more trees, the woodland sniper
reduces the penalty on Stealth checks to remain hidden while sniping by half his slayer level.

This replaces stalker.

## Branchwalking (Ex) {#branchwalking}

At 11th level, the woodland sniper gains a climb speed equal to his base speed. In addition, at 13th
level, he can move from one tree to another via connecting branches by adding 5 to the DC of an
Acrobatics or Climb check to move within the canopy. The woodland sniper cannot end his movement on
a branch that cannot support his weight.

This replaces swift tracker and slayer's advance.
