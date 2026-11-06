+++
id = "ref/rule/wound-points"
kind = "rule"
title = "Wound Points"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wound_points", path = "json/rules_opt_combat01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Combat pg 206

Typically a creature has a number of wound points equal to twice its Constitution score. It also has
a wound threshold equal to its Constitution score.

Wound points represent the amount of physical punishment a creature can take before it dies. When a
creature's wound points drop to or below its wound threshold, that creature becomes wounded. When a
creature is wounded, it gains the staggered condition until it is no longer wounded. Furthermore,
when a creature is wounded, if that creature takes any standard or move action on its turn, its
remaining wound points are reduced by 1 and it must make a DC 10 Constitution check. If the creature
fails that check, it falls unconscious.

When a creature reaches 0 or fewer wound points, it is dead.

**Wound Points and Constitution Damage, Drain, and Penalties:** A creature's wound points and
Constitution score are intrinsically linked. For each point of Constitution damage a creature takes,
it loses 2 wound points, but this damage does not affect the creature's wound threshold. When a
creature takes a penalty to its Constitution score or its Constitution is drained, it loses 1 wound
point per point of drain or per penalty for the duration of the penalty or drain. A penalty to
Constitution or Constitution drain has no effect on the creature's wound threshold.
