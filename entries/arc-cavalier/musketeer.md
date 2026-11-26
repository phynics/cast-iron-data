+++
id = "ref/arc-cavalier/musketeer"
kind = "archetype"
title = "Musketeer"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Musketeer"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "musketeer", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-combat"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "gifted-firearm", level = 1 },
  { anchor = "swift-powder", level = 4 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["gifted-firearm"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["swift-powder"] },
]
+++

Some cavaliers are entrusted by their masters with the care and use of expensive and powerful
oddities—firearms. Capable of inflicting shocking amounts of destruction without the aid of magic,
these musketeers lead the advance of their troops, firing devastating fusillades long before the
enemy can prepare for the armed charge that follows.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A musketeer does not gain proficiency in heavy armor. Musketeers are proficient with all simple and
martial weapons, and with firearms. A cavalier's levels stack with any fighter levels he possesses
for the purpose of meeting the level prerequisite for feats that specifically select a firearm, such
as [Weapon Specialization](ref/feat/weapon-specialization).

## Gifted Firearm (Ex) {#gifted-firearm}

At 1st level, a musketeer is gifted by his order with a firearm (either a
[pistol](ref/eq-weapon/pistol) or a [musket](ref/eq-weapon/musket)). This weapon is both a symbol of
the cavalier's duty and a focus for much of his talent. He cannot sell this weapon. He also gains
the [Gunsmithing](ref/feat/gunsmithing) feat.

Beginning at 8th level, the musketeer can focus himself when wielding his gifted weapon. As a
standard action, he can focus himself to gain a number of benefits for 1 minute per cavalier level.
The musketeer can use this ability twice per day, plus one additional time per day for every four
levels beyond 8th, to a total of five times per day at 20th level.

At 8th level, the cavalier gains the benefit of the [Improved Critical](ref/feat/improved-critical)
feat. At 11th level, he can reduce the misfire chance of his weapon by 1 (to a minimum of 1), and at
17th level, the musketeer can double the range increment of his weapon. The reduction of the
weapon's misfire chance and the doubled range increment abilities don't stack with the similar
benefits of the _[reliable](ref/magic-enh/reliable)_ and _[distance](ref/magic-enh/distance)_ magic
weapon special abilities.

Finally, at 20th level, during a period of such focus, the musketeer can engage in a flurry of
gunfire. The cavalier can expend one of his daily challenges to make a
[full attack](ref/rule/full-attack) with his firearm. The musketeer ignores the normal load times
for his weapon, but must still expend enough doses of powder and enough bullets to complete each
attack.

If the musketeer's gifted firearm is destroyed, the cavalier loses this ability for 30 days while a
replacement weapon is crafted for him. During this 30-day period, the musketeer takes a -1 penalty
on weapon and damage rolls. This ability replaces the standard cavalier's mount ability.

## Swift Powder (Ex) {#swift-powder}

At 4th level, the musketeer gains [Rapid Reload](ref/feat/rapid-reload) (musket) or Rapid Reload
(pistol) as a bonus feat. At 14th level, each time the musketeer issues a challenge, he may reload a
wielded firearm as a free action. This ability replaces expert trainer.
