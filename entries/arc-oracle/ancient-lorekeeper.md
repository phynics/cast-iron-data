+++
id = "ref/arc-oracle/ancient-lorekeeper"
kind = "archetype"
title = "Ancient Lorekeeper"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Ancient%20Lorekeeper"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ancient_lorekeeper", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-race-guide"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "elven-arcana", level = 2 },
]
trades = [
  { replaces = "Bonus skills the ancient lorekeeper gains from her mystery", feature = "mystery", power = "class skills" },
  { replaces = "Bonus spells she would normally gain at these levels from her chosen mystery", feature = "mystery", levels = [4, 6, 8, 10, 12, 14, 16, 18], power = "bonus spells", by = ["elven-arcana"] },
]
+++

The ancient lorekeeper is a repository for all the beliefs and vast knowledge of an
[elven](ref/race/elf) people. She shows a strong interest in and understanding of histories and
creation legends at a young age, and as she matures her calling to serve as the memory of her
long-lived people becomes clear to all who know her. An ancient lorekeeper has the following class
features.

## Class Skills {#class-skills}

An ancient lorekeeper adds Knowledge (arcane) and Knowledge (local) to her list of class skills.
Whenever she makes a Knowledge check of any kind about a question regarding elves (creatures of the
elf subtype), the ancient lorekeeper adds half her class level on her check. This replaces the bonus
skills the ancient lorekeeper gains from her mystery.

## Elven Arcana (Ex) {#elven-arcana}

At 2nd level, an ancient lorekeeper's mastery of elven legends and philosophy has allowed her to
master one spell used by elven wizards. She selects one spell from the sorcerer/wizard spell list
that is at least one level lower than the highest-level oracle spell she can cast. The ancient
lorekeeper gains this as a bonus spell known. The spell is treated as one level higher than its true
level for all purposes. The ancient lorekeeper may choose an additional spell at 4th, 6th, 8th,
10th, 12th, 14th, 16th, and 18th levels. This ability replaces the bonus spells she would normally
gain at these levels from her chosen mystery.

## Mysteries {#mysteries}

The following oracle mysteries complement the ancient lorekeeper archetype:
[Lore](ref/mystery/lore), [Nature](ref/mystery/nature), [Waves](ref/mystery/waves),
[Wind](ref/mystery/wind) (_Advanced Player's Guide_); [Ancestor](ref/mystery/ancestor),
[Time](ref/mystery/time), [Wood](ref/mystery/wood) (_Ultimate Magic_).
