+++
id = "ref/arc-monk/far-strike-monk"
kind = "archetype"
title = "Far Strike Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Far%20Strike%20Monk"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "far_strike_monk", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ranged-tactics-toolbox"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "flurry-of-blows", level = 1 },
  { anchor = "fast-thrower", level = 1 },
  { anchor = "invisible-blade", level = 3 },
  { anchor = "ki-pool", level = 4 },
  { anchor = "ki-missile", level = 5 },
  { anchor = "trick-throw", level = 11 },
]
trades = [
  { replaces = "Stunning Fist", feature = "stunning-fist", by = ["fast-thrower"] },
  { replaces = "Still mind", feature = "still-mind", by = ["invisible-blade"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["ki-missile"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["trick-throw"] },
  { alters = "Flurry of blows", feature = "flurry-of-blows", by = ["flurry-of-blows"] },
]
+++

Far strike monks are masters of thrown weapons, from [shuriken](ref/eq-weapon/shuriken) to
[throwing axes](ref/eq-weapon/throwing-axe) to [spears](ref/eq-weapon/spear). The far strike school
views thrown attacks as an extension of unarmed strikes, and masters of this school can infuse
thrown weapons with their ki.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

In addition to the standard monk weapon proficiencies, a far strike monk is proficient with all
thrown weapons.

## Flurry of Blows (Ex) {#flurry-of-blows}

A far strike monk can make a flurry of blows as a full-attack action as long as he's attacking with
thrown weapons. He can't make a flurry of blows with his unarmed attacks or any other weapons. A far
strike monk's flurry of blows otherwise functions as the standard monk class feature.

A far strike monk can't use [Rapid Shot](ref/feat/rapid-shot) when making a flurry of blows with a
thrown weapon. This ability alters flurry of blows.

## Bonus Feats {#bonus-feats}

A far strike monk adds the following feats to his list of bonus feats at 1st level:
[Far Shot](ref/feat/far-shot), [Point-Blank Shot](ref/feat/point-blank-shot),
[Precise Shot](ref/feat/precise-shot), and any targeting feat. At 6th level, he adds the following
feats: [Improved Precise Shot](ref/feat/improved-precise-shot),
[Parting Shot](ref/feat/parting-shot), and [Trick Shooter](ref/feat/trick-shooter). At 10th level,
he adds the following feats: [Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery) and
[Pinpoint Targeting](ref/feat/pinpoint-targeting).

## Fast Thrower {#fast-thrower}

At 1st level, a far strike monk gains [Quick Draw](ref/feat/quick-draw) as a bonus feat, even if he
doesn't meet the prerequisites. At 4th level, he gains [Shot on the Run](ref/feat/shot-on-the-run)
as a bonus feat, even if he doesn't meet the prerequisites. At 8th level, when using the Shot on the
Run feat, he can make a second ranged attack with a -5 penalty at any point during his movement. At
15th level, he can make a third ranged attack with a -10 penalty at any point during his movement.
This ability replaces Stunning Fist.

## Invisible Blade (Ex) {#invisible-blade}

At 3rd level, when a far strike monk uses the Stealth skill to maintain his obscured location after
sniping, he takes a -10 penalty on his Stealth check instead of -20. This ability replaces still
mind.

## Ki Pool (Su) {#ki-pool}

At 4th level, in addition to the normal abilities of his ki pool, a far strike monk can spend 1
point from his ki pool to increase the range increment of a thrown weapon by 20 feet for 1 round.

## Ki Missile (Su) {#ki-missile}

At 5th level, a far strike monk can spend 1 point from his ki pool as a swift action to change the
base damage dice of thrown weapons to that of his unarmed strikes. These weapons are also treated as
_[ki focus](ref/magic-enh/ki-focus)_ weapons, allowing the monk to apply his special ki attacks to
his thrown weapons as if they were unarmed strikes. This effect lasts until the beginning of his
next turn. This ability replaces purity of body.

## Trick Throw (Su) {#trick-throw}

At 11th level, a far strike monk can infuse his thrown weapons with ki to hit targets that he might
otherwise miss. By spending 1 point from his ki pool as a swift action, the far strike monk can
ignore [concealment](ref/rule/concealment). By spending 2 points, he can ignore total concealment or
[cover](ref/rule/cover). By spending 3 points, he can ignore total cover, even throwing weapons
around corners. The weapon must still be able to reach the target; for instance, a target inside a
closed building with no open doors or windows cannot be attacked using Trick Throw. These effects
last for 1 round. This ability replaces diamond body.
