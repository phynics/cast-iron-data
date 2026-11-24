+++
id = "ref/arc-slayer/stygian-slayer"
kind = "archetype"
title = "Stygian Slayer"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Stygian%20Slayer"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stygian_slayer", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "120"

[fields]
kind = "archetype"
features = [
  { anchor = "invisibility", level = 4 },
  { anchor = "spell-use", level = 7 },
  { anchor = "shadowy-mist-form", level = 10 },
]
trades = [
  { replaces = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { replaces = "Slayer talent gained at 4th level", feature = "slayer-talents", levels = [4], by = ["invisibility"] },
  { replaces = "Stalker", feature = "stalker", by = ["spell-use"] },
  { replaces = "Advanced slayer talent gained at 10th level", feature = "advanced-talents", levels = [10], by = ["shadowy-mist-form"] },
]
+++

A stygian slayer crawls out of the darkest shadows to strike fear into the hearts of civilized folk.
He's a merciless killer who can control a sliver of magic, allowing him to arrive unseen, commit
murder, and depart without detection.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A stygian slayer is proficient with light armor, but not with medium armor, heavy armor, or any kind
of shield (including tower shields). This replaces the slayer's armor proficiency.

## Invisibility (Sp) {#invisibility}

At 4th level, a stygian slayer can cast _[invisibility](ref/spell/invisibility)_ once per day, using
his slayer level as his caster level. The slayer uses his Intelligence modifier for
[concentration](ref/rule/concentration) checks when using this ability. The slayer can use this an
additional time per day at 8th level and every 4 levels thereafter. This ability replaces the slayer
talent gained at 4th level.

## Spell Use {#spell-use}

At 7th level, a stygian slayer is able to use spell completion and spell trigger items as if he were
an arcane caster with these spells on his spell list: _[darkness](ref/spell/darkness)_,
_[forced quiet](ref/spell/forced-quiet)_, _[modify memory](ref/spell/modify-memory)_,
_[nondetection](ref/spell/nondetection)_, _[obscuring mist](ref/spell/obscuring-mist)_,
_[phantom steed](ref/spell/phantom-steed)_, _[shadow walk](ref/spell/shadow-walk)_, and wizard
spells of the illusion school of spell level 0 through 4th. The slayer's uses his class level as his
caster level for this ability. This ability replaces stalker.

## Shadowy Mist Form (Sp) {#shadowy-mist-form}

At 10th level, a stygian slayer can transform into an inky black cloud of mist. This functions as
_[gaseous form](ref/spell/gaseous-form)_, except it also obscures vision as
_[fog cloud](ref/spell/fog-cloud)_. The slayer can use this ability for a number of minutes per day
equal to his level. These minutes need not be consecutive, but must be used in 1-minute increments.
This ability replaces the advanced slayer talent gained at 10th level.

## Slayer Talents {#slayer-talents}

The following slayer talents (and rogue talents) complement the stygian slayer archetype: bleeding
attack, lasting poison, poison use, powerful sneak, rogue crawl, slow reactions, surprise attack,
and swift poison. (Those with asterisks \[\*\] are detailed in the slayer class, starting on page
53.)

## Advanced Slayer Talents {#advanced-slayer-talents}

The following advanced slayer talents (and advanced rogue talents) complement the stygian slayer
archetype: assassinate, hunter's surprise, and slayer camouflage.
