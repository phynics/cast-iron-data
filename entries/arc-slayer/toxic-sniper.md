+++
id = "ref/arc-slayer/toxic-sniper"
kind = "archetype"
title = "Toxic Sniper"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxic_sniper", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "27"

[fields]
kind = "archetype"
replaces = ["Track", "Slayer talent gained at 2nd level", "Slayer talent gained at 4th level", "Slayer talents gained at 6th, 8th, 12th, 14th, 16th, 18th, and 20th levels", "Slayer talent gained at 10th level"]
alters = ["Weapon and armor proficiency", "Studied target"]
replaces_features = ["track"]
alters_features = ["studied-target"]
+++

Followers of the daemonic harbinger [Cixyron](ref/faith/cixyron) hide throughout the Mana Wastes,
scavenging for guns. With significant firepower in hand, the Furious Thunder's snipers bring
poisonous death to the wastes.

**Weapon and Armor Proficiency**

**Ability:** A toxic sniper is proficient with all simple weapons and firearms. He is proficient
with light armor.

**Alters:** Weapon and armor proficiency

**Scrapper's Gun**

**Ability:** A toxic sniper gains the [Gunsmithing](ref/feat/gunsmithing) feat, a battered gun
identical to that gained by a 1st-level [gunslinger](ref/class/gunslinger), and the ability to
restore his battered gun as if he were a gunslinger.

**Replaces:** Track

**Sharpshooter's Study (Ex)**

**Alters:** Studied target

**Flavor:** A toxic sniper's focus makes him extremely deadly with ranged weapons.

**Info:** He gains a bonus on attack and damage rolls against his _studied target_ only when
attacking with a ranged weapon.

**Toxic Grit (Ex)**

**Ability:** The toxic sniper gains the [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat as a
bonus feat.

**Gained:** At 2nd Level

**Replaces:** Slayer talent gained at 2nd level

**Toxic Shots (Ex)**

**Ability:** A toxic sniper can coat his ammunition in poison without requiring a
[pitted bullet](ref/eq-weapon/pitted-bullet). He is trained in applying poison in this way and
cannot accidentally poison himself when applying poison to his ammunition. The toxic sniper can
create a number of _toxic shots_ per day equal to [half](ref/misc/fractions-and-rounding) his slayer
level plus his Wisdom modifier. The penetrating nature of a _toxic shot_ increases the DC of any
poisons applied in this way by 2.

**Gained:** At 4th Level

**Replaces:** Slayer talent gained at 4th level

**Special:** A toxic sniper cannot create a _toxic shot_ that is part of an
[alchemical cartridge](ref/eq-weapon/alchemical-cartridge).

**Marksman (Ex)**

**At 6th Level:** A toxic sniper reduces the penalty on Stealth checks while sniping by 5.

**At 8th Level:** He increases the distance from which he can deliver a ranged sneak attack against
his _studied target_ by 10 feet.

**Replaces:** Slayer talents gained at 6th, 8th, 12th, 14th, 16th, 18th, and 20th levels

**Precise Toxin (Ex)**

**Ability:** When he hits an opponent with a _toxic shot_ and deals sneak attack damage, he can
forgo all his bonus damage to increase the DC of the his _toxic shot's_ poison. The DC increases by
1 for every 2d6 points of sneak attack damage he forgoes in this way.

**Flavor:** A toxic sniper can deliver a _toxic shot_ to especially vulnerable areas.

**Gained:** At 10th Level

**Replaces:** Slayer talent gained at 10th level
