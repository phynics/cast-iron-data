+++
id = "ref/arc-cavalier/wave-rider"
kind = "archetype"
title = "Wave Rider"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wave_rider", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "inner-sea-combat"
page = "47"

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiencies"]
alters = ["Mount"]
replaces_features = ["weapon-and-armor-proficiencies"]
alters_features = ["mount"]
+++

Throughout the Inner Sea region, wave riders patrol harbors, keeping them safe from dangerous sea
creatures and watching for smugglers. The most famous of these is the hippocampus-riding Sea Cavalry
of Absalom.

**Weapon and Armor Proficiency**

**Info:** Wave riders are proficient with all simple and martial weapons and with light and medium
armor, but not with shields.

**Replaces:** Weapon and armor proficiencies

**Seafaring Companion**

**Ability:** A wave rider gains [Monstrous Mount](ref/feat/monstrous-mount) as a bonus feat. The
wave rider can use this feat only to select a [hippocampus mount](ref/companion/hippocampus).
Otherwise, this ability functions identically to the cavalier's _[mount](ref/spell/mount)_ ability.

**Alters:** Mount

**Gained:** At 1st Level
