+++
id = "ref/arc-companion/tracker"
kind = "archetype"
title = "Tracker"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tracker", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "189"

[fields]
kind = "archetype"
features = [
  { anchor = "expert-tracker" },
]
trades = [
  { replaces = "Share Spells", by = ["expert-tracker"] },
  { replaces = "Devotion", by = ["expert-tracker"] },
]
+++

Some companions are expert trackers, able to use their [scent](ref/umr/scent) ability to follow any
trail.

## Keen Nose {#keen-nose}

A tracker must be an animal companion with the scent ability.

## Tracker Skills {#tracker-skills}

Trackers treat Survival as a class skill.

## Expert Tracker (Ex) {#expert-tracker}

A tracker gains a competence bonus on Survival checks to track via scent equal to
[half](ref/misc/fractions-and-rounding) its total Hit Dice. At 6th level, it can move at its normal
speed while using Survival to follow tracks without taking the normal -5 penalty. It takes only a
-10 penalty (instead of the normal -20 penalty) when moving at up to twice its normal speed while
tracking.

This replaces share spells and devotion.
