+++
id = "ref/arc-cavalier/oceanrider"
kind = "archetype"
title = "Oceanrider"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oceanrider", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]

[fields]
kind = "archetype"
replaces = ["Expert trainer"]
alters = ["Armor proficiency", "Mount"]
+++

**Sources:** Aquatic Adventures pg 53\
Oceanriders are underwater cavaliers who ride dolphins, orcas, or seahorses.

**Armor Proficiency**

**Alters:** Armor proficiency

**Info:** An oceanrider is proficient with light and medium armor, and with shields (but not tower
shields).

**Aquatic Mount**

**Alters:** Mount

**Info:** A Medium oceanrider can ride either a [giant seahorse](ref/companion/seahorse-giant) or an
[orca](ref/companion/orca) (unlike most orcas, this one starts at size Large with none of the other
level 7 abilities until level 7) instead of the normal options, while a Small oceanrider can ride a
[dolphin](ref/companion/dolphin).

**Replaces:** Expert trainer
