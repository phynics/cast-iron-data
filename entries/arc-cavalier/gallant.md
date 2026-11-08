+++
id = "ref/arc-cavalier/gallant"
kind = "archetype"
title = "Gallant"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gallant", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]

[fields]
kind = "archetype"
replaces = ["Banner", "Greater banner"]
alters = ["The cavalier's order"]
+++

**Sources:** Heroes of the High Court pg 12\
Gallants embody the virtues of honor, generosity, and civility. Their personal symbol serves as an
inspiration to others in a courtly setting as much as on a battlefield.

**Code of Gallantry**

**Alters:** The cavalier's order

**Info:** A gallant must belong to either the
[order of the blue rose](ref/order/order-of-the-blue-rose), the
[order of the guard](ref/order/order-of-the-guard), the
[order of the lion](ref/order/order-of-the-lion), or the
[order of the sword](ref/order/order-of-the-sword). A gallant must also be of lawful good or neutral
good alignment. A gallant who ceases to be lawful good or neutral good, or who violates his order's
edicts, loses all class features except armor and weapon proficiencies until he restores his
alignment or atones for his violation (see the [atonement](ref/spell/atonement) spell), as
appropriate.

**Symbol of Inspiration (Ex)**

**Flavor:** The gallant's personal crest becomes an inspirational symbol of his chivalrous ideals.

**Gained:** At 5th Level

**Passive:** As long as he displays his crest on his tabard, banner, or similar item, allies within
60 feet who can see him gain a morale bonus on saving throws against charm, compulsion, and fear
effects, and a bonus on damage rolls to deal nonlethal damage. Both of these bonuses are equal to
1 + [one-fifth](ref/misc/fractions-and-rounding) of his cavalier level.

**Replaces:** Banner

**Symbol of Resilience (Su)**

**Flavor:** The gallant's personal crest empowers his allies to stand firm against evil.

**Gained:** At 14th Level

**Replaces:** Greater banner

**Standard:** While his personal crest is displayed, the gallant can bolster his allies' resilience.
All allies within 60 feet of the gallant gain DR 5/evil for 1 minute. An ally cannot benefit from
this ability more than once per day.
