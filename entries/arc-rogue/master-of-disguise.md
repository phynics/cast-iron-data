+++
id = "ref/arc-rogue/master-of-disguise"
kind = "archetype"
title = "Master of Disguise"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Master%20of%20Disguise"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "master_of_disguise", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "46"

[fields]
kind = "archetype"
features = [
  { anchor = "consummate-actor", level = 1 },
  { anchor = "grandmaster-of-disguise", level = 10 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["consummate-actor"] },
  { replaces = "rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["consummate-actor"] },
  { replaces = "Rogue talent gained at 10th level", feature = "rogue-talents", levels = [10], by = ["grandmaster-of-disguise"] },
]
+++

A master of disguise feels no need to advertise her skills to build a reputation. Instead, she
believes that never letting her adversaries know her true identity protects her from bad luck or
missteps on a job.

## Consummate Actor (Ex) {#consummate-actor}

A master of disguise adds half her rogue level (minimum 1) on all Disguise checks and on Bluff
checks to stay in character while using Disguise. At 2nd level, she gains the
[quick disguise](ref/talent/quick-disguise) rogue talent, and she can create a disguise twice as
quickly as normal even for that rogue talent (she can create a disguise that encompasses only minor
details as a standard action).

This ability replaces trapfinding and the rogue talent gained at 2nd level.

## Grandmaster of Disguise (Ex) {#grandmaster-of-disguise}

At 10th level, a [master of disguise](ref/talent/master-of-disguise) gains the master of disguise
advanced rogue talent and can use it an unlimited number of times per day. Because she must still
don a physical disguise to gain this bonus, it doesn't stack with the bonuses from spells like
_[alter self](ref/spell/alter-self)_ and _[disguise self](ref/spell/disguise-self)_, but since it is
completely nonmagical, it is more reliable when scrutinized under magical detection.

This ability replaces the rogue talent gained at 10th level.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the master of disguise archetype: camouflage, false friend,
major magic, minor magic, obfuscate story, shades of gray, and steal the story.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the master of disguise archetype: hard minded,
hidden mind, skill mastery, slippery mind, and unwitting ally.
