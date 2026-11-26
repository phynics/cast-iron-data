+++
id = "ref/arc-cavalier/oceanrider"
kind = "archetype"
title = "Oceanrider"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Oceanrider"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oceanrider", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "aquatic-adventures"
page = "53"

[fields]
kind = "archetype"
features = [
  { anchor = "aquatic-mount", level = 1 },
]
trades = [
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["aquatic-mount"] },
  { alters = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Mount", feature = "mount", by = ["aquatic-mount"] },
]
+++

Oceanriders are underwater cavaliers who ride dolphins, orcas, or seahorses.

## Armor Proficiency {#armor-proficiency}

An oceanrider is proficient with light and medium armor, and with shields (but not tower shields).

This alters armor proficiency.

## Aquatic Mount {#aquatic-mount}

A Medium oceanrider can ride either a seahorse (_Pathfinder RPG Bestiary 4_ 234) or an
[orca](ref/companion/orca) (unlike most orcas, this one starts at size Large with none of the other
level 7 abilities until level 7) instead of the normal options, while a Small oceanrider can ride a
[dolphin](ref/companion/dolphin).

This alters mount and replaces expert trainer.
