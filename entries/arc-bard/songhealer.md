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
replaces = ["Versatile performance", "Frightening tune", "Deadly performance"]
replaces_features = ["versatile-performance"]
+++

Words can harm, but they also heal. The songhealer brings peace and surcease of pain, calming wild
emotions and providing a balm for the wounded body.

**Enhance Healing (Su)**

**Ability:** A songhealer can cause any healing effect from a spell completion or spell trigger item
to function at a caster level equal to his class level.

**Replaces:** Versatile performance

**Usage:** Cha modifier times/day

**Bardic Performance**

**Info:** A songhealer gains the following type of bardic performance.

**Healing Performance (Su)**

**Ability:** A songhealer can use his performance to create an effect equivalent to
[heal](ref/spell/heal) on a living target (or [harm](ref/spell/harm) on an undead target), using the
bard's level as the caster level. Using this ability requires 5 rounds of continuous performance,
and the target must be able to see and hear the bard throughout the performance.

**Gained:** At 14th Level

**Replaces:** Frightening tune

**Special:** The _healing performance_ relies on audible and visual components.

**Funereal Ballad (Su)**

**Ability:** A songhealer can use his performance to create an effect equivalent to
[resurrection](ref/spell/resurrection) on a dead creature, using the bard's level as the caster
level. Using this ability requires 20 rounds of continuous performance, and the target must be
within 10 feet of the bard for the entire performance.

**Gained:** At 20th Level

**Replaces:** Deadly performance

**Special:** _Funereal ballad_ relies on audible and visual components.
