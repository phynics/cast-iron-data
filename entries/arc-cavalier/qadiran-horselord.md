+++
id = "ref/arc-cavalier/qadiran-horselord"
kind = "archetype"
title = "Qadiran Horselord"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Qadiran%20Horselord"
source_ids = ["adventurers-guide", "inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "qadiran_horselord", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "adventurers-guide"
page = "12"
[[sources]]
publication = "inner-sea-combat"
page = "42"

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiencies", "Tactician", "Cavalier's charge", "The bonus feat gained at 6th level", "Greater tactician", "Master tactician"]
alters = ["Mount"]
replaces_features = ["weapon-and-armor-proficiencies", "tactician", "cavalier-s-charge", "greater-tactician", "master-tactician"]
alters_features = ["mount"]
+++

The traditions of the Qadiran horselords are now spread throughout Qadira and the lands beyond in
the Inner Sea region, but they originated among the horse-breeders and mounted-combat specialists of
the [Al-Zabriti](ref/rule/aff-deserts); the name "horselord" was applied by outlanders. Qadiran
horselords pride themselves on their mobility and endurance - qualities also found in the breed of
horses they ride. While they don't command the same presence as a host of Lastwall cavalry, Qadiran
horselords can get to a battleground in half the time and on a third of the rations. In battle, they
are skirmishers, ducking in and out of combat with brutal, precise slashes of their scimitars.

**Weapon and Armor Proficiency**

**Info:** A Qadiran horselord is proficient with all simple and martial weapons, with light and
medium armor, and with shields (except tower shields).

**Replaces:** Weapon and armor proficiencies

**Mount (Ex)**

**Alters:** Mount

**Info:** A Qadiran horselord must select a [horse](ref/companion/horse) or
[pony](ref/companion/pony) as his mount. At the GM's discretion, a different mount can be selected.

**Desert Wind (Ex)**

**Passive:** The speed of a Qadiran horselord's mount increases by 5 feet, plus an additional 5 feet
for every 5 cavalier levels he possesses.

**Replaces:** Tactician

**Desert Mastery (Ex)**

**Ability:** A Qadiran horselord gains [favored terrain](ref/ability/favored-terrain) (desert) as
per the [ranger](ref/class/ranger) ability of the same name.

**At 13th Level:** The bonuses increase by 2 again.

**At 18th Level:** The bonuses increase by 2 once again.

**At 8th Level:** The bonus on initiative and skill checks increases by 2, but the Qadiran horselord
never selects additional favored terrains.

**Gained:** At 3rd Level

**Passive:** His mount gains all the benefits of the favored terrain ability.

**Replaces:** Cavalier's charge

**Sand Storm (Ex)**

**Gained:** At 6th Level

**Passive:** A Qadiran horselord gains the benefits of the [Mobility](ref/feat/mobility) feat so
long as he is mounted. Additionally, he deals double damage while using a one-handed slashing weapon
from the back of a charging mount, as though using a [lance](ref/eq-weapon/lance).

**Replaces:** The bonus feat gained at 6th level

**As One (Ex)**

**Ability:** A Qadiran horselord gains the benefits of the [Spring Attack](ref/feat/spring-attack)
feat so long as he is mounted. He uses his mount's movement for this action, and neither he nor his
mount provokes attacks of opportunity from the target. When he makes a single attack with a
one-handed slashing weapon in this way, the attack deals 1d6 additional points of damage.

**At 17th Level:** The bonus damage increases to 3d6.

**Gained:** At 9th Level

**Replaces:** Greater tactician

**Special:** This ability counts as the Spring Attack feat for the purpose of meeting feat
prerequisites, but only while the Qadiran horselord is mounted.

**Sand Scourge (Ex)**

**Fullround:** A Qadiran horselord and his mount can make a tactical rush through enemy ranks. His
mount can move up to twice its normal speed in a straight line. The Qadiran horselord can make a
single attack against each creature he threatens during his mount's movement, up to his normal
number of attacks per round. These attacks use his full base attack bonus and take a -2 penalty;
this is not a charge, and these attacks deal normal damage. The Qadiran horselord provokes attacks
of opportunity during this movement, but his mount does not.

**Gained:** At 17th Level

**Replaces:** Master tactician
