+++
id = "ref/discovery/void-bomb"
kind = "rule"
title = "Void Bomb"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "void_bomb", path = "json/class_ability_discoveries.json" },
]

[fields]
kind = "none"
+++

**&L&Void Bomb&FN&**

**Ability:** _Void bombs_ deals 1d4 points of bludgeoning damage, plus 1d4 points of bludgeoning
damage for every 2 alchemist levels beyond 1st, instead of 1d6.

A creature hit by the bomb must succeed at a Reflex save against the bomb's DC. If it fails, it is
knocked [prone](ref/rule/prone) and can't get up for 1 round. If it succeeds, all of its movement
speeds are reduced to 5 feet for 1 round.

Other creatures within 5 feet of the bomb's target take no damage, but must succeed at a Reflex save
against the bomb's DC or have all their movement speeds reduced to 5 feet for 1 round.

**Flavor:** By combining the spores from strange fungi with slivers from extradimensional voids,
some drow alchemists create bombs that cause bursts of gravity capable of crushing those inside.

**Prereq:** [Drow](ref/race/drow), 6th-level alchemist
