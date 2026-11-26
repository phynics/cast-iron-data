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
features = [
  { anchor = "bloodstained-hands" },
  { anchor = "focused-killer", level = 1 },
  { anchor = "painful-strike", level = 4 },
  { anchor = "assassinate", level = 10 },
  { anchor = "swift-death", level = 14 },
]
trades = [
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["painful-strike"] },
  { replaces = "Quarry", feature = "quarry", by = ["swift-death"] },
  { replaces = "improved quarry", feature = "improved-quarry", by = ["swift-death"] },
  { alters = "Studied target", feature = "studied-target", by = ["focused-killer"] },
  { alters = "Slayer talent received at 4th level", feature = "slayer-talents", levels = [4], by = ["painful-strike"] },
  { alters = "Slayer talent received at 10th level", feature = "slayer-talents", levels = [10], by = ["assassinate"] },
]
+++

These professional killers are trained and used almost exclusively by the various Sczarni crime
families. Streetwise and ruthless, they operate independently, often making their talents available
to the highest bidder. Though a few unscrupulous Sczarni executioners exploit this arrangement and
force families to pay higher rates for their services, most of these assassins follow a strict
personal code and maintain absolute transparency with their employers.

Talents marked with an asterisk (\*) add effects to a slayer's sneak attack. Only one of these
talents can be applied to an individual attack, and the decision of which to use must be made before
the attack roll is made.

## Class Skills {#class-skills}

A Sczarni executioner doesn't receive Knowledge (dungeoneering) (Int), Knowledge (geography) (Int),
Ride (Dex), or Survival (Wis) as class skills. Instead, he receives Appraise (Int), Diplomacy (Cha),
and Escape Artist (Dex) in addition to the other standard slayer class skills.

## Bloodstained Hands (Ex) {#bloodstained-hands}

A Sczarni executioner must be evil. If he ever becomes nonevil, he loses this archetype and becomes
a regular slayer.

## Focused Killer (Ex) {#focused-killer}

At 1st level, a Sczarni executioner's studied target bonuses and the DCs of his slayer abilities
increase by 1 against humanoid opponents, but decrease by 1 against non-humanoid targets. This
ability alters studied target.

## Painful Strike\* (Ex) {#painful-strike}

At 4th level, a Sczarni executioner automatically gains this talent. Sczarni executioners are
trained to cause excruciating pain when striking targets, often leaving them reeling in agony or
completely incapacitated as they slowly bleed out. A creature that takes sneak attack damage from a
Sczarni executioner must make a successful a Fortitude save (DC = 10 + 1/2 the Sczarni executioner's
class level + his Intelligence modifier) or become [sickened](ref/misc/sickened) for 1d4 rounds.
This ability alters the slayer talent received at 4th level and replaces swift tracker.

## Assassinate (Ex) {#assassinate}

At 10th level, a Sczarni executioner must select the [assassinate](ref/slayertalent/assassinate)
advanced slayer talent.

## Swift Death (Ex) {#swift-death}

At 14th level, once per day a Sczarni executioner can attempt to assassinate a foe without studying
his foe beforehand. He must still succeed at a sneak attack against the target. At 19th level, he
can make two such attacks per day. This ability replaces quarry and improved quarry.
