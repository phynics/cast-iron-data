+++
id = "ref/arc-alchemist/aquachymist"
kind = "archetype"
title = "Aquachymist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Aquachymist"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquachymist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "aquatic-adventures"
page = "49"

[fields]
kind = "archetype"
replaces = ["The discovery at 2nd level"]
alters = ["Alchemy", "Bombs"]
alters_features = ["alchemy"]
+++

The principles of alchemy work equally well underwater and on land, but mixing solutions and keeping
them pure is a tougher task beneath the waves. Aquachymists are those rare few alchemists of
land-dwelling and aquatic races alike who strive to unlock new and fantastic secrets of alchemy that
can be discovered only in the water's depths.

**Gained class skills:** swim

**Lost class skills:** fly

**Sureseal Alchemy (Su)**

**Alters:** Alchemy

**Gained:** At 1st Level

**Passive:** An aquachymist's extracts and mutagens self-generate a flexible outer shell of
_sureseal,_ similar to [sureseal bladders](ref/eq-misc/sureseal-bladder-mundane), allowing the
aquachymist to craft a waterproof supply without expending a plethora of sureseal bladders.

**Underwater Bombs (Su)**

**Ability:** An aquachymist's fire bombs deal steam damage, allowing them to deal damage underwater
or on land. Since thrown weapons don't work well underwater, when the aquachymist creates a bomb, he
either weights it or includes excess air as part of the action of creating the bomb, granting the
bomb his choice of swiftly rising or swiftly sinking [buoyancy](ref/rule/buoyancy) and allowing him
to target foes directly above or below him. If the attack misses, the bomb doesn't deal splash
damage, but instead continues to travel up or down until it loses potency at the end of the
alchemist's turn; the exception is when the aquachymist throws a swiftly sinking bomb close to the
bottom, in which case it might reach the bottom and explode there.

**Alters:** Bombs

**Gained:** At 1st Level

**Special:** Because of the strange aquadynamic features of the aquachymist's underwater bombs, they
have a range increment of only 5 feet above the water.

**Amphibious Mutagen (Su)**

**Gained:** At 2nd Level

**Passive:** An aquachymist's mutagen allows him to breathe both air and water for its duration, in
addition to its other effects.

**Replaces:** The discovery at 2nd level
