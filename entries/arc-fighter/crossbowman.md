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
replaces = ["Armor training 1", "Weapon training 1", "Armor training 2", "Weapon training 2", "Armor training 3", "Weapon training 3", "Armor training 4", "Weapon training 4", "Armor mastery"]
alters = ["Weapon mastery"]
replaces_features = ["armor-mastery"]
alters_features = ["weapon-mastery"]
+++

The crossbowman has perfected the deadly use of the crossbow, a simple but cruelly efficient weapon,
as a craftsman mastering a lethal tool.

**Deadshot (Ex)**

**Ability:** When a crossbowman attacks with a crossbow as a [readied action](ref/rule/ready), he
may add [half](ref/misc/fractions-and-rounding) his Dexterity bonus (minimum +1) on his damage roll.

**Gained:** At 3rd Level

**Replaces:** Armor training 1

**Crossbow Expert (Ex)**

**Gained:** At 5th Level

**Passive:** A crossbowman gains a +1 bonus on attack and damage rolls with crossbows.

**Replaces:** Weapon training 1

At 9th level: This bonus +2.

At 13th level: This bonus +3.

At 17th level: This bonus +4.

**Improved Deadshot (Ex)**

**Gained:** At 7th Level

**Passive:** When a crossbowman attacks with a crossbow as a readied action, his target is denied
its Dexterity bonus to its AC.

**Replaces:** Armor training 2

**Quick Sniper (Ex)**

**Immediate:** When he is hit with a ranged attack, he can shoot his crossbow at his attacker if it
is loaded.

**Gained:** At 9th Level

**Passive:** A crossbowman gains a bonus equal to 1/2 his fighter level on Stealth checks when
[sniping](ref/skill/stealth).

**Replaces:** Weapon training 2

**Greater Deadshot (Ex)**

**Ability:** When a crossbowman attacks with a crossbow as a readied action, he may add his
Dexterity bonus (minimum +1) on his damage roll.

**Gained:** At 11th Level

**Replaces:** Armor training 3

**Safe Shot (Ex)**

**Gained:** At 13th Level

**Passive:** A crossbowman does not provoke attacks of opportunity when making ranged attacks with a
crossbow.

**Replaces:** Weapon training 3

**Pinpoint Targeting**

**Ability:** A crossbowman gains [Pinpoint Targeting](ref/feat/pinpoint-targeting) as a bonus feat.

**Gained:** At 15th Level

**Replaces:** Armor training 4

**Meteor Shot (Ex)**

**Gained:** At 17th Level

**Replaces:** Weapon training 4

**Standard:** A crossbowman can make one attack with a crossbow at a -4 penalty. If the attack hits,
it inflicts damage normally and the target is subject to a [bull rush](ref/rule/bull-rush) or a
[trip](ref/rule/trip) maneuver using the attack roll as the combat maneuver check. The crossbowman
must decide which maneuver to attempt before making his attack roll.

**Penetrating Shot (Ex)**

**Gained:** At 19th Level

**Passive:** When a crossbowman confirms a critical hit with a crossbow, the bolt pierces the target
and can strike another creature in line behind it. The crossbowman must be able to trace a line
starting at his space and passing through both targets to make this additional attack. The secondary
attack is made at a -4 penalty, in addition to any modifiers for added range. If this attack is also
a critical hit, the bolt can continue to hit another target, but the penalties stack.

**Replaces:** Armor mastery

**Weapon Mastery (Ex)**

**Alters:** Weapon mastery

**Info:** A crossbowman must choose a type of crossbow when he receives _weapon mastery._
