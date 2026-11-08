+++
id = "ref/arc-fighter/calistrian-hunter"
kind = "archetype"
title = "Calistrian Hunter"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calistrian_hunter", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]

[fields]
kind = "archetype"
replaces = ["Armor and weapon proficiencies", "Bravery", "Weapon training 1", "Weapon training 2", "Weapon training 3", "Weapon training 4", "Weapon mastery"]
+++

**Sources:** Inner Sea Combat pg 36\
Not every [Calistrian](ref/faith/calistria) who dedicates himself to the goddess can channel divine
magic to track down those who deserve punishment. Like a bounty hunter following his own rules, a
Calistrian hunter tracks down elusive prey using his wits and delivers long-overdue retribution
while easily ignoring his own injuries thanks to the joy he receives from a job well done.

**Weapon and Armor Proficiency**

**Info:** A Calistrian hunter is proficient with all simple and martial weapons, plus the
[whip](ref/eq-weapon/whip). In addition, the hunter is proficient with light and medium armor as
well as shields (except tower shields).

**Replaces:** Armor and weapon proficiencies

**Gained class skills:** diplo, kl, per

**Lost class skills:** kd, ke

**Tenacious Tracker (Ex)**

**Gained:** At 2nd Level

**Passive:** A Calistrian hunter gains a +1 bonus on Diplomacy checks to gather information and on
Survival checks made to identify or follow tracks.

**Replaces:** Bravery

At 6th level: This bonus +2.

At 10th level: This bonus +3.

At 14th level: This bonus +4.

At 18th level: This bonus +5.

**Vengeance (Ex)**

**Ability:** A Calistrian hunter deals 1d4 points of [bleed](ref/rule/bleed) damage when he damages
a creature that has damaged him since the beginning of his last turn. Whenever a creature takes
bleed damage from this effect, it also takes a -1 penalty on attack rolls, weapon damage rolls,
saving throws, skill checks, and ability checks for 1 round. This penalty is a
[pain](ref/spelldef/pain) effect and does not stack with the effects of the
[sickened](ref/misc/sickened) condition.

**At 13th Level:** The bleed increases to 1d8.

**At 17th Level:** The bleed damage increases to 2d6.

**At 9th Level:** The bleed damage becomes 1d6.

**Gained:** At 5th Level

**Replaces:** Weapon training 1

**Savor the Sting (Ex)**

**Gained:** At 9th Level

**Passive:** Whenever a target takes bleed damage from a Calistrian hunter's _vengeance_ ability,
the Calistrian hunter gains an equal number of
[temporary hit points](ref/rule/temporary-hit-points). These temporary hit points last for 1 minute
and do not stack with each other.

**Replaces:** Weapon training 2

**Swift Revenge (Ex)**

**Ability:** A Calistrian hunter gains the quarry class feature; this functions like the
[ranger](ref/class/ranger) ability of the same name, but the target must be one that has damaged the
Calistrian hunter in the past hour.

**Gained:** At 13th Level

**Replaces:** Weapon training 3

**Perceived Wrongs (Ex)**

**Ability:** A Calistrian hunter can, once per day, use his _vengeance_ ability against any
creature - even one that has not harmed him. If the target is also one that has damaged him since
the beginning of his last turn, the bleed damage increases to 3d6 and the target is sickened for as
long as the bleed effect continues.

**Gained:** At 17th Level

**Replaces:** Weapon training 4

**Certain Revenge (Ex)**

**Ability:** A Calistrian hunter gains the _improved quarry_ class feature; this functions like the
ranger ability of the same name, but the target must have attacked him in the past day. Whenever he
uses his _vengeance_ ability against his quarry, the bleed damage increases by 2 per bleed damage
die.

**Gained:** At 20th Level

**Replaces:** Weapon mastery
