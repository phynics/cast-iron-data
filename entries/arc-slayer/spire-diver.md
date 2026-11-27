+++
id = "ref/arc-slayer/spire-diver"
kind = "archetype"
title = "Spire Diver"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Spire%20Diver"
source_ids = ["pathfinder-124-city-in-the-deep"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spire_diver", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "pathfinder-124-city-in-the-deep"
page = "80"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-target", level = 1 },
  { anchor = "hold-breath", level = 1 },
  { anchor = "slayer-talents" },
  { anchor = "swift-swimmer", level = 11 },
  { anchor = "diver-s-advance", level = 13 },
  { anchor = "diver-s-quarry", level = 14 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["hold-breath"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["swift-swimmer"] },
  { replaces = "Slayer's advance", feature = "slayer-s-advance", by = ["diver-s-advance"] },
  { alters = "Studied target", feature = "studied-target", by = ["studied-target"] },
  { alters = "stalker", feature = "stalker", by = ["studied-target"] },
  { alters = "Quarry", feature = "quarry", by = ["diver-s-quarry"] },
  { alters = "improved quarry", feature = "improved-quarry", by = ["diver-s-quarry"] },
]
+++

Peerless divers, assassins, and scouts, spire divers operate in and out of water using the same
weapons and equipment. Although the elves of the Mordant Spire originally developed the techniques
that spire divers use, people living in coastal areas and archipelagos near the Mwangi Expanse and
Tian Xia have similar, independently developed warrior and diving traditions.

## Studied Target (Ex) {#studied-target}

A spire diver does not gain the ability to add her studied target bonus on Bluff and Survival checks
against an opponent she has studied. At 7th level, she cannot add her studied target bonus on
Disguise checks. Instead, when using any bow or crossbow against her studied target underwater, the
spire diver ignores the normal penalty for shooting underwater and instead treats the weapon as
though its range increment were 10 feet. At 5th, 10th, 15th, and 20th levels, the range increment
increases by 10 feet, to a maximum of 50 feet.

When using a bow or crossbow that already has an underwater range increment, such as an underwater
crossbow (_Pathfinder RPG Ultimate Equipment_ 39–40), the spire diver adds the range increment
gained from studied target as a bonus to the weapon's usual underwater range increment, though the
combined range increment cannot exceed the weapon's normal range increment.

This alters studied target and stalker.

## Hold Breath (Ex) {#hold-breath}

A spire diver increases the number of rounds she can [hold her breath](ref/misc/hold-your-breath)
before she is required to start attempting Constitution checks to avoid drowning by 2 per slayer
level she has.

This replaces track.

## Slayer Talents {#slayer-talents}

A spire diver can select the [strong stroke](ref/talent/strong-stroke) rogue talent as a slayer
talent.

## Swift Swimmer (Ex) {#swift-swimmer}

At 11th level, a spire diver gains a swim speed equal to her base speed.

This replaces swift tracker.

## Diver's Advance (Ex) {#diver-s-advance}

At 13th level, a spire diver can swim up to twice her swim speed once per day as a move action. She
can use Stealth as part of this movement but takes a -10 penalty on her check for doing so. At 17th
level, she can use this ability twice per day.

This replaces slayer's advance.

## Diver's Quarry (Ex) {#diver-s-quarry}

A spire diver gains quarry and improved quarry as a normal slayer, but she does not gain the ability
to take 10 or take 20 on Survival checks while moving at normal speed without penalty. Instead, at
14th level, a spire diver can take 10 on Knowledge checks to identify a monster she has selected as
her quarry. At 19th level, she can take 20 on these checks without spending extra time to do so. The
spire diver must be trained in the appropriate Knowledge skill to use this ability.

This alters quarry and improved quarry.
