+++
id = "ref/arc-investigator/holomog-demolitionist"
kind = "archetype"
title = "Holomog Demolitionist"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Holomog%20Demolitionist"
source_ids = ["heroes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holomog_demolitionist", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "heroes-of-golarion"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "structural-knowledge", level = 2 },
  { anchor = "structural-insight", level = 2 },
  { anchor = "ricochet", level = 3 },
  { anchor = "studied-strike", level = 4 },
  { anchor = "battlefield-preparation", level = 6 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["structural-knowledge"] },
  { replaces = "Poison resistance", feature = "poison-resistance", by = ["structural-insight"] },
  { replaces = "Investigator talents gained at 3rd and 9th levels", feature = "investigator-talent", levels = [3, 9], by = ["ricochet"] },
  { alters = "Studied strike", feature = "studied-strike", by = ["studied-strike"] },
]
+++

Holomog is an ancient nation built on even more ancient ruins. Its renowned civil engineers develop
skills that allow them to take full advantage of their environments.

## Structural Knowledge (Ex) {#structural-knowledge}

At 2nd level, a Holomog demolitionist gains [Improved Sunder](ref/feat/improved-sunder) as a bonus
feat, even if he does not meet the prerequisites.

This replaces poison lore.

## Structural Insight (Ex) {#structural-insight}

At 2nd level, a Holomog demolitionist gains an insight bonus equal to his investigator level on
Acrobatics checks to move through [difficult terrain](ref/rule/terrain-and-obstacles). At 5th level,
when attempting to damage objects and structures, he ignores the first 5 points of
[hardness](ref/umr/hardness). At 8th level, the Holomog demolitionist gains a +2 insight bonus on
attack rolls when attempting to [sunder](ref/rule/sunder) an item. At 11th level, he can attempt a
sunder combat maneuver check against a wall no more than 5 feet thick. If the damage from the sunder
combat maneuver exceeds the wall's [hardness](ref/umr/hardness), the Holomog demolitionist creates a
5-foot opening in the wall, through which a Medium creature can easily pass.

This replaces poison resistance.

## Ricochet (Ex) {#ricochet}

At 3rd level as a standard action, the Holomog demolitionist can attack an adjacent wall or object
with a melee weapon. On a hit, he creates a 15-foot-cone of rock shards or splinters that deals 2d6
points of damage to targets in the area of effect. A target can attempt a Reflex save (DC = 10 +
half the Holomog demolitionist's level + his Intelligence modifier) to reduce this damage by half.
At 9th level, the damage increases to 4d6, and the investigator can create this effect with a ranged
weapon by targeting a wall or object within 30 feet.

This replaces the investigator talents gained at 3rd and 9th levels.

## Studied Strike (Ex) {#studied-strike}

A Holomog demolitionist's studied strike damage increases every 4 levels, rather than every 2 (to
2d6 at 8th, 3d6 at 12th, 4d6 at 16th, and 5d6 at 20th level).

This alters studied strike.

## Battlefield Preparation (Ex) {#battlefield-preparation}

At 6th level, the investigator can create 10 feet of
[difficult terrain](ref/rule/terrain-and-obstacles) by spending a full-round action to analyze and
manipulate his surroundings. This terrain can be in any shape designated by the investigator, but at
least 1 square must be adjacent to his position. For every 4 levels he has beyond 6th, the
investigator can create an additional 10 feet of difficult terrain, to a maximum of 40 feet at 18th
level. This is a physical alteration that remains in place until the surface is altered again (the
road is repaved, the floor repaired, etc.), and the Holomog demolitionist ignores the effects of any
difficult terrain he creates in this way.

At 10th level, the Holomog demolitionist can use this ability to create clouds of dust and rubble
that create [concealment](ref/rule/concealment) rather than difficult terrain in the same area. This
concealment lasts 1d4 rounds plus 1 round for every 4 investigator levels, and the Holomog
demolitionist is affected by the concealment as normal.

At 14th level, the difficult terrain the Holomog demolitionist creates provides
[cover](ref/rule/cover) for himself and his allies.
