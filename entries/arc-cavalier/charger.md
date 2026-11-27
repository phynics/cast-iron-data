+++
id = "ref/arc-cavalier/charger"
kind = "archetype"
title = "Charger"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Charger"
source_ids = ["inner-sea-monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charger", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "inner-sea-monster-codex"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-mount", level = 1 },
  { anchor = "thundering-hooves", level = 3 },
  { anchor = "courser", level = 4 },
  { anchor = "ride-down", level = 11 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Mount", feature = "mount", by = ["natural-mount"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["thundering-hooves"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["courser"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["ride-down"] },
  { alters = "Class skills" },
]
+++

No warrior better epitomizes the centaur's devastating martial power than the charger. Born to the
swiftest and most powerful of their kind, these natural cavaliers can achieve unparalleled feats of
equestrian combat. Chargers rush headlong into the heart of any conflict to swiftly close on and
smash into their enemies, channeling their power into their lances. Prerequisite:
[Centaur](ref/monster/centaur) (or any tauric creature at the GM's discretion).

## Class Skills {#class-skills}

A charger gains Acrobatics, Knowledge (nature), and Survival as class skills, but does not gain
Climb, Handle Animal, or Ride as class skills. This alters the cavalier's class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A charger is proficient with all simple and martial weapons, with light and medium armor, and with
shields (except tower shields). A charger's cavalier levels stack with any fighter levels he
possesses for the purpose of meeting the level prerequisite for feats that can specify a
[lance](ref/eq-weapon/lance), such as [Weapon Specialization](ref/feat/weapon-specialization). This
replaces the cavalier's weapon and armor proficiencies.

## Natural Mount (Ex) {#natural-mount}

A charger counts as having the [Mounted Combat](ref/feat/mounted-combat) feat only for the purpose
of meeting feat prerequisites, and substitutes the Acrobatics skill for any Ride skill prerequisites
when acquiring feats that have Mounted Combat as a prerequisite. Because of his equine form, a
charger can wield a lance one-handed as if mounted and deals double damage with a lance while
charging. A charger can never gain the benefit of the Mounted Combat feat (or other similar feats or
effects, such as [Trick Riding](ref/feat/trick-riding)) if ridden by another creature. This ability
replaces mount.

## Thundering Hooves (Ex) {#thundering-hooves}

At 3rd level, a charger's hoof attack deals an additional 1d6 points of damage and its critical
threat range increases to 19–20. This effect doesn't stack with any other effect that expands the
critical threat range of a weapon. Whenever he performs a [charge](ref/rule/charge), the charger can
make an additional hoof attack against his target with a -5 penalty on his attack roll. This ability
replaces cavalier's charge.

## Courser (Ex) {#courser}

At 4th level, a charger's constant training increases his land speed by 10 feet. A charger can also
move through up to 10 feet of [difficult terrain](ref/rule/terrain-and-obstacles) each round as if
it were normal terrain. These benefits apply only when he is wearing no armor, light armor, or
medium armor, and not carrying a heavy load. Apply this bonus before modifying the charger's speed
because of any load carried or armor worn. These bonuses stack with any other bonuses to the
charger's land speed or ability to ignore difficult terrain. This ability replaces expert trainer.

## Ride Down (Ex) {#ride-down}

At 11th level, a charger can attempt to [overrun](ref/rule/overrun) any number of targets in the
path of his charge as a free action. For each successful overrun combat maneuver check, the charger
automatically deals an amount of damage to the overrun target equal to that of his hoof attack and
can continue with his charge. If any overrun attempt fails during the charge, the charger's progress
ends in the space directly in front of the target where the maneuver failed. These overrun attempts
do not provoke attacks of opportunity. For each target in the path of his charge, the charger incurs
a cumulative -2 penalty on his overrun combat maneuver checks. This ability replaces mighty charge.
