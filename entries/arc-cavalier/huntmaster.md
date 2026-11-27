+++
id = "ref/arc-cavalier/huntmaster"
kind = "archetype"
title = "Huntmaster"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Huntmaster"
source_ids = ["animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "huntmaster", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "animal-archive"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "bestial-challenge", level = 1 },
  { anchor = "hunting-pack", level = 1 },
  { anchor = "tactician", level = 1 },
  { anchor = "takedown", level = 3 },
  { anchor = "animal-trainer", level = 4 },
  { anchor = "swift-tracker", level = 5 },
  { anchor = "pack-attack", level = 11 },
  { anchor = "quarry", level = 14 },
  { anchor = "improved-quarry", level = 20 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["hunting-pack"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["takedown"] },
  { replaces = "Banner", feature = "banner", by = ["swift-tracker"] },
  { replaces = "A cavalier's standard bonus feats", feature = "bonus-feat" },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["pack-attack"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["quarry"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["improved-quarry"] },
  { alters = "Challenge", feature = "challenge", by = ["bestial-challenge"] },
  { alters = "Tactician", feature = "tactician", by = ["tactician"] },
  { alters = "greater tactician", feature = "greater-tactician", by = ["tactician"] },
  { alters = "master tactician", feature = "master-tactician", by = ["tactician"] },
  { alters = "Expert trainer", feature = "expert-trainer", by = ["animal-trainer"] },
]
+++

Huntmasters train the beasts favored by lordly castes into swift and deadly trackers.

## Class Skills {#class-skills}

A huntmaster gains Knowledge (nature), Stealth, and Survival as class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A huntmaster is not proficient with heavy armor. Huntmasters are proficient with all simple and
martial weapons, plus the [net](ref/eq-weapon/net) and [whip](ref/eq-weapon/whip).

## Bestial Challenge (Ex) {#bestial-challenge}

Whenever a huntmaster issues a challenge, both he and his hunting pack gain the bonuses and
penalties associated with his challenge. This modifies the challenge ability.

## Hunting Pack (Ex) {#hunting-pack}

At 1st level, a huntmaster forms a close bond with an
[animal companion](ref/sidekick/animal-companion). This animal companion functions as a druid's
animal companion, using the cavalier's level as his effective druid level. He can choose either a
[bird](ref/companion/bird) or a [dog](ref/companion/dog) when selecting his animal companion.

The huntmaster can have more than one animal companion, but he must divide up his effective druid
level between his companions to determine the abilities of each companion. Each time a huntmaster's
effective druid level increases, he must decide how to allocate the increase among his animal
companions (including the option of adding a new 1st-level companion). Once an effective druid level
is allocated to a particular companion, it cannot be redistributed while that companion is in the
huntmaster's service (he must release a companion or wait until a companion dies to allocate its
levels to another companion). The share spells animal companion ability does not give the huntmaster
the ability to cast a single spell so that it affects all of his animal companions.

A huntmaster's animal companions gain a bonus on Survival checks to follow tracks equal to 1/2 the
cavalier's class level (minimum 1). This ability replaces mount.

## Tactician (Ex) {#tactician}

A huntmaster's tactician ability affects only his hunting pack, not other allies. This modifies the
tactician, greater tactician, and master tactician abilities.

## Takedown (Ex) {#takedown}

At 3rd level, a huntmaster's dog can make a free [trip](ref/rule/trip) or
[dirty trick](ref/rule/dirty-trick) ([entangled](ref/rule/entangled)) combat maneuver after a
successful melee attack. A huntmaster's bird can make a free dirty trick
([dazzled](ref/misc/dazzled) or [deafened](ref/misc/deafened)) combat maneuver after a successful
melee attack; if the target is already dazzled, the bird can choose dirty trick
([blinded](ref/misc/blinded)) instead. These combat maneuvers do not provoke attacks of opportunity.
This ability replaces cavalier's charge.

## Animal Trainer (Ex) {#animal-trainer}

At 4th level, a huntmaster's expert trainer ability applies to birds and dogs rather than mounts.
This modifies the expert trainer ability.

## Swift Tracker (Ex) {#swift-tracker}

At 5th level, a huntmaster gains the swift tracker ability, as the [ranger](ref/class/ranger)
ability of the same name. This ability replaces banner.

## Bonus Feats {#bonus-feats}

At 6th level, a huntmaster and all members of his hunting pack gain [Step Up](ref/feat/step-up) as a
bonus feat. At 12th level, they gain [Following Step](ref/feat/following-step) and at 18th level,
they gain [Step Up and Strike](ref/feat/step-up-and-strike). This ability replaces a cavalier's
standard bonus feats.

## Pack Attack (Ex) {#pack-attack}

At 11th level, whenever a huntmaster and any of his hunting pack or multiple animals in his hunting
pack are adjacent and attack the same target in melee, they are treated as
[flanking](ref/rule/flanking). In addition, they can flank a creature with
[improved uncanny dodge](ref/ability/improved-uncanny-dodge) if the huntmaster has at least 4 more
levels than the target. This ability replaces mighty charge.

## Quarry (Ex) {#quarry}

At 14th level, a huntmaster gains quarry, as the ranger ability of the same name. The benefits of
this ability also apply to his hunting pack. This ability replaces greater banner.

## Improved Quarry (Ex) {#improved-quarry}

At 20th level, a huntmaster gains improved quarry, as the ranger ability of the same name. The
benefits of this ability also apply to his hunting pack. This ability replaces supreme charge.
