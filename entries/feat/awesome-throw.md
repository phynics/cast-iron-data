+++
id = "ref/feat/awesome-throw"
kind = "feat"
title = "Awesome Throw"
source_ids = ["pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "awesome_throw", path = "json/feat01.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Str 25, Throw Anything or rock throwing, Improved Bull Rush, size Large or larger."
prerequisite_feats = ["ref/feat/improved-bull-rush", "ref/feat/throw-anything"]
benefit = "As a standard action, you can perform the awesome throw combat maneuver. You do this by making a thrown weapon attack; if you don't have the Throw Anything feat, you must use a large, bulky, and relatively regular-shaped object with a hardness of at least 5 (such as a rock or treasure chest). If that attack hits a corporeal opponent smaller than you, the opponent takes damage and is knocked away, flying 10 feet in a straight line away from you and falling prone. If an obstacle prevents the completion of your target's move, the target and the obstacle each take 1d6 points of damage, and the target is knocked prone in a space adjacent to the obstacle."
+++

## Awesome Throw (Combat)

**Sources:** Pathfinder \#91: Battle of Bloodmarch Hills pg 69

Your ranged attacks can send smaller opponents flying.\
**Prerequisites:** Str 25, [Throw Anything](ref/feat/throw-anything) or rock throwing,
[Improved Bull Rush](ref/feat/improved-bull-rush), size Large or larger.\
**Benefit:** As a standard action, you can perform the awesome throw combat maneuver. You do this by
making a thrown weapon attack; if you don't have the Throw Anything feat, you must use a large,
bulky, and relatively regular-shaped object with a [hardness](ref/umr/hardness) of at least 5 (such
as a rock or treasure chest). If that attack hits a corporeal opponent smaller than you, the
opponent takes damage and is knocked away, flying 10 feet in a straight line away from you and
falling [prone](ref/rule/prone). If an obstacle prevents the completion of your target's move, the
target and the obstacle each take 1d6 points of damage, and the target is knocked prone in a space
adjacent to the obstacle.
