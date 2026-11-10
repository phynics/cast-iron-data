+++
id = "ref/arc-cavalier/huntmaster"
kind = "archetype"
title = "Huntmaster"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Huntmaster"
source_ids = ["animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "huntmaster", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "animal-archive"
page = "6"

[fields]
kind = "archetype"
replaces = ["Mount", "Cavalier's charge", "Banner", "Cavalier bonus feats", "Mighty charge", "Greater banner", "Supreme charge"]
alters = ["Challenge", "Tactician", "greater tactician", "master tactician", "Expert trainer"]
replaces_features = ["mount", "cavalier-s-charge", "banner", "mighty-charge", "greater-banner", "supreme-charge"]
alters_features = ["challenge", "tactician", "greater-tactician", "master-tactician", "expert-trainer"]
+++

Huntmasters train the beasts favored by lordly castes into swift and deadly trackers.

**Gained class skills:** kna, stl, sur

**Weapon and Armor Proficiency**

**Info:** A huntmaster is not proficient with heavy armor. Huntmasters are proficient with all
simple and martial weapons, plus the [net](ref/eq-weapon/net) and [whip](ref/eq-weapon/whip).

**Hunting Pack (Ex)**

**Action:** Ability

**Gained:** At 1st Level

**Passive:** A huntmaster's animal companions gain a bonus on Survival checks to follow tracks equal
to [half](ref/misc/fractions-and-rounding) the cavalier's class level (minimum 1).

**Replaces:** Mount

A huntmaster forms a close bond with an animal companion. This animal companion functions as a
druid's animal companion, using the cavalier's level as his effective druid level. He can choose
either a [bird](ref/companion/bird) or a [dog](ref/companion/dog) when selecting his animal
companion.

The huntmaster can have more than one [animal companion](ref/sidekick/animal-companion), but he must
divide up his effective druid level between his companions to determine the abilities of each
companion. Each time a huntmaster's effective druid level increases, he must decide how to allocate
the increase among his animal companions (including the option of adding a new 1st-level companion).
Once an effective druid level is allocated to a particular companion, it cannot be redistributed
while that companion is in the huntmaster's service (he must release a companion or wait until a
companion dies to allocate its levels to another companion). The _share spells_ animal companion
ability does not give the huntmaster the ability to cast a single spell so that it affects all of
his animal companions.

**Bestial Challenge (Ex)**

**Alters:** Challenge

**Passive:** Whenever a huntmaster issues a challenge, both he and his _hunting pack_ gain the
bonuses and penalties associated with his challenge.

**Tactician (Ex)**

**Alters:** Tactician, greater tactician, master tactician

**Info:** A huntmaster's tactician ability affects only his _hunting pack,_ not other allies.

**Takedown (Ex)**

**Ability:** A huntmaster's dog can make a free [trip](ref/rule/trip) or
[dirty trick](ref/rule/dirty-trick) ([entangled](ref/rule/entangled)) combat maneuver after a
successful melee attack. A huntmaster's bird can make a free dirty trick
([dazzled](ref/misc/dazzled) or [deafened](ref/misc/deafened)) combat maneuver after a successful
melee attack; if the target is already dazzled, the bird can choose dirty trick
([blinded](ref/misc/blinded)) instead. These combat maneuvers do not provoke attacks of opportunity.

**Gained:** At 3rd Level

**Replaces:** Cavalier's charge

**Animal Trainer (Ex)**

**Ability:** A huntmaster's _expert trainer_ ability applies to birds and dogs rather than mounts.

**Alters:** Expert trainer

**Gained:** At 4th Level

**Swift Tracker (Ex)**

**Ability:** A huntmaster gains the swift tracker ability, as the [ranger](ref/class/ranger) ability
of the same name.

**Gained:** At 5th Level

**Replaces:** Banner

**Bonus Feats**

**At 12th Level:** They gain [Following Step](ref/feat/following-step).

**At 18th Level:** They gain [Step Up and Strike](ref/feat/step-up-and-strike).

**At 6th Level:** A huntmaster and all members of his _hunting pack_ gain
[Step Up](ref/feat/step-up) as a bonus feat.

**Replaces:** Cavalier bonus feats

**Pack Attack (Ex)**

**Ability:** Whenever a huntmaster and any of his _hunting pack_ or multiple animals in his _hunting
pack_ are adjacent and attack the same target in melee, they are treated as
[flanking](ref/rule/flanking). In addition, they can flank a creature with
[improved uncanny dodge](ref/ability/improved-uncanny-dodge) if the huntmaster has at least 4 more
levels than the target.

**Gained:** At 11th Level

**Replaces:** Mighty charge

**Quarry (Ex)**

**Ability:** A huntmaster gains _quarry,_ as the ranger ability of the same name. The benefits of
this ability also apply to his hunting pack.

**Gained:** At 14th Level

**Replaces:** Greater banner

**Improved Quarry (Ex)**

**Ability:** A huntmaster gains _improved quarry,_ as the ranger ability of the same name. The
benefits of this ability also apply to his hunting pack.

**Gained:** At 20th Level

**Replaces:** Supreme charge
