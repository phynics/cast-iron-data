+++
id = "ref/rule/identify-magic"
kind = "rule"
title = "Identify Magic"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "identify_magic", path = "json/rules_opt_skills01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 64

By succeeding at a Spellcraft check, you can determine specific types of spells as they're being
cast or while they are in effect. You can also pinpoint magical auras in this manner, or decipher
the magical writing on scrolls without casting [read magic](ref/spell/read-magic).

|Task|Spellcraft DC|
| --- | --- |
|Identify auras while using [detect magic](ref/spell/detect-magic)|15 + spell level|
|Identify properties of a magic item using _[detect magic](ref/spell/detect-magic)_|15 + item's caster level|
|Identify a spell as it is being cast|15 + spell level|
|Decipher a scroll without using _[read magic](ref/spell/read-magic)_|20 + spell level|
|Identify a spell effect that is in place|20 + spell level|
|Identify a spell that just targeted you|25 + spell level|

**Action:** None, in most cases. Deciphering a scroll is a full-round action, and attempting to
identify the properties of a magic item takes 3 rounds per item.

**Try Again:** You can retry checks to identify a spell. When using
_[detect magic](ref/spell/detect-magic)_ and [identify](ref/spell/identify) to learn the properties
of magic items, you can make only one attempt per item per day.

**Perception Penalties:** Attempting to identify a spell as it's being cast incurs the same
penalties as a Perception check due to distance, poor conditions, and other factors.
