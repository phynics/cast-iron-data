+++
id = "ref/arc-fighter/aquanaut"
kind = "archetype"
title = "Aquanaut"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Aquanaut"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquanaut", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "aquatic-adventures"
page = "51"

[fields]
kind = "archetype"
replaces = ["Bravery", "Armor training", "armor mastery", "Weapon training"]
alters = ["Armor proficiency", "Bonus feats", "weapon mastery"]
+++

Aquanaut fighters master the movement of water, using its flow to their advantage in combat.

**Armor Proficiency**

**Alters:** Armor proficiency

**Info:** An aquanaut is proficient with light and medium armor, but not with shields.

**Piercing Focus**

**Ability:** If an aquanaut takes a fighter bonus feat that normally requires selecting a single
weapon (except weapon proficiency feats), he can instead apply the feat to all melee piercing
weapons with which he is already proficient and that meet all other prerequisites for that feat.

**Alters:** Bonus feats, weapon mastery

**Special:** This ability counts as having the feat for each such individual weapon for the purpose
of meeting prerequisites. This ability also applies to the _weapon mastery_ class feature.

**Tidal Celerity**

**Gained:** At 2nd Level

**Passive:** An aquanaut gains a +1 bonus on Reflex saves and saving throws against effects that
would immobilize or paralyze him.

**Replaces:** Bravery

At 6th level: The bonus +2.

At 10th level: The bonus +3.

At 14th level: The bonus +4.

At 18th level: The bonus +5.

**Aquadynamic Paragon**

**Ability:** An aquanaut gains a swim speed equal to his unmodified base land speed (if he has a
racial swim speed, he instead increases it by 10 feet).

**Free:** He can choose to have a neutral [buoyancy](ref/rule/buoyancy) once per turn.

**At 11th Level:** Whenever he takes a _move, double move, withdraw,_ or _run_ action underwater, he
can leave a current behind him in the squares along his path; this current has a speed of 10 feet in
the direction of his movement (if his movement was circuitous, so is the current) and lasts until
the beginning of his next turn.

**At 15th Level:** As a **full-round action**, an aquanaut can spin ferociously underwater, creating
a whirlpool around himself with a spinning force that drags all creatures within 120 feet of him 30
feet closer to him. Creatures closer than 30 feet spend the 30 feet of movement circling around the
aquanaut in a single direction of his choice. The whirlpool isn't fast enough to deal damage, but
the aquanaut is unaffected by his own whirlpool, allowing him to make attacks of opportunity against
creatures moving in it.

**At 19th Level:** The aquanaut learns to use the water around him to soften blows, gaining DR 5/-
while underwater.

**At 7th Level:** He can choose any of the five states of buoyancy once per turn as a **free
action**, and can take his buoyancy movement as part of that free action instead of at the end of
his turn without becoming [off-balance](ref/rule/off-balance-and-prone-underwater) and without
requiring a Swim check; additionally, he can choose to double or halve how far a
[current](ref/rule/currents-and-running-water) moves him.

**Gained:** At 3rd Level

**Replaces:** Armor training, armor mastery

**Underwater Training**

**Choice:** An aquanaut chooses bludgeoning, slashing, or piercing melee weapons. If he chooses
piercing melee weapons, he gains a +1 bonus on attack and damage rolls with those weapons when
attacking underwater. If he chooses bludgeoning or slashing melee weapons, he can ignore
[the usual underwater penalties](ref/rule/physical-attacks-underwater) for attacking with those
weapons.

**At 13th Level:** He gains the benefits with his remaining type of melee weapon, and gains another
additional +1 bonus on attack and damage rolls to his previously chosen weapon types.

**At 17th Level:** He gains an additional +1 bonus on attack and damage rolls with all three types.

**At 9th Level:** He can choose another type of melee weapon, applying this ability's initial
benefit to his new choice and gaining an additional +1 bonus on attack and damage rolls to his
previously chosen weapon type.

**Gained:** At 5th Level

**Replaces:** Weapon training
