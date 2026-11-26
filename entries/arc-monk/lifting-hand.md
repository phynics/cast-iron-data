+++
id = "ref/arc-monk/lifting-hand"
kind = "archetype"
title = "Lifting Hand"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Lifting%20Hand"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lifting_hand", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "savage-toss", level = 1 },
  { anchor = "joint-lock", level = 10 },
  { anchor = "counter-throw", level = 12 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["savage-toss"] },
  { replaces = "Bonus feat gained at 10th level", feature = "bonus-feat", levels = [10], by = ["joint-lock"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["counter-throw"] },
  { alters = "Bonus feats", feature = "bonus-feat" },
]
+++

Those studied in the art of grappling know that using their opponents' own weight and momentum to
lift, disable, or throw them is impressive and effective. When facing a master of the lifting hand,
an enemy is likely to find itself sailing through the air or locked in a tortuous compliance hold.

## Savage Toss (Ex) {#savage-toss}

A lifting hand gains [Savage Slam](ref/feat/savage-slam) as a bonus feat, even if she doesn't meet
the prerequisites.

At 4th level, when the lifting hand succeeds at her grapple combat maneuver check while using the
Savage Slam feat and her grapple combat maneuver check result exceeds the opponent's CMD by at least
5, she can throw the opponent into an non-adjacent square. The lifting hand can throw the opponent
10 feet, plus an additional 5 feet for every 5 by which her grapple check exceeds the opponent's
CMD. For instance, if the lifting monk exceeds the target's CMD by 15, she can throw the target into
a square 20 feet away.

At 8th level, when using Savage Slam, the lifting hand's target no longer receives a bonus to its
CMD when the lifting hand attempts to throw it into a dangerous area.

This replaces stunning fist.

## Bonus Feats (Ex) {#bonus-feats}

A lifting hand adds [Whirling Hold](ref/feat/whirling-hold) to her list of bonus feats at 1st level.
At 6th level, she adds [Dramatic Slam](ref/feat/dramatic-slam) and
[Overhead Flip](ref/feat/overhead-flip). At 10th level, she adds
[Savage Leap](ref/feat/savage-leap).

This alters the monk's bonus feats.

## Joint Lock (Ex) {#joint-lock}

At 10th level, when a lifting hand succeeds at a combat maneuver check to maintain a grapple,
instead of choosing to damage, move, pin, or tie up the opponent, she can instead force one of the
target's limbs into an agonizing position. The target becomes [sickened](ref/misc/sickened) as long
as the lifting hand maintains the grapple. When the grapple is released or broken, the target is
[fatigued](ref/misc/fatigued) for a number of rounds equal to the lifting hand's level. This is a
pain effect.

This replaces the bonus feat gained at 10th level.

## Counter-Throw (Sp) {#counter-throw}

At 12th level, a lifting hand can [ready an action](ref/rule/ready) to trigger if a creature tries
to attack her. When the readied action triggers, the lifting hand can attempt a grapple combat
maneuver check with a +2 bonus. If she succeeds, she grapples the creature and negates the
triggering attack, and she can spend an immediate action to use the Savage Slam feat.

This replaces abundant step. (For the unchained monk from _Pathfinder Unchained_, this replaces the
ki power gained at 12th level.)
