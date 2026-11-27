+++
id = "ref/arc-fighter/crossbowman"
kind = "archetype"
title = "Crossbowman"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Crossbowman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crossbowman", path = "json/archetypes_fighter.json" },
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
  { anchor = "deadshot", level = 3 },
  { anchor = "crossbow-expert", level = 5 },
  { anchor = "improved-deadshot", level = 7 },
  { anchor = "quick-sniper", level = 9 },
  { anchor = "greater-deadshot", level = 11 },
  { anchor = "safe-shot", level = 13 },
  { anchor = "pinpoint-targeting", level = 15 },
  { anchor = "meteor-shot", level = 17 },
  { anchor = "penetrating-shot", level = 19 },
  { anchor = "weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["deadshot"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["crossbow-expert"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["improved-deadshot"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["quick-sniper"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["greater-deadshot"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["safe-shot"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["pinpoint-targeting"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["meteor-shot"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["penetrating-shot"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

The crossbowman has perfected the deadly use of the crossbow, a simple but cruelly efficient weapon,
as a craftsman mastering a lethal tool.

## Deadshot (Ex) {#deadshot}

At 3rd level, when a crossbowman attacks with a crossbow as a [readied action](ref/rule/ready), he
may add 1/2 his Dexterity bonus (minimum +1) on his damage roll. This ability replaces armor
training 1.

## Crossbow Expert (Ex) {#crossbow-expert}

At 5th level, a crossbowman gains a +1 bonus on attack and damage rolls with crossbows. This bonus
increases by +1 per four levels after 5th. This ability replaces weapon training 1.

## Improved Deadshot (Ex) {#improved-deadshot}

At 7th level, when a crossbowman attacks with a crossbow as a readied action, his target is denied
its Dexterity bonus to its AC. This ability replaces armor training 2.

## Quick Sniper (Ex) {#quick-sniper}

At 9th level, a crossbowman gains a bonus equal to 1/2 his fighter level on Stealth checks when
[sniping](ref/skill/stealth). When he is hit with a ranged attack, he can shoot his crossbow at his
attacker as an immediate action if it is loaded. This ability replaces weapon training 2.

## Greater Deadshot (Ex) {#greater-deadshot}

At 11th level, when a crossbowman attacks with a crossbow as a readied action, he may add his
Dexterity bonus (minimum +1) on his damage roll. This ability replaces armor training 3.

## Safe Shot (Ex) {#safe-shot}

At 13th level, a crossbowman does not provoke attacks of opportunity when making ranged attacks with
a crossbow. This ability replaces weapon training 3.

## Pinpoint Targeting {#pinpoint-targeting}

At 15th level, a crossbowman gains [Pinpoint Targeting](ref/feat/pinpoint-targeting) as a bonus
feat. This ability replaces armor training 4.

## Meteor Shot (Ex) {#meteor-shot}

At 17th level, as a standard action, a crossbowman can make one attack with a crossbow at a -4
penalty. If the attack hits, it inflicts damage normally and the target is subject to a
[bull rush](ref/rule/bull-rush) or a [trip](ref/rule/trip) maneuver using the attack roll as the
combat maneuver check. The crossbowman must decide which maneuver to attempt before making his
attack roll. This ability replaces weapon training 4.

## Penetrating Shot (Ex) {#penetrating-shot}

At 19th level, when a crossbowman confirms a critical hit with a crossbow, the bolt pierces the
target and can strike another creature in line behind it. The crossbowman must be able to trace a
line starting at his space and passing through both targets to make this additional attack. The
secondary attack is made at a -4 penalty, in addition to any modifiers for added range. If this
attack is also a critical hit, the bolt can continue to hit another target, but the penalties stack.
This ability replaces armor mastery.

## Weapon Mastery (Ex) {#weapon-mastery}

A crossbowman must choose a type of crossbow.
