+++
id = "ref/arc-cavalier/wave-rider"
kind = "archetype"
title = "Wave Rider"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Wave%20Rider"
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
features = [
  { anchor = "seafaring-companion", level = 1 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Mount", feature = "mount", by = ["seafaring-companion"] },
]
+++

Throughout the Inner Sea region, wave riders patrol harbors, keeping them safe from dangerous sea
creatures and watching for smugglers. The most famous of these is the hippocampus-riding Sea Cavalry
of Absalom.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Wave riders are proficient with all simple and martial weapons and with light and medium armor, but
not with shields. This replaces the cavalier's weapon and armor proficiencies.

## Seafaring Companion {#seafaring-companion}

At 1st level, a wave rider gains [Monstrous Mount](ref/feat/monstrous-mount) (see page 14) as a
bonus feat. The wave rider can use this feat only to select a
[hippocampus mount](ref/companion/hippocampus) (see page 14). Otherwise, this ability functions
identically to and replaces the cavalier's [mount](ref/class/cavalier#mount) ability.
