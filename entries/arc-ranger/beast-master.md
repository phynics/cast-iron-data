+++
id = "ref/arc-ranger/beast-master"
kind = "archetype"
title = "Beast Master"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Beast%20Master"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beast_master", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-players-guide"
page = "124"

[fields]
kind = "archetype"
replaces = ["Hunter's bond", "6th-level combat style feat", "Camouflage"]
+++

Some rangers, particularly those in primitive lands or who were raised by animals, have unusually
strong bonds with animals. Unique among rangers, they can bond with multiple animals of any kind,
creating a menagerie of wild yet loyal creatures, like a strange family. A beast master has the
following class features.

**Gained class skills:** acro, ea

**Lost class skills:** kd, kg, prof, spc

**Animal Companion (Ex)**

**Ability:** A beast master forms a close bond with an
[animal companion](ref/sidekick/animal-companion).^1^ This ability functions like the druid animal
companion ability except that the ranger's effective druid level is equal to his ranger level - 3.
The ranger gains a +2 bonus on _wild empathy_ and Handle Animal checks made regarding his animal
companion. Unlike a normal ranger, a beast master's choice of animal companion is not limited to a
subset of all possibile animal companion choices - he may choose freely among all animal companion
choices, just as a druid can.

**Ability2:** Each time a beast master's effective druid level increases, he must decide how to
allocate the increase among his animal companions (including the option of adding a new 1st-level
companion). Once an effective druid level is allocated to a particular companion, it cannot be
redistributed while that companion is in the ranger's service (he must release a companion or wait
until a companion dies to allocate its levels to another companion).

**Info:** The beast master may have more than one animal companion, but he must divide up his
effective druid level between his companions to determine the abilities of each companion. For
example, a beast master with an effective druid level of 4 can have one 4th-level companion, two
2nd-level companions, or one 1st-level and one 3rd-level companion.

**Gained:** At 4th Level

**Replaces:** Hunter's bond

**Special:** The _share spells_ animal companion ability does not give the ranger the ability to
cast a single spell so that it affects all of his animal companions.

**Improved Empathic Link (Su)**

**Ability:** The beast master gains^1-2^ an empathic link with all of his animal companions. This
functions like an empathic link with a [familiar](ref/sidekick/familiar), except the ranger can also
see through a companion's eyes as a **swift action**, maintaining this connection as long as he
likes (as long as the companion is within 1 mile) and ending it as a **free action**.

**Gained:** At 6th Level

**Replaces:** 6th-level combat style feat

**Special:** The ranger can only see through the eyes of one companion at a time, and is
[blinded](ref/misc/blinded) while maintaining this connection.

**Strong Bond (Ex)**

**Ability:** The ranger strengthens his bond with his animal companions. The ranger's effective
druid level for his animal companions is now equal to his ranger level; he may immediately allocate
these additional levels to his companions as he sees fit.

**Gained:** At 12th Level

**Replaces:** Camouflage

^1^ The text does not specify when these abilities are granted. The listed levels are an educated
guess, equal to the same level of the features they are replacing.
