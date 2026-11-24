+++
id = "ref/arc-bard/sound-striker"
kind = "archetype"
title = "Sound Striker"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Sound%20Striker"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sound_striker", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]

[fields]
kind = "archetype"
trades = [
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence" },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion" },
]
+++

**Source** Ultimate Magic pg. 27

They say that words can cut deeper than any blade, and the sound striker proves this true. Using
music and words as a weapon, he can focus his performances into a deadly delivery.

**Bardic Performance**

**Info:** A sound striker gains the following types of bardic performance. Neither performance can
be performed more quickly than a standard action.

**Wordstrike (Su)**

**Gained:** At 3rd Level

**Replaces:** Inspire competence

**Standard:** The sound striker bard can spend 1 round of bardic performance to direct a burst of
sonically charged words at a creature or object. This performance deals 1d4 points of damage plus
the bard's level to an object, or half this damage to a living creature.

**Weird Words (Su)**

**At 6th Level:** A sound striker can start a performance as a **standard action**, lashing out with
1 potent sound per bard level (maximum 10), each sound affecting one target within 30 feet. These
are ranged touch attacks. Each weird word deals 1d8 points of damage plus the bard's Charisma bonus
(Fortitude half), and the bard chooses whether it deals bludgeoning, piercing, or slashing damage
for each word.

**Replaces:** Suggestion
