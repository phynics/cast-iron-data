+++
id = "ref/arc-alchemist/deep-bomber"
kind = "archetype"
title = "Deep Bomber"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Deep%20Bomber"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deep_bomber", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "advanced-race-guide"
page = "205"

[fields]
kind = "archetype"
features = [
  { anchor = "silent-bomb", level = 2 },
  { anchor = "targeting-bomb", level = 3 },
  { anchor = "stonekin", level = 6 },
]
trades = [
  { replaces = "Poison use", feature = "poison-use", by = ["silent-bomb"] },
  { replaces = "Instant alchemy", feature = "instant-alchemy", by = ["targeting-bomb"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["stonekin"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["targeting-bomb"] },
]
+++

Consumed with keeping hidden from the horrors below the surface, svirfneblin use their proclivity
for alchemy and talent for obfuscation to strike from the darkness and retreat unseen. A deep bomber
has the following class features.

## Silent Bomb {#silent-bomb}

At 2nd level, when the deep bomber creates a bomb, he can choose to have it explode without making
any noise, although those damaged by it may cry out. This ability replaces poison use.

## Targeting Bomb\* {#targeting-bomb}

At 3rd level, when the deep bomber creates a bomb, he can choose to have its detonation include a
_[faerie fire](ref/spell/faerie-fire)_ effect that applies to all creatures within the splash radius
(including the target, if any). This ability replaces swift alchemy (the deep bomber gains swift
alchemy at 18th level and never gains instant alchemy).

## Stonekin {#stonekin}

At 6th level, the deep bomber automatically learns _[tree shape](ref/spell/tree-shape)_ as a
2nd-level extract, except instead of a tree, he takes the form of a stalagmite that is the same size
as his current size. At 7th level, he automatically learns
_[meld into stone](ref/spell/meld-into-stone)_ as a 3rd-level extract. This ability replaces swift
poisoning.

## Discoveries {#discoveries}

The following discoveries complement the deep bomber archetype:
[delayed bomb](ref/discovery/delayed-bomb), [dispelling bomb](ref/discovery/dispelling-bomb),
[fast bombs](ref/discovery/fast-bombs), [infusion](ref/discovery/infusion),
[madness bomb](ref/discovery/madness-bomb), [poison bomb](ref/discovery/poison-bomb).
