+++
id = "ref/arc-oracle/seer"
kind = "archetype"
title = "Seer"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Seer"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seer", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-magic"
page = "59"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-divination" },
  { anchor = "gift-of-prophecy", level = 3 },
]
trades = [
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [4, 6, 8, 10, 12, 14, 16, 18], power = "bonus spells" },
]
+++

While all oracles possess some ability at divination, the seer is a true prophet, able to see things
as they really are, or will be.

## Recommended Mysteries {#recommended-mysteries}

lore, nature, time.

## Bonus Spells {#bonus-spells}

_detect thoughts_ (4th), _clairaudience/clairvoyance_ (6th), _scrying_ (8th), _true seeing_ (10th),
_legend lore_ (12th), _greater scrying_ (14th), _vision_ (16th), _foresight_ (18th). These bonus
spells replace the oracle's mystery bonus spells at these levels.

## Revelations {#revelations}

A seer must take the following revelations at the listed levels.

## Natural Divination (Ex) {#natural-divination}

As the [nature](ref/mystery/nature) mystery revelation (see page 51 of the _Advanced Player's
Guide_). You must take this revelation at 1st level.

## Gift of Prophecy (Su) {#gift-of-prophecy}

Once per day, you can enter a trance to gain a glimpse of the future. This trance lasts for 1
minute, which must be uninterrupted and during which you can take no other actions. At 3rd level,
you gain the benefits of an _[augury](ref/spell/augury)_ spell with 90% effectiveness. At 5th level,
you gain the benefits of a _[divination](ref/spell/divination)_ spell with 90% effectiveness. At 9th
level, the knowledge you gain is equivalent to a _[commune](ref/spell/commune)_ spell. None of these
spell effects require material components. You must take this revelation at 3rd level.
