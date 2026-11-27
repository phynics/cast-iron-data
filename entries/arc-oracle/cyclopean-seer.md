+++
id = "ref/arc-oracle/cyclopean-seer"
kind = "archetype"
title = "Cyclopean Seer"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Cyclopean%20Seer"
source_ids = ["inner-sea-monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cyclopean_seer", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "inner-sea-monster-codex"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "oracle-s-curse" },
  { anchor = "assume-fate", level = 1 },
  { anchor = "brutal-trance", level = 7 },
  { anchor = "doomsaying" },
  { anchor = "flash-of-insight" },
  { anchor = "prescience", level = 1 },
  { anchor = "final-revelation", level = 20 },
]
trades = [
  { replaces = "The additional class skills granted by her mystery", feature = "mystery", power = "class skills" },
  { replaces = "Revelation gained at 1st level", feature = "revelation", levels = [1], by = ["assume-fate"] },
  { replaces = "Revelation gained at 7th level", feature = "revelation", levels = [7], by = ["brutal-trance"] },
  { replaces = "The final revelation of the oracle's mystery", feature = "final-revelation", by = ["final-revelation"] },
  { alters = "Bonus spells granted by the oracle's mystery", feature = "mystery", power = "bonus spells" },
  { alters = "Revelations", feature = "revelation", by = ["prescience"] },
]
+++

A cyclopean seer draws power from the mysterious prophetic abilities of ancient giants.

## Recommended Mysteries {#recommended-mysteries}

Ancestor (_Pathfinder RPG Ultimate Magic_ 53), lore, nature, occult (_Pathfinder Campaign Setting:
Occult Mysteries_ 53), time (_Ultimate Magic_ 56).

## Class Skills {#class-skills}

A cyclopean seer adds Linguistics and all Knowledge skills to her list of class skills. These
replace the additional class skills granted by her mystery.

## Oracle's Curse {#oracle-s-curse}

A cyclopean seer must choose the [haunted](ref/oraclecurse/haunted),
[hunger](ref/oraclecurse/hunger) (see above),
[powerless prophecy](ref/oraclecurse/powerless-prophecy) (see above), or
[tongues](ref/oraclecurse/tongues) curse at 1st level.

## Bonus Spells {#bonus-spells}

Each time a cyclopean seer would gain a bonus spell from her mystery, she instead selects a
divination spell from any class's spell list. If the spell is not on the cleric spell list, it must
be at least 1 level lower than the highest-level oracle spell the cyclopean seer can cast. This
ability alters the bonus spells granted by the oracle's mystery.

## Assume Fate (Su) {#assume-fate}

As an immediate action when targeted by an effect that requires a saving throw, you can choose
another creature within line of sight that is attempting a save against the same effect. The target
takes a penalty on its saving throw equal to 1d4 + 1 for every 4 levels you possess. You gain the
value of their penalty as a luck bonus on your saving throw. You can use this ability a number of
times per day equal to your Charisma bonus. This replaces the revelation gained at 1st level.

## Brutal Trance (Su) {#brutal-trance}

Once per day as a standard action, you can enter a trance that lasts 1 round per oracle level you
possess. While in this trance, you are [confused](ref/misc/confused), but each round that you can
act normally, you can ask a single question as if using _[commune](ref/spell/commune)_. This
replaces the revelation gained at 7th level.

## Revelations {#revelations}

All cyclopean seers have access to the following revelations, regardless of their chosen mysteries.

## Doomsaying (Su) {#doomsaying}

As a standard action, you can pronounce doom on a creature within 30 feet. The target takes a
penalty equal to your oracle level on either all skill checks, all saving throws, or all attack
rolls (your choice) for 1 minute or until he fails one such roll. You can use this ability a number
of times per day equal to your Charisma bonus. This is a curse effect (_Ultimate Magic_ 137).

## Flash of Insight (Su) {#flash-of-insight}

You gain the [cyclops](ref/monster/cyclops) racial ability of the same name (_Bestiary_ 52). If you
already possess this ability, you gain an additional daily use.

## Prescience (Ex) {#prescience}

You gain a +2 bonus to your Armor Class against attacks of opportunity and a +2 bonus on
[concentration](ref/rule/concentration) checks. At 5th level and every 5 levels thereafter, these
bonuses increase by 1.

This ability alters the revelation class feature.

## Final Revelation {#final-revelation}

Upon reaching 20th level, you embody ancient cyclopes' insight. You can use each of the following
once per day as a spell-like ability: _[discern location](ref/spell/discern-location)_,
_[prying eyes](ref/spell/prying-eyes)_, and _[stone tell](ref/spell/stone-tell)_. In addition, using
flash of insight to select a d20 roll result equal to or lower than your Charisma modifier doesn't
expend that ability. This replaces the final revelation of the oracle's mystery.
