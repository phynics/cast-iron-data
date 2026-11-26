+++
id = "ref/arc-bard/songhealer"
kind = "archetype"
title = "Songhealer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Songhealer"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "songhealer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-magic"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "enhance-healing" },
  { anchor = "healing-performance", level = 14 },
  { anchor = "funereal-ballad", level = 20 },
]
trades = [
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["enhance-healing"] },
  { replaces = "Frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["healing-performance"] },
  { replaces = "Deadly performance", feature = "bardic-performance", power = "deadly performance", by = ["funereal-ballad"] },
]
+++

Words can harm, but they also heal. The songhealer brings peace and surcease of pain, calming wild
emotions and providing a balm for the wounded body.

## Enhance Healing (Su) {#enhance-healing}

A number of times per day equal to his Charisma modifier, a songhealer can cause any healing effect
from a spell completion or spell trigger item to function at a caster level equal to his class
level. This ability replaces versatile performance.

## Bardic Performance {#bardic-performance}

A songhealer gains the following type of bardic performance.

## Healing Performance (Su) {#healing-performance}

A bard of 14th level or higher can use his performance to create an effect equivalent to
_[heal](ref/spell/heal)_ on a living target (or _[harm](ref/spell/harm)_ on an undead target), using
the bard's level as the caster level. Using this ability requires 5 rounds of continuous
performance, and the target must be able to see and hear the bard throughout the performance. The
healing performance relies on audible and visual components. This ability replaces frightening tune.

## Funereal Ballad (Su) {#funereal-ballad}

A bard of 20th level or higher can use his performance to create an effect equivalent to
_[resurrection](ref/spell/resurrection)_ on a dead creature, using the bard's level as the caster
level. Using this ability requires 20 rounds of continuous performance, and the target must be
within 10 feet of the bard for the entire performance. Funereal ballad relies on audible and visual
components. This ability replaces deadly performance.
