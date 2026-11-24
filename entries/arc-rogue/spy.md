+++
id = "ref/arc-rogue/spy"
kind = "archetype"
title = "Spy"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Spy"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spy", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "135"

[fields]
kind = "archetype"
features = [
  { anchor = "skilled-liar" },
  { anchor = "poison-use", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["skilled-liar"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["poison-use"] },
]
+++

The best spies are like chameleons, but not only can they change their appearances to fit the
situation, they can also change their personalities, allegiances, and even loves if that's what it
takes to achieve their clandestine goals. Spies are the ultimate manipulators, and even those who
commission their services sometimes find that they've merely served the spies' own interests.

## Skilled Liar (Ex) {#skilled-liar}

Whenever a spy uses [Bluff](ref/skill/bluff) to attempt to deceive someone, she gains a bonus on the
opposed roll equal to 1/2 her rogue level (minimum +1). This bonus does not apply to feint attempts
or attempts to pass secret messages. This ability replaces trapfinding.

## Poison Use (Ex) {#poison-use}

At 3rd level, a spy is trained in the use of poison and cannot accidentally poison herself when
applying poison to a blade. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the spy archetype: canny observer, guileful polyglot, honeyed
words, major magic\*, minor magic\*, and quick disguise.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the spy archetype: crippling strike\*, master of
disguise, and stealthy sniper.
