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
features = [
  { anchor = "poison-affinity", level = 4 },
  { anchor = "toxic-diet", level = 6 },
]
trades = [
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["toxic-diet"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["poison-affinity"] },
  { alters = "Venom immunity", feature = "venom-immunity", by = ["toxic-diet"] },
]
+++

A mantella focuses on exploring her poisonous heritage, whether or not it has manifested in her own
personal biology. The mantella is an archetype available to grippli druids.

## Poison Affinity (Su) {#poison-affinity}

At 4th level, if a form the mantella assumes with wild shape has any poison abilities, the mantella
also gains those abilities. However, the mantella can never use wild shape to take the form of an
elemental.

This alters wild shape.

## Toxic Diet (Ex) {#toxic-diet}

At 6th level, both the mantella and her animal companion gain immunity to poison. Additionally, as
an immediate action when exposed to a dose of poison, a mantella can absorb the toxin and store it
internally for up to 1 day. As a swift action, a mantella can secrete this poison; this changes the
poison's type to injury and applies the dose of poison to all of the druid's natural attacks. A
mantella can use this ability three times per day, plus one additional time per day at 8th level and
every 2 druid levels thereafter.

This alters venom immunity and replaces spontaneous casting.
