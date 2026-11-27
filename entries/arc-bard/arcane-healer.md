+++
id = "ref/arc-bard/arcane-healer"
kind = "archetype"
title = "Arcane Healer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Arcane%20Healer"
source_ids = ["faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_healer", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "faiths-and-philosophies"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "channel-energy", level = 2 },
  { anchor = "inspiring-healing", level = 5 },
]
trades = [
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["channel-energy"] },
  { replaces = "Loremaster", feature = "lore-master", by = ["inspiring-healing"] },
]
+++

Thought bards may have different reasons for wanting to heal the sick and injured, both out of pure
altruism and in order to keep adventuring companions safe, the ability to heal also makes it much
easier for a bard to pose as a cleric or other divine healer, opening the door for a wide array of
swindles and scams.

## Channel Energy (Su) {#channel-energy}

At 2nd level, an arcane healer gains the ability to
[channel positive energy](ref/ability/channel-energy) as a cleric of one level lower than his level.
If a creature within the channeled energy's area of effect would be allowed a save against its
effects, the DC is equal to 10 + 1/2 the arcane healer's level + the arcane healer's Charisma
modifier. An arcane healer can use this ability once per day at 2nd level, gaining an additional use
per day every four levels thereafter (6th, 10th, 14th, and 18th), to a maximum of 5 times per day at
18th level. This ability replaces versatile performance.

## Inspiring Healing (Sp) {#inspiring-healing}

At 5th level, an arcane healer gains the ability to expend rounds of his bardic performance to
provide extra healing to his allies. By expending 2 rounds of bardic performance, an arcane healer
can cast [cure light wounds](ref/spell/cure-light-wounds) as a
[spell-like ability](ref/umr/spell-like-abilities). At 11th level, the arcane healer can expend 2
rounds of bardic performance to cast [cure moderate wounds](ref/spell/cure-moderate-wounds) as a
[spell-like ability](ref/umr/spell-like-abilities). At 17th level, he may instead expend 2 rounds of
bardic performance to cast [cure serious wounds](ref/spell/cure-serious-wounds) as a
[spell-like ability](ref/umr/spell-like-abilities). No single target may be affected by an arcane
healer's inspiring healing ability more than once in a 24-hour period. This ability replaces
loremaster.
