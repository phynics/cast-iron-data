+++
id = "ref/arc-slayer/sczarni-executioner"
kind = "archetype"
title = "Sczarni Executioner"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Sczarni%20Executioner"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sczarni_executioner", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-origins"
page = "21"

[fields]
kind = "archetype"
replaces = ["Swift tracker", "Quarry", "improved quarry"]
alters = ["Studied target", "Slayer talent received at 4th level", "Slayer talent received at 10th level"]
replaces_features = ["swift-tracker", "quarry", "improved-quarry"]
alters_features = ["studied-target"]
+++

These professional killers are trained and used almost exclusively by the various Sczarni crime
families. Streetwise and ruthless, they operate independently, often making their talents available
to the highest bidder. Though a few unscrupulous Sczarni executioners exploit this arrangement and
force families to pay higher rates for their services, most of these assassins follow a strict
personal code and maintain absolute transparency with their employers.

**Bloodstained Hands (Ex)**

**Info:** If he ever becomes nonevil, he loses this archetype and becomes a regular slayer.

**Prereq:** A Sczarni executioner must be evil.

**Gained class skills:** app, diplo, ea

**Lost class skills:** kd, kg, ride, sur

**Focused Killer (Ex)**

**Alters:** Studied target

**Gained:** At 1st Level

**Passive:** A Sczarni executioner's _studied target_ bonuses and the DCs of his slayer abilities
increase by 1 against humanoid opponents, but decrease by 1 against non-humanoid targets.

**Painful Strike (Ex)**

**Ability:** A Sczarni executioner automatically gains this talent. A creature that takes sneak
attack damage from a Sczarni executioner must make a successful a Fortitude save (DC = 10 + 1/2 the
Sczarni executioner's class level + his Intelligence modifier) or become
[sickened](ref/misc/sickened) for 1d4 rounds.

**Alters:** Slayer talent received at 4th level

**Flavor:** Sczarni executioners are trained to cause excruciating pain when striking targets, often
leaving them reeling in agony or completely incapacitated as they slowly bleed out.

**Gained:** At 4th Level

**Replaces:** Swift tracker

**Special:** This is considered a Primary Sneak Attack Talent. Only one such talent can be applied
to an individual attack, and the decision of which to use must be made before the attack roll is
made.

**Assassinate (Ex)**

**Ability:** A Sczarni executioner must select the [assassinate](ref/slayertalent/assassinate)
advanced slayer talent.

**Alters:** Slayer talent received at 10th level

**Gained:** At 10th Level

**Swift Death (Ex)**

**Ability:** Once per day a Sczarni executioner can attempt to _assassinate_ a foe without
_studying_ his foe beforehand. He must still succeed at a sneak attack against the target.

**At 19th Level:** He can make two such attacks per day.

**Gained:** At 14th Level

**Replaces:** Quarry, improved quarry
