+++
id = "ref/arc-fighter/archer"
kind = "archetype"
title = "Archer"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Archer"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "archer", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "104"

[fields]
kind = "archetype"
features = [
  { anchor = "hawkeye", level = 2 },
  { anchor = "trick-shot", level = 3 },
  { anchor = "expert-archer", level = 5 },
  { anchor = "safe-shot", level = 9 },
  { anchor = "evasive-archer", level = 13 },
  { anchor = "volley", level = 17 },
  { anchor = "ranged-defense", level = 19 },
  { anchor = "weapon-mastery" },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["hawkeye"] },
  { replaces = "Armor training 1, 2, 3, and 4", feature = "armor-training", levels = [3, 7, 11, 15], by = ["trick-shot"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["expert-archer"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["safe-shot"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["evasive-archer"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["volley"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["ranged-defense"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

The archer is dedicated to the careful mastery of the bow, perfecting his skills with years of
practice honed day after day on ranges and hunting for game, or else on the battlefield, raining
destruction down on the enemy lines.

## Hawkeye (Ex) {#hawkeye}

At 2nd level, an archer gains a +1 bonus on Perception checks, and the range increment for any bow
he uses increases by 5 feet. These bonuses increase by +1 and 5 additional feet for every 4 levels
beyond 2nd. This ability replaces bravery.

## Trick Shot (Ex) {#trick-shot}

At 3rd level, an archer can choose one of the following combat maneuvers or actions:
[disarm](ref/rule/disarm), [feint](ref/rule/feint), or [sunder](ref/rule/sunder). He can perform
this action with a bow against any target within 30 feet, with a -4 penalty to his CMB. Every four
levels beyond 3rd, he may choose an additional trick shot to learn. These maneuvers use up arrows as
normal.

At 11th level, he may also choose from the following combat maneuvers:
[bull rush](ref/rule/bull-rush), [grapple](ref/rule/grapple), [trip](ref/rule/trip). A target
grappled by an arrow can break free by destroying the archer's arrow ([hardness](ref/umr/hardness)
5, hit points 1, break DC 13) or with an Escape Artist or CMB check (against the archer's CMD -4).
This ability replaces armor training 1, 2, 3, and 4.

## Expert Archer (Ex) {#expert-archer}

At 5th level, an archer gains a +1 bonus on attack and damage rolls with bows. This bonus increases
by +1 for every four levels beyond 5th. This ability replaces weapon training 1.

## Safe Shot (Ex) {#safe-shot}

At 9th level, an archer does not provoke attacks of opportunity when making ranged attacks with a
bow. This ability replaces weapon training 2.

## Evasive Archer (Ex) {#evasive-archer}

At 13th level, an archer gains a +2 dodge bonus to AC against ranged attacks. This bonus increases
to +4 at 17th level. This ability replaces weapon training 3.

## Volley (Ex) {#volley}

At 17th level, as a full-round action, an archer can make a single bow attack at his highest base
attack bonus against any number of creatures in a 15-foot-radius [burst](ref/misc/burst), making
separate attack and damage rolls for each creature. This ability replaces weapon training 4.

## Ranged Defense (Ex) {#ranged-defense}

At 19th level, an archer gains DR 5/— against ranged attacks. In addition, as an immediate action,
he can catch an arrow fired at him and shoot it any target he chooses, as if he had the
[Snatch Arrows](ref/feat/snatch-arrows) feat. This ability replaces armor mastery.

## Weapon Mastery (Ex) {#weapon-mastery}

An archer must choose a type of bow.
