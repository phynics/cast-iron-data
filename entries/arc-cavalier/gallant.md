+++
id = "ref/arc-cavalier/gallant"
kind = "archetype"
title = "Gallant"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Gallant"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gallant", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "code-of-gallantry", level = 1 },
  { anchor = "symbol-of-inspiration", level = 5 },
  { anchor = "symbol-of-resilience", level = 14 },
]
trades = [
  { replaces = "Banner", feature = "banner", by = ["symbol-of-inspiration"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["symbol-of-resilience"] },
  { alters = "The cavalier's order", feature = "order", by = ["code-of-gallantry"] },
]
+++

Gallants embody the virtues of honor, generosity, and civility. Their personal symbol serves as an
inspiration to others in a courtly setting as much as on a battlefield.

## Code of Gallantry {#code-of-gallantry}

A gallant must belong to either the [order of the blue rose](ref/order/order-of-the-blue-rose), the
[order of the guard](ref/order/order-of-the-guard), the
[order of the lion](ref/order/order-of-the-lion), or the
[order of the sword](ref/order/order-of-the-sword). A gallant must also be of lawful good or neutral
good alignment. A gallant who ceases to be lawful good or neutral good, or who violates his order's
edicts, loses all class features except armor and weapon proficiencies until he restores his
alignment or atones for his violation (see the _[atonement](ref/spell/atonement)_ spell), as
appropriate.

This alters the cavalier's order.

## Symbol of Inspiration (Ex) {#symbol-of-inspiration}

At 5th level, the gallant's personal crest becomes an inspirational symbol of his chivalrous ideals.
As long as he displays his crest on his tabard, banner, or similar item, allies within 60 feet who
can see him gain a +2 morale bonus on saving throws against charm, compulsion, and fear effects, and
a +2 bonus on damage rolls to deal nonlethal damage. At 10th level and every 5 cavalier levels
thereafter, these bonuses increase by 1.

This ability replaces banner.

## Symbol of Resilience (Su) {#symbol-of-resilience}

At 14th level, the gallant's personal crest empowers his allies to stand firm against evil. While
his personal crest is displayed, the gallant can bolster his allies' resilience as a standard
action. All allies within 60 feet of the gallant gain DR 5/evil for 1 minute. An ally cannot benefit
from this ability more than once per day.

This ability replaces greater banner.
