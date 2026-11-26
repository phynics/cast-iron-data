+++
id = "ref/arc-swashbuckler/inspired-blade"
kind = "archetype"
title = "Inspired Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Inspired%20Blade"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inspired_blade", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "125"

[fields]
kind = "archetype"
features = [
  { anchor = "inspired-panache", level = 1 },
  { anchor = "inspired-finesse", level = 1 },
  { anchor = "deeds" },
  { anchor = "inspired-strike", level = 11 },
  { anchor = "rapier-training", level = 5 },
  { anchor = "rapier-weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Swashbuckler finesse", feature = "swashbuckler-finesse", by = ["inspired-finesse"] },
  { replaces = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["inspired-strike"] },
  { replaces = "Swashbuckler weapon training", feature = "swashbuckler-weapon-training", by = ["rapier-training"] },
  { replaces = "Swashbuckler weapon mastery", feature = "swashbuckler-weapon-mastery", by = ["rapier-weapon-mastery"] },
  { alters = "Panache", feature = "panache", by = ["inspired-panache"] },
]
+++

An inspired blade is both a force of personality and a sage of swordplay dedicated to the perfection
of combat with the rapier. They use the science and geometry with swordplay to beautiful and deadly
effect.

## Inspired Panache (Ex) {#inspired-panache}

Each day, an inspired blade gains a number of panache points equal to her Charisma modifier (minimum
1) and Intelligence modifier (minimum 1), instead of just her Charisma modifier.

Unlike other swashbucklers, an inspired blade gains no panache from a killing blow. She gains
panache only from scoring a critical hit with a [rapier](ref/eq-weapon/rapier). This ability alters
the panache class feature.

## Inspired Finesse (Ex) {#inspired-finesse}

At 1st level, an inspired blade gains the benefits of [Weapon Finesse](ref/feat/weapon-finesse) with
the rapier (this ability counts as having the Weapon Finesse feat for the purpose of meeting feat
prerequisites) and gains [Weapon Focus](ref/feat/weapon-focus) (rapier) as a bonus feat. This
ability replaces swashbuckler finesse.

## Deeds {#deeds}

The inspired blade gains the following deeds, each of which replaces an existing deed.

## Inspired Strike (Ex) {#inspired-strike}

At 11th level, an inspired blade can spend 1 panache point when making an attack with a rapier to
gain an insight bonus on that attack roll equal to her Intelligence modifier (minimum +1). When an
inspired blade hits with an attack augmented by inspired strike, she can spend 1 additional panache
point to make the hit a critical threat, though if she does so, she does not regain panache if she
confirms that critical threat. The cost of this deed cannot be reduced by abilities such as
[Signature Deed](ref/feat/signature-deed). This ability replaces bleeding wound.

## Rapier Training (Ex) {#rapier-training}

At 5th level, an inspired blade gains a +1 bonus on attack rolls and a +2 bonus on damage rolls with
rapiers. While wielding a rapier, she gains the benefit of the
[Improved Critical](ref/feat/improved-critical) feat. These attack and damage bonuses increase by 1
for every 4 levels beyond 5th (to a maximum of +4 on attack rolls and +5 on damage rolls at 17th
level). This ability replaces swashbuckler weapon training.

## Rapier Weapon Mastery (Ex) {#rapier-weapon-mastery}

At 20th level, when an inspired blade threatens a critical hit with a rapier, that critical hit is
automatically confirmed. Furthermore, the critical threat range increases by 1 (this increase to the
critical threat range stacks with the increase from rapier training, to a total threat range of
14-20), and the critical modifier of the weapon increases by 1 (×2 becomes ×3, for example). This
ability replaces swashbuckler weapon mastery.
