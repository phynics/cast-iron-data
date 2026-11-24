+++
id = "ref/arc-rogue/investigator"
kind = "archetype"
title = "Investigator"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Investigator"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "investigator", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "133"

[fields]
kind = "archetype"
features = [
  { anchor = "follow-up", level = 1 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["follow-up"] },
]
+++

> _**Note:** This is a rogue archetype, and has no relation to the
> [investigator](ref/class/investigator) hybrid class._

Not all rogues work against the law. Investigators use their skills to serve the law, often in the
employ of nobles or in the pursuit of noble causes. In some cities cabals of investigators work for
rulers or bureaucracies, but often an investigator is a free agent who pursues whatever mysteries
come across her path. Of course, not all investigators serve the law. Crime lords and guildmasters
often have squads of investigators serving their own nefarious purposes.

## Follow Up (Ex) {#follow-up}

An investigator can roll twice on any Diplomacy check made to gather information, and receives the
information for both results. This takes the same amount of time as one check. If the lesser of the
two checks reveals false information, the rogue is aware of it. False information is not revealed in
this way if the people she questioned do not know it to be false. This ability replaces trapfinding.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the investigator archetype: coax information, fast picks,
follow clues, hard to fool, and minor magic.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the investigator archetype: hunter's surprise,
slippery mind, and thoughtful reexamining.
