+++
id = "ref/arc-druid/mantella"
kind = "archetype"
title = "Mantella"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Mantella"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mantella", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "potions-and-poisons"
page = "4"

[fields]
kind = "archetype"
replaces = ["Spontaneous casting"]
alters = ["Wild shape", "Venom immunity"]
replaces_features = ["spontaneous-casting"]
alters_features = ["wild-shape", "venom-immunity"]
+++

A mantella focuses on exploring her poisonous heritage, whether or not it has manifested in her own
personal biology.

**Prerequisites:** Grippli

**Poison Affinity (Su)**

**Alters:** Wild shape

**Info:** If a form the mantella assumes with _wild shape_ has any poison abilities, the mantella
also gains those abilities. However, the mantilla can never use _wild shape_ to take the form of an
elemental.

**Gained:** At 4th Level

**Toxic Diet (Ex)**

**Alters:** Venom immunity

**Immediate:** When exposed to a dose of poison, a mantella can absorb the toxin and store it
internally for up to 1 day.

**Gained:** At 6th Level

**Passive:** Both the mantella and her animal companion gain immunity to poison.

**Replaces:** Spontaneous casting

**Swift:** A mantella can secrete this poison; this changes the poison's type to injury and applies
the dose of poison to all of the druid's natural attacks.

**Usage:** 3 times/day + 1 per 2 druid levels beyond 6th
