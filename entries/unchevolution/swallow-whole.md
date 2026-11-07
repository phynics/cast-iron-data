+++
id = "ref/unchevolution/swallow-whole"
kind = "rule"
title = "Swallow Whole"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swallow_whole", path = "json/class_ability_unchained_evolutions.json" },
]

[fields]
kind = "none"
+++

**Swallow Whole (Ex)**

**Ability:** The eidolon gains the [swallow whole](ref/umr/swallow-whole) ability, giving it the
ability to consume its foes. If the eidolon begins its turn with a creature grappled using its
_bite_ attack (see the _[grab](ref/carried/bestiary/rules/universal-monster-rules/grab)_ evolution),
it can attempt a combat maneuver check to swallow the creature. The creature must be at least one
size category smaller than the eidolon.

Swallowed creatures take an amount of bludgeoning damage equal to the eidolon's bite damage each
round + 1d6 points of damage. A swallowed creature keeps the [grappled](ref/rule/grapple-conditions)
condition, but can attempt to cut its way free with a light piercing or slashing weapon. The amount
of damage needed to cut free is equal to 1/10 the eidolon's total hit points. The eidolon's AC
against these attacks is equal to 10 + 1/2 its natural armor bonus. If a swallowed creature cuts its
way out, the eidolon loses this ability until it heals this damage.

Alternatively, the swallowed creature can attempt to escape the grapple as normal. Success indicates
that it has returned to the eidolon's mouth, where it can attempt to escape or can be swallowed
again.

**Prereq:** 9th-level unchained summoner; [agathion](ref/eidolon/agathion),
[daemon](ref/eidolon/daemon), [demon](ref/eidolon/demon), [devil](ref/eidolon/devil),
[div](ref/eidolon/div), [elemental](ref/eidolon/elemental), [protean](ref/eidolon/protean), or
[psychopomp](ref/eidolon/psychopomp) subtype; [grab](ref/unchevolution/grab) (bite)
