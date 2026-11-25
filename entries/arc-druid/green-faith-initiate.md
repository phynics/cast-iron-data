+++
id = "ref/arc-druid/green-faith-initiate"
kind = "archetype"
title = "Green Faith Initiate"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Green%20Faith%20Initiate"
source_ids = ["ultimate-wilderness", "faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "green_faith_initiate", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "141"
[[sources]]
publication = "faiths-and-philosophies"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "mediator-s-ear" },
  { anchor = "zephyr-message", level = 6 },
  { anchor = "path-to-refuge", level = 9 },
  { anchor = "secrets-across-lifetimes", level = 10 },
  { anchor = "a-thousand-voices", level = 13 },
]
trades = [
  { replaces = "Trackless step", feature = "trackless-step", by = ["mediator-s-ear"] },
  { replaces = "The druid's additional daily use of wild shape gained at 6th level", feature = "wild-shape", levels = [6], by = ["zephyr-message"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["path-to-refuge"] },
  { replaces = "The druid's additional daily use of wild shape gained at 10th level", feature = "wild-shape", levels = [10], by = ["secrets-across-lifetimes"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["a-thousand-voices"] },
]
+++

Druids who are initiated into the magic of nature as strict students of the
[Green Faith's](ref/faith/green-faith) traditions sometimes demonstrate abilities unique to their
organization.

## Mediator's Ear (Ex) {#mediator-s-ear}

By 3rd level, a Green Faith initiate is respected for her neutrality and even-handed attitude toward
all people as well as other living things. She quickly develops a sense of other peoples' attitudes,
much as she does with animals. A Green Faith initiate gains a bonus on Diplomacy and Sense Motive
checks equal to [half](ref/misc/fractions-and-rounding) her druid level.

This replaces trackless step.

## Zephyr Message (Sp) {#zephyr-message}

At 6th level, once per day, a Green Faith initiate can cast
_[whispering wind](ref/spell/whispering-wind)_ as a
[spell-like ability](ref/umr/spell-like-abilities), treating her druid level as her caster level.

This replaces the druid's additional daily use of wild shape gained at 6th level.

## Path to Refuge (Sp) {#path-to-refuge}

At 9th level, once per day, a Green Faith initiate can travel as if with
_[transport via plants](ref/spell/transport-via-plants)_ to any major Green Faith druid circle or
important holy site. Each of these sites is marked with special standing stones that allow all Green
Faith followers within range using _[transport via plants](ref/spell/transport-via-plants)_ or _tree
strid_e to sense their distance from it and the direction to it. At 14th level and again at 19th
level, she can use this ability one additional time per day.

This replaces venom immunity.

## Secrets across Lifetimes (Sp) {#secrets-across-lifetimes}

At 10th level, a Green Faith initiate can use _[legend lore](ref/spell/legend-lore)_ once per week
as a [spell-like ability](ref/umr/spell-like-abilities), drawing upon the knowledge of Green Faith
archdruids recorded in secret across the generations in places where magic such as this can retrieve
it. This ability does not require material components.

This replaces the druid's additional daily use of wild shape gained at 10th level.

## A Thousand Voices (Su) {#a-thousand-voices}

At 13th level, a Green Faith initiate can communicate with any creature that has a language or with
any stone, as if using _[tongues](ref/spell/tongues)_ or _[stone tell](ref/spell/stone-tell)_,
respectively, for up to 1 minute per druid level each day. This duration does not need to be
consecutive, but it must be spent in 1-minute increments.

This replaces a thousand faces.
