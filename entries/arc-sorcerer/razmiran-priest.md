+++
id = "ref/arc-sorcerer/razmiran-priest"
kind = "archetype"
title = "Razmiran Priest"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Razmiran%20Priest"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "razmiran_priest", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "inner-sea-magic"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "false-piety", level = 1 },
  { anchor = "lay-healer", level = 3 },
  { anchor = "razmiran-channel", level = 9 },
]
trades = [
  { replaces = "Eschew Materials bonus feat", feature = "eschew-materials", by = ["false-piety"] },
  { replaces = "Bloodline spells gained at 3rd level and 5th level respectively", feature = "bloodline", levels = [3, 5], power = "bloodline spell", by = ["lay-healer"] },
  { replaces = "Bloodline power gained at 9th level", feature = "bloodline", levels = [9], power = "bloodline power", by = ["razmiran-channel"] },
]
+++

The so-called "priests" of Razmir are magical charlatans—missionary servants of the Living God who
spread his fervent devotion wherever they travel. Altered by Razmir's magic, he can perform feats
impossible for other sorcerers. A Razmiran priest has the following class features.

## False Piety (Ex) {#false-piety}

At 1st level, a Razmiran priest gains Knowledge (religion) and Perform as class skills, but loses
Appraise and Fly as class skills. He adds [half](ref/misc/fractions-and-rounding) his sorcerer level
to Use Magic Device checks to activate spell trigger and spell completion items that use divine
spells. He gains [False Focus](ref/feat/false-focus) as a bonus feat (see page 10). In addition to
replacing Appraise and Fly as class skills, this ability replaces the priest's Eschew Materials
bonus feat.

## Lay Healer (Su) {#lay-healer}

At 3rd level, the Razmiran priest adds _[aid](ref/spell/aid)_ to his list of spells known as a
2nd-level spell. At 5th level, he adds _[remove disease](ref/spell/remove-disease)_ to his list of
spells known as a 3rd-level spell. This ability replaces the bloodline spells gained at 3rd level
and 5th level respectively.

## Razmiran Channel (Su) {#razmiran-channel}

At 9th level, the Razmiran priest can use his own magic to power spell completion and spell trigger
items that use divine spells. He expends a sorcerer spell slot that is at least 1 level higher than
the level of the spell he's trying to activate, then makes a Use Magic Device check. If he succeeds,
the item's spell occurs and the item or charge is not expended. If he fails, nothing happens.
Whether he succeeds or fail, his spell slot is expended. This ability replaces the bloodline power
gained at 9th level.
