+++
id = "ref/arc-monk/far-strike-monk"
kind = "archetype"
title = "Far Strike Monk"
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
replaces = ["Stunning Fist", "Still mind", "Purity of body", "Diamond body"]
alters = ["Flurry of blows"]
replaces_features = ["stunning-fist", "still-mind", "purity-of-body", "diamond-body"]
alters_features = ["flurry-of-blows"]
+++

Far strike monks are masters of thrown weapons, from [shuriken](ref/eq-weapon/shuriken) to
[throwing axes](ref/eq-weapon/throwing-axe) to [spears](ref/eq-weapon/spear). The far strike school
views thrown attacks as an extension of unarmed strikes, and masters of this school can infuse
thrown weapons with their ki.

**Weapon and Armor Proficiency**

**Info:** In addition to the standard monk weapon proficiencies, a far strike monk is proficient
with all thrown weapons.

**Flurry of Blows (Ex)**

**Ability:** A far strike monk can make a _flurry of blows_ as a full-attack action as long as he's
attacking with thrown weapons. He can't make a _flurry of blows_ with his unarmed attacks or any
other weapons. A far strike monk's _flurry of blows_ otherwise functions as the standard monk class
feature.

**Alters:** Flurry of blows

**Special:** A far strike monk can't use [Rapid Shot](ref/feat/rapid-shot) when making a _flurry of
blows_ with a thrown weapon.

**Bonus Feats**

**At 1st Level:** A far strike monk adds the following feats to his list of bonus feats:
[Far Shot](ref/feat/far-shot), [Point-Blank Shot](ref/feat/point-blank-shot),
[Precise Shot](ref/feat/precise-shot), and any targeting feat.

**At 10th Level:** He adds the following feats:
[Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery) and
[Pinpoint Targeting](ref/feat/pinpoint-targeting).

**At 6th Level:** He adds the following feats:
[Improved Precise Shot](ref/feat/improved-precise-shot), [Parting Shot](ref/feat/parting-shot), and
[Trick Shooter](ref/feat/trick-shooter).

**Fast Thrower**

**At 1st Level:** A far strike monk gains [Quick Draw](ref/feat/quick-draw) as a bonus feat, even if
he doesn't meet the prerequisites.

**At 15th Level:** He can make a third ranged attack with a -10 penalty at any point during his
movement.

**At 4th Level:** He gains [Shot on the Run](ref/feat/shot-on-the-run) as a bonus feat, even if he
doesn't meet the prerequisites.

**At 8th Level:** When using the Shot on the Run feat, he can make a second ranged attack with a -5
penalty at any point during his movement.

**Replaces:** Stunning Fist

**Invisible Blade (Ex)**

**Ability:** When a far strike monk uses the Stealth skill to maintain his obscured location after
sniping, he takes a -10 penalty on his Stealth check instead of -20.

**Gained:** At 3rd Level

**Replaces:** Still mind

**Ki Pool (Su)**

**Ability:** In addition to the normal abilities of his _ki pool,_ a far strike monk can spend 1
point from his _ki pool_ to increase the range increment of a thrown weapon by 20 feet for 1 round.

**Gained:** At 4th Level

**Ki Missile (Su)**

**Gained:** At 5th Level

**Replaces:** Purity of body

**Swift:** A far strike monk can spend 1 point from his _ki pool_ to change the base damage dice of
thrown weapons to that of his unarmed strikes. These weapons are also treated as
[ki focus](ref/magic-enh/ki-focus) weapons, allowing the monk to apply his special ki attacks to his
thrown weapons as if they were unarmed strikes. This effect lasts until the beginning of his next
turn.

**Trick Throw (Su)**

**Flavor:** A far strike monk can infuse his thrown weapons with ki to hit targets that he might
otherwise miss.

**Gained:** At 11th Level

**Replaces:** Diamond body

**Special:** The weapon must still be able to reach the target; for instance, a target inside a
closed building with no open doors or windows cannot be attacked using Trick Throw.

**Swift:** By spending 1 point from his _ki pool,_ the far strike monk can ignore
[concealment](ref/rule/concealment). By spending 2 points, he can ignore total concealment or
[cover](ref/rule/cover). By spending 3 points, he can ignore total cover, even throwing weapons
around corners. These effects last for 1 round.
