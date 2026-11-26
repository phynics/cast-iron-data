+++
id = "ref/arc-fighter/calistrian-hunter"
kind = "archetype"
title = "Calistrian Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Calistrian%20Hunter"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calistrian_hunter", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "inner-sea-combat"
page = "36"

[fields]
kind = "archetype"
features = [
  { anchor = "tenacious-tracker", level = 2 },
  { anchor = "vengeance", level = 5 },
  { anchor = "savor-the-sting", level = 9 },
  { anchor = "swift-revenge", level = 13 },
  { anchor = "perceived-wrongs", level = 17 },
  { anchor = "certain-revenge", level = 20 },
]
trades = [
  { replaces = "Armor and weapon proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Bravery", feature = "bravery", by = ["tenacious-tracker"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["vengeance"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["savor-the-sting"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["swift-revenge"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["perceived-wrongs"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["certain-revenge"] },
]
+++

Not every [Calistrian](ref/faith/calistria) who dedicates himself to the goddess can channel divine
magic to track down those who deserve punishment. Like a bounty hunter following his own rules, a
Calistrian hunter tracks down elusive prey using his wits and delivers long-overdue retribution
while easily ignoring his own injuries thanks to the joy he receives from a job well done.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A Calistrian hunter is proficient with all simple and martial weapons, plus the
[whip](ref/eq-weapon/whip). In addition, the hunter is proficient with light and medium armor as
well as shields (except tower shields). This replaces the normal fighter armor and weapon
proficiencies.

## Class Skills {#class-skills}

A Calistrian hunter gains Diplomacy, Knowledge (local), and Perception as class skills and loses
Knowledge (dungeoneering) and Knowledge (engineering) as class skills.

## Tenacious Tracker (Ex) {#tenacious-tracker}

At 2nd level, a Calistrian hunter gains a +1 bonus on Diplomacy checks to gather information and on
Survival checks made to identify or follow tracks. This bonus increases by 1 for every 4 levels the
Calistrian hunter possesses beyond 2nd. This ability replaces bravery.

## Vengeance (Ex) {#vengeance}

At 5th level, a Calistrian hunter deals 1d4 points of [bleed](ref/rule/bleed) damage when he damages
a creature that has damaged him since the beginning of his last turn. Whenever a creature takes
bleed damage from this effect, it also takes a -1 penalty on attack rolls, weapon damage rolls,
saving throws, skill checks, and ability checks for 1 round. This penalty is a
[pain](ref/spelldef/pain) effect and does not stack with the effects of the
[sickened](ref/misc/sickened) condition. This bleed damage increases to 1d6 at 9th level, 1d8 at
13th level, and 2d6 at 17th level. This ability replaces weapon training 1.

## Savor the Sting (Ex) {#savor-the-sting}

At 9th level, whenever a target takes bleed damage from a Calistrian hunter's vengeance ability, the
Calistrian hunter gains an equal number of [temporary hit points](ref/rule/temporary-hit-points).
These temporary hit points last for 1 minute and do not stack with each other. This ability replaces
weapon training 2.

## Swift Revenge (Ex) {#swift-revenge}

At 13th level, a Calistrian hunter gains the quarry class feature; this functions like the
[ranger](ref/class/ranger) ability of the same name, but the target must be one that has damaged the
Calistrian hunter in the past hour. This ability replaces weapon training 3.

## Perceived Wrongs (Ex) {#perceived-wrongs}

At 17th level, a Calistrian hunter can, once per day, use his vengeance ability against any
creature—even one that has not harmed him. If the target is also one that has damaged him since the
beginning of his last turn, the bleed damage increases to 3d6 and the target is sickened for as long
as the bleed effect continues. This ability replaces weapon training 4.

## Certain Revenge (Ex) {#certain-revenge}

At 20th level, a Calistrian hunter gains the improved quarry class feature; this functions like the
ranger ability of the same name, but the target must have attacked him in the past day. Whenever he
uses his vengeance ability against his quarry, the bleed damage increases by 2 per bleed damage die.
This ability replaces weapon mastery.
