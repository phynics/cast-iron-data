+++
id = "ref/arc-bard/disciple-of-the-forked-tongue"
kind = "archetype"
title = "Disciple of the Forked Tongue"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Disciple%20of%20the%20Forked%20Tongue"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disciple_of_the_forked_tongue", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "potions-and-poisons"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "discordant-spiral", level = 1 },
  { anchor = "venomous-whispers", level = 9 },
  { anchor = "serpent-of-the-mind", level = 2 },
]
trades = [
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["discordant-spiral"] },
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["venomous-whispers"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["serpent-of-the-mind"] },
]
+++

Studied in venomous words as well as venomous blood, a disciple of the forked tongue knows just the
right phrase to slowly poison the soul. His voice can sink deep into his victims' hearts, destroying
friendships and devouring the mind. The disciple of the forked tongue is an archetype of the bard
class available to vishkanya characters.

## Bardic Performance {#bardic-performance}

A disciple of the forked tongue gains the following bardic performances.

## Discordant Spiral (Su) {#discordant-spiral}

The disciple can disrupt the thought processes of enemies who hear his performance, causing them to
take a -1 penalty on saves against mind-affecting and
[curse](ref/carried/bestiary/rules/universal-monster-rules/curse) effects and a -2 penalty on
[concentration](ref/rule/concentration) checks. These penalties increase by 1 at 5th level and every
6 levels thereafter.

This replaces inspire courage.

## Venomous Whispers (Su) {#venomous-whispers}

At 9th level, a disciple of the forked tongue can use his performance to sow distrust into the mind
of an enemy within 30 feet. An affected creature treats its allies as hostile for the purposes of
their spells and abilities—it is never considered a willing target of spells and must attempt saving
throws against them when possible, and it gains no benefit from allied bardic performances and other
abilities that specifically target allies. For every 3 levels a disciple of the forked tongue has
beyond 9th, he can target one additional enemy while using this performance (up to a maximum of four
at 18th level).

This replaces inspire greatness.

## Serpent of the Mind (Su) {#serpent-of-the-mind}

A disciple of the forked tongue can add one spell with the
[curse](ref/carried/bestiary/rules/universal-monster-rules/curse) descriptor from the spell list of
any spellcasting class to his list of spells known at 2nd level and every 4 levels thereafter.

This replaces versatile performance.
