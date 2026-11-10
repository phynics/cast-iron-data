+++
id = "ref/arc-magus/greensting-slayer"
kind = "archetype"
title = "Greensting Slayer"
source_ids = ["bastards-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "greensting_slayer", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "bastards-of-golarion"
page = "9"

[fields]
kind = "archetype"
replaces = ["Medium armor", "Heavy armor"]
alters = ["Arcane pool"]
replaces_features = ["medium-armor", "heavy-armor"]
alters_features = ["arcane-pool"]
+++

The blending of martial prowess with elven magic has long been a staple of the Blackash Training
Grounds in Erages. More than a few who study at Erages Academy follow this path because of the
promises of wealth that the city's criminal element makes toward practiced brawlers and smugglers.
Greensting slayers have the following class features.

**Arcane Pool**

**Alters:** Arcane pool

**Gained:** At 1st Level

**Special:** If a greensting slayer gets a sneak attack from another source, the bonuses on damage
stack. A greensting slayer cannot use his _arcane pool_ to enhance his weapon.

**Swift:** A greensting slayer can expend 1 point from his _arcane pool_ to add 1d6 points of
[sneak attack](ref/ability/sneak-attack) damage to his next melee attack that round. The attack must
meet all of the usual prerequisites for making a sneak attack, as the [rogue](ref/class/rogue) class
feature.

At 5th level: The amount of sneak attack damage +2d6.

At 9th level: The amount of sneak attack damage +3d6.

At 13th level: The amount of sneak attack damage +4d6.

At 17th level: The amount of sneak attack damage +5d6.

**Evasion (Ex)**

**Gained:** At 7th Level

**Passive:** The greensting slayer gains [evasion](ref/ability/evasion), as the rogue class feature.

**Replaces:** Medium armor

**Improved Evasion (Ex)**

**Gained:** At 13th Level

**Passive:** The greensting slayer gains [improved evasion](ref/talent/improved-evasion), as the
advanced rogue talent of the same name.

**Replaces:** Heavy armor

**Magus Arcana**

**Info:** In addition to the new magus arcana presented below, the following magus arcana complement
the greensting slayer archetype: [close range](ref/arcana/close-range),
[hasted assault](ref/arcana/hasted-assault), [maneuver mastery](ref/arcana/maneuver-mastery),
[pool strike](ref/arcana/pool-strike), and [silent magic](ref/arcana/silent-magic).

**Dark Shifter (Su)**

**Move:** The magus can expend 1 point from his _arcane pool_ to change the target of an ongoing
spell effect with the [darkness](ref/spelldef/darkness) descriptor within 60 feet. The new target
must be within the spell's range, using the magus's level as the effective caster level for the
purpose of determining the maximum range the effect can be moved from the magus.

**Prereq:** 6th-level magus

**Special:** If the spell effect the magus is moving originated from another creature, the magus
must succeed at a caster level check to reposition the effect (DC = 11 + the effect's caster level).
Failure wastes the magus's move action, but does not expend the point from his _arcane pool._
