+++
id = "ref/arc-oracle/reincarnated-oracle"
kind = "archetype"
title = "Reincarnated Oracle"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Reincarnated%20Oracle"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reincarnated_oracle", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-race-guide"
page = "199"

[fields]
kind = "archetype"
features = [
  { anchor = "oracle-s-curse", level = 1 },
  { anchor = "location-memories" },
  { anchor = "spirit-memories" },
]
trades = [
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [2, 4, 10, 16, 18], power = "bonus spells" },
]
+++

A reincarnated oracle draws her knowledge and power from the experiences of her previous lives. Her
memories guide her through a spiritual ascension leading the way to her ultimate incarnation. A
reincarnated oracle has the following class features.

## Recommended Mysteries {#recommended-mysteries}

ancestor, lore, time.

## Oracle's Curse {#oracle-s-curse}

A reincarnated oracle must choose the [haunted](ref/oraclecurse/haunted) or
[tongues](ref/oraclecurse/tongues) curse at 1st level.

## Bonus Spells {#bonus-spells}

_see alignment_ (2nd), _detect thoughts_ (4th), _contact other plane_ (10th), _moment of prescience_
(16th), _overwhelming presence_ (18th). These spells replace the oracle's mystery bonus spells at
these levels.

## Revelations {#revelations}

A reincarnated oracle must take the following revelations at one of the listed levels.

## Location Memories (Su) {#location-memories}

As a swift action, you may search your past lives for memories of or insight about your current
location. This grants you the [scent](ref/umr/scent) ability,
[low-light vision](ref/rule/low-light-vision), and a +2 insight bonus on Perception and Survival
checks for 1 minute. You can use this ability a number of times per day equal to 3 + your Charisma
modifier. You must take this revelation at 1st level or 3rd level.

## Spirit Memories (Su) {#spirit-memories}

Once per day, you call upon the unfulfilled desires and goals of your past lives and project their
frustration and despair through your eyes at a target. This is a [gaze](ref/umr/gaze) attack
affecting one creature. The target must make a Will save (DC 10 + 1/2 your oracle level + your
Charisma modifier) or be [sickened](ref/misc/sickened) and [staggered](ref/misc/staggered) for 1
round. This is a mind-affecting compulsion effect. You can use this ability a number of times per
day equal to 3 + your Charisma modifier. You must take this revelation at 1st, 3rd, or 7th level.
